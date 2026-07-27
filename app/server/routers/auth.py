# app/routers/auth.py

import requests
import os
from dotenv import load_dotenv

import secrets
from fastapi import APIRouter, Response
from fastapi.responses import RedirectResponse

# --- Helper functions
def get_client_id(): 
    load_dotenv()
    return os.getenv("FORTNOX_CLIENT_ID")

def get_secret_id():
    load_dotenv()
    return os.getenv("FORTNOX_SECRET_ID")


router = APIRouter(prefix="/api/auth/fortnox", tags=["Auth"])

FORTNOX_AUTH_URL = f"https://apps.fortnox.se/oauth-v1/auth?client_id={get_client_id()}&redirect_uri=https%3A%2F%2Fmysite.org%2Factivation&scope=companyinformation&state=somestate123&access_type=offline&response_type=code&account_type=service"
CLIENT_ID = get_client_id()
REDIRECT_URI = "https://127.0.0.1/api/auth/fortnox/callback"
SCOPES = "bookkeeping invoice"  # Space-separated list of scopes you need

@router.get("/login")
async def fortnox_login(response: Response):
    # Generate a random state token
    state_token = secrets.token_urlsafe(16)
    
    auth_url = (
        f"{FORTNOX_AUTH_URL}?"
        f"client_id={CLIENT_ID}&"
        f"redirect_uri={REDIRECT_URI}&"
        f"scope={SCOPES}&"
        f"state={state_token}&"
        f"response_type=code"
    )
    
    # Store state in a secure HTTP-only cookie to check during callback
    redirect = RedirectResponse(url=auth_url)
    redirect.set_cookie(key="oauth_state", value=state_token, httponly=True)
    return redirect


