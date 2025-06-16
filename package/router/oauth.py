from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import APIRouter, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from package.core.config import settings
# from fastapi.responses import RedirectResponse

router = APIRouter()

templates = Jinja2Templates(directory="package/templates")

# Mount static files correctly
router.mount("/static", StaticFiles(directory="package/static"), name="static")


oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    client_kwargs={
        'scope': 'openid email profile'
    },
)


@router.get("/auth/login")
async def login_with_google(request: Request):
    redirect_uri = settings.GOOGLE_REDIRECT_URI
    print(f"Redirect URI: {redirect_uri}")
    if not redirect_uri:
        raise HTTPException(status_code=500, detail="Google redirect URI is not set.")
    
    # redirect_uri = redirect_uri.replace("http://", "https://")

    return await oauth.google.authorize_redirect(request, redirect_uri)



@router.get('/auth/google/callback')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during authentication {e}.")
    user = token.get('userinfo')
    if user:
        request.session['user'] = dict(user)
    return templates.TemplateResponse(
        name='index.html',
        request=request,
        context={'user': user, 'message': 'Login successful!'},
        url='/'
    )

@router.get('/auth/logout')
async def logout(request: Request):
    request.session.pop('user', None)
    return templates.TemplateResponse(
        name='index.html',
        request=request,
        context={'message': 'Logged out successfully!'},
        url='/'
    )

@router.get('/auth/me')
async def get_current_user(request: Request):
    user = request.session.get('user')
    return {'user': user}
