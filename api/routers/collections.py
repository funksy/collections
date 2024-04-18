from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from queries.collections import (
    CollectionRepository,
    CollectionIn,
    CollectionOut,
    CollectionListOut,
)


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/collections", response_model=CollectionOut, tags=["collections"])
def create_collection(
    collection: CollectionIn,
    repo: CollectionRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.create_collection(collection)


@router.get(
    "/collections/{collection_id}", response_model=CollectionOut, tags=["collections"]
)
def get_collection(
    collection_id: str,
    repo: CollectionRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.get_collection(collection_id)


@router.delete("/collections/{collection_id}", tags=["collections"])
def delete_collection(
    collection_id: str,
    repo: CollectionRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.delete_collection(collection_id)


@router.put("/collections/{collection_id}", tags=["collections"])
def update_collection(
    collection_id: str,
    collection: CollectionIn,
    repo: CollectionRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.update_collection(collection_id, collection)


@router.get("/collections", response_model=CollectionListOut, tags=["collections"])
def get_collections(
    repo: CollectionRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.get_list_of_collections()
