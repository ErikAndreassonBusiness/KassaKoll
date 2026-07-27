# Responsibility: Route requests to HTML templates for pages like Login, Dashboard, etc.

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Init route
router = APIRouter(tags=["Page Navigation"])
templates = Jinja2Templates(directory="app/client/templates")


@router.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"title": "KassaKoll - Likviditetsprognos"}
    )


@router.get("/login", response_class=HTMLResponse)
async def read_login(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="login.html", 
        context={"title": "KassaKoll - Logga in"}
    )