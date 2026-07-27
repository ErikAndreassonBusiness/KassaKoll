# Responsibility: Connect the routers, static/frontend assets, and setup configuration

from fastapi.staticfiles import StaticFiles
from app.server import app
from app.server.routers.routers import router as api_router
from app.server.routers.static_routers import router as static_router

# Mount static files
app.mount("/static", StaticFiles(directory="app/client/static"), name="static")

# Include routers
app.include_router(api_router)     # Handles API endpoints
app.include_router(static_router)  # Handles HTML pages