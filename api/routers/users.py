from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from queries.users import (
    UserRepository,
    UserIn,
    UserOut,
    UserToken,
)

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token", response_model=UserToken, tags=["users"])
def generate_token(
    repo: UserRepository = Depends(), form_data: OAuth2PasswordRequestForm = Depends()
):
    return repo.generate_token(form_data)


@router.get("/token/current", response_model=UserOut, tags=["users"])
async def get_current_user(
    repo: UserRepository = Depends(), token: str = Depends(oauth2_scheme)
):
    return repo.get_current_user(token)


@router.post("/users", response_model=UserOut, tags=["users"])
def create_user(user: UserIn, repo: UserRepository = Depends()):
    return repo.create_user(user)


@router.get("/users/{username}", response_model=UserOut, tags=["users"])
def get_user(username: str, repo: UserRepository = Depends()):
    return repo.get_user(username)
