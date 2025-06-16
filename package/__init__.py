from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from .api.v1.endpoints import router as predict
from .router.oauth import router as oauth
from .router.frontend import router as frontend
from dotenv import load_dotenv
import os

load_dotenv()

def create_app() -> FastAPI:
    app = FastAPI()

    # Load environment variables
    secret_key = os.getenv("SECRET_KEY")
    if not secret_key:
        raise ValueError("SECRET_KEY environment variable is not set.")
    

    # Session middleware setup
    app.add_middleware(
            SessionMiddleware,
            secret_key=secret_key,
            session_cookie="session",
            max_age=14 * 24 * 60 * 60  # 14 days in seconds
    )


    # CORS configuration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Adjust this to your needs
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    # Correctly mount static files
    app.mount("/static", StaticFiles(directory="package/static"), name="static")

    # Include the router
    app.include_router(oauth)
    app.include_router(frontend)
    app.include_router(predict)


    return app