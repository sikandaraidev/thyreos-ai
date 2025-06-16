from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

router = APIRouter()

templates = Jinja2Templates(directory="package/templates")

# Mount static files correctly
router.mount("/static", StaticFiles(directory="package/static"), name="static")


# Serve index.html for all routes
@router.get("/", name="home")
async def serve_spa(request: Request):
    # if user is None:
    #    return RedirectResponse(url="/auth/login")
    
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": "Home Page"}
        )


@router.get("/login")
async def login(request: Request):

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "message": "Home Page"}
        )

    # return RedirectResponse(url="/auth/login/google")


@router.get("/signup")
async def signup(request: Request):

    return templates.TemplateResponse(
        "signup.html",
        {"request": request, "message": "Home Page"}
        )

    # return RedirectResponse(url="/auth/signup/google")

