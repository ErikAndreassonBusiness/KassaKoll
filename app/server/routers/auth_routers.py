import base64
import secrets
import httpx
import os
from dotenv import load_dotenv
from fastapi import APIRouter, Request, HTTPException, Response
from fastapi.responses import RedirectResponse, HTMLResponse

router = APIRouter(prefix="/auth/fortnox", tags=["Auth"]) #crete auth_router

# --- Helper functions
load_dotenv()
def get_client_id():
   return os.getenv("FORTNOX_CLIENT_ID")

def get_secret_id():
   return os.getenv("FORTNOX_SECRET_ID")


# ---------------------------------------------------------------------------
# CONFIGURATION - Replace with your Fortnox Developer Credentials
# ---------------------------------------------------------------------------
FORTNOX_AUTH_URL = "https://apps.fortnox.se/oauth-v1/auth"
FORTNOX_TOKEN_URL = "https://apps.fortnox.se/oauth-v1/token"

CLIENT_ID = get_client_id()
CLIENT_SECRET = get_secret_id()
REDIRECT_URI = "http://127.0.0.1:8000/api/auth/fortnox/callback"
SCOPES = "invoice"  # Match scopes configured in Fortnox Developer Portal

# Temporary in-memory token storage for testing (Replace with DB in production)
tokens_db = {}


# ---------------------------------------------------------------------------
# 1. Redirects browser to Fortnox
# ---------------------------------------------------------------------------
@router.get("/login")
async def fortnox_login():
    state_token = secrets.token_urlsafe(16)

    auth_url = (
        f"{FORTNOX_AUTH_URL}?"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"scope={SCOPES}&"
        f"state={state_token}&"
        f"response_type=code"
    )

    redirect = RedirectResponse(url=auth_url)
    # Secure HTTP-only cookie prevents CSRF attacks
    redirect.set_cookie(key="oauth_state", value=state_token, httponly=True)
    return redirect


# ---------------------------------------------------------------------------
# 2. Receives Auth Code & Swaps for Access Token
# ---------------------------------------------------------------------------
@router.get("/callback")
async def fortnox_callback(request: Request, code: str, state: str):
    # Security check: verify state token matches cookie
    saved_state = request.cookies.get("oauth_state")
    if not saved_state or saved_state != state:
        raise HTTPException(
            status_code=400, detail="Security error: State parameter mismatch."
        )

    # Basic Auth Header: base64(client_id:client_secret)
    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }

    # Server-to-Server POST request to retrieve tokens
    async with httpx.AsyncClient() as client:
        response = await client.post(
            FORTNOX_TOKEN_URL, headers=headers, data=payload
        )

    if response.status_code != 200:
        raise HTTPException(
            status_code=400,
            detail=f"Token exchange failed ({response.status_code}): {response.text}",
        )

    token_data = response.json()
    
    # Save tokens to local store
    tokens_db["access_token"] = token_data.get("access_token")
    tokens_db["refresh_token"] = token_data.get("refresh_token")

    print("\n================ FORTNOX TOKENS RECEIVED ================")
    print(f"Access Token : {tokens_db['access_token']}")
    print(f"Refresh Token: {tokens_db['refresh_token']}")
    print("=========================================================\n")

    # Redirect user to the dashboard shell
    redirect = RedirectResponse(url="/")
    redirect.delete_cookie("oauth_state")
    return redirect


# ---------------------------------------------------------------------------
# 3. TEST DATA ROUTE: Backend fetches Fortnox data on behalf of Frontend
# ---------------------------------------------------------------------------
@router.get("/company-information")
async def get_company_info():
    access_token = tokens_db.get("access_token")
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated with Fortnox.")

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
    }

    async with httpx.AsyncClient() as client:
        res = await client.get("https://api.fortnox.se/3/companyinformation", headers=headers)

    if res.status_code != 200:
        raise HTTPException(status_code=res.status_code, detail=res.text)

    return res.json()