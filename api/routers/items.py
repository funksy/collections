from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from queries.items import (
    ItemsRepository,
    ItemIn,
    ItemUpdate,
    ItemOut,
    ItemListOut,
    DataStructureException,
    InvalidCollectionIdException,
    RequiredFieldException,
)
from queries.users import UserRepository


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post(
    "/{username}/collections/{collection_id}/items", response_model=ItemOut, tags=["items"]
)
def create_item(
    collection_id: str,
    data: ItemIn,
    user_repo: UserRepository = Depends(),
    repo: ItemsRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    owner = user_repo.get_current_user(token).username
    return repo.create_item(owner, collection_id, data)



@router.get(
    "/{username}/collections/{collection_id}/items/{item_id}",
    response_model=ItemOut,
    tags=["items"],
)
def get_item(
    item_id: str,
    repo: ItemsRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.get_item(item_id)


@router.delete("/{username}/collections/{collection_id}/items/{item_id}", tags=["items"])
def delete_item(
    item_id: str,
    user_repo: UserRepository = Depends(),
    repo: ItemsRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    current_user = user_repo.get_current_user(token).username
    return repo.delete_item(current_user, item_id)


@router.put("/{username}/collections/{collection_id}/items/{item_id}", tags=["items"])
def update_item(
    item_id: str,
    item_update: ItemUpdate,
    user_repo: UserRepository = Depends(),
    repo: ItemsRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    current_user = user_repo.get_current_user(token).username
    return repo.update_item(current_user, item_id, item_update)


@router.get(
    "/{username}/collections/{collection_id}/items", response_model=ItemListOut, tags=["items"]
)
def get_list_of_items(
    collection_id: str,
    repo: ItemsRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.get_list_of_items(collection_id)
