from fastapi import APIRouter, Depends, Response
from queries.items import (
    ItemsRepository,
    ItemIn,
    ItemOut,
    ItemListOut,
)


router = APIRouter()


@router.post("/collections/{collection_id}/items", response_model=ItemOut, tags=["items"])
def create_item(
    collection_id: str,
    data: ItemIn,
    repo: ItemsRepository = Depends(),
):
    return repo.create_item(collection_id, data)


@router.get("/collections/{collection_id}/items/{item_id}", response_model=ItemOut, tags=["items"])
def get_item(
    item_id: str,
    repo: ItemsRepository = Depends()
):
    return repo.get_item(item_id)


@router.delete("/collections/{collection_id}/items/{item_id}", tags=["items"])
def delete_item(
    item_id: str,
    repo: ItemsRepository = Depends()
):
    return repo.delete_item(item_id)


@router.put("/collections/{collection_id}/items/{item_id}", tags=["items"])
def update_item(
    item_id: str,
    item: ItemIn,
    repo: ItemsRepository = Depends()
):
    return repo.update_item(item_id, item)


@router.get("/collections/{collection_id}/items", response_model=ItemListOut, tags=["items"])
def get_list_of_items(
    collection_id: str,
    repo: ItemsRepository = Depends()
):
    return repo.get_list_of_items(collection_id)