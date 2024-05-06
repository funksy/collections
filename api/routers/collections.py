from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from queries.collections import (
    CollectionRepository,
    CollectionIn,
    CollectionUpdate,
    CollectionOut,
    CollectionListOut,
)
from queries.users import UserRepository


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post(
    "/{username}/collections", response_model=CollectionOut, tags=["collections"]
)
def create_collection(
    collection: CollectionIn,
    user_repo: UserRepository = Depends(),
    repo: CollectionRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    owner = user_repo.get_current_user(token).username
    return repo.create_collection(owner, collection)


@router.get(
    "/{username}/collections/{collection_id}",
    response_model=CollectionOut,
    tags=["collections"],
)
def get_collection(
    collection_id: str,
    repo: CollectionRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.get_collection(collection_id)


@router.delete("/{username}/collections/{collection_id}", tags=["collections"])
def delete_collection(
    collection_id: str,
    user_repo: UserRepository = Depends(),
    repo: CollectionRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    current_user = user_repo.get_current_user(token).username
    return repo.delete_collection(current_user, collection_id)


@router.put("/{username}/collections/{collection_id}", tags=["collections"])
def update_collection(
    collection_id: str,
    collection_update: CollectionUpdate,
    user_repo: UserRepository = Depends(),
    repo: CollectionRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    current_user = user_repo.get_current_user(token).username
    return repo.update_collection(current_user, collection_id, collection_update)


@router.get(
    "/{username}/collections", response_model=CollectionListOut, tags=["collections"]
)
def get_collections_by_owner(
    username: str,
    repo: CollectionRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.get_list_of_collections_by_owner(username)