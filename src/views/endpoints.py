from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


CURRENT_PATH = Path(__file__).parent


pages_router = APIRouter()
templates = Jinja2Templates(directory= CURRENT_PATH / "templates")


@pages_router.get("/signin")
async def signin(request: Request):
    return templates.TemplateResponse("signin_form.html",
        context={
            "request": request
        }
    )


