from fastapi import APIRouter, Depends, Response
from queries.collections import (
    CollectionRepository,
    CollectionIn,
    CollectionOut,
    CollectionListOut,
)


router = APIRouter()


@router.post("/collections", response_model=CollectionOut, tags=["collections"])
def create_collection(
    collection: CollectionIn,
    repo: CollectionRepository = Depends(),
):
    return repo.create_collection(collection)


@router.get("/collections/{collection_id}", response_model=CollectionOut, tags=["collections"])
def get_collection(
    collection_id: str,
    repo: CollectionRepository = Depends()
):
    return repo.get_collection(collection_id)


@router.delete("/collections/{collection_id}", tags=["collections"])
def delete_collection(
    collection_id: str,
    repo: CollectionRepository = Depends()
):
    return repo.delete_collection(collection_id)


@router.put("/collections/{collection_id}", tags=["collections"])
def update_collection(
    collection_id: str,
    collection: CollectionIn,
    repo: CollectionRepository = Depends()
):
    return repo.update_collection(collection_id, collection)


@router.get("/collections", response_model=CollectionListOut, tags=["collections"])
def get_collections(
    repo: CollectionRepository = Depends(),
):
    return repo.get_list_of_collections()