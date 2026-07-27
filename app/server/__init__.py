from pathlib import Path
from fastapi import FastAPI

# Responsibility: Create and expose the app instance

# --- Dynamic folder-finding ---
APP_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = APP_DIR / "client" / "templates"

app = FastAPI(title="KassaKoll API")

# # ======== Page Routers ========
app.frontend("/", directory=str(TEMPLATES_DIR))


# router.frontend("/", directory=str(TEMPLATES_DIR))
# router.frontend("/login", directory=str(TEMPLATES_DIR))
# router.frontend("/dashboard", directory=str(TEMPLATES_DIR), fallback="index.html")

# app.include_router(router)