import requests

import os
from dotenv import load_dotenv

def get_client_id(): 
    load_dotenv()
    return os.getenv("FORTNOX_CLIENT_ID")

def get_secret_id():
    load_dotenv()
    return os.getenv("FORTNOX_SECRET_ID")

def get_auth_code():
    client_id = get_client_id()
    secret_id = get_secret_id()
    url = f"https://apps.fortnox.se/oauth-v1/auth?client_id={client_id}&redirect_uri=https%3A%2F%2Fmysite.org%2Factivation&scope=companyinformation&state=somestate123&access_type=offline&response_type=code&account_type=service"

def authorize_integration(): 
    """
    1. The App Backend attempts to access a resource that requires authorization that it does not have. It redirects the user to the authorization server for authentication.
    2. The Authorization Server authenticates the user by asking for their login credentials. The server determines if the user should be granted or denied their request.
    3. If the User is determined to be authentic, an Authorization-Code is issued and returned to the App Frontend. This code is used to retrieve an Access-Token from the Authorization Server.
    4. The retrieved Authorization-Code is sent to the App Backend.
    5. The App Backend makes a POST request to the Authorization Server, containing its Client-ID, Client-Secret, and Authorization-Code.
    6. The Authorization Server verifies the key, secret and code, and issues an Access-Token and Refresh-Token.
    7. The App Backend receives and processes the Access-Token. The Access-Token is then kept in the App Backend, which can request resources on behalf of the App Frontend without exposing the token itself.
    """

    auth_code = get_auth_code()