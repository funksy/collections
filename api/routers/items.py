from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from queries.items import (
    ItemsRepository,
    ItemIn,
    ItemOut,
    ItemListOut,
    DataStructureException,
    InvalidCollectionIdException,
    RequiredFieldException,
)


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post(
    "/collections/{collection_id}/items", response_model=ItemOut, tags=["items"]
)
def create_item(
    collection_id: str,
    data: ItemIn,
    repo: ItemsRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    try:
        return repo.create_item(collection_id, data)
    except InvalidCollectionIdException:
        raise HTTPException(status_code=404, detail="invalid collection_id")
    except DataStructureException:
        raise HTTPException(status_code=404, detail="invalid data structure")
    except RequiredFieldException:
        raise HTTPException(status_code=404, detail="required field violation")


@router.get(
    "/collections/{collection_id}/items/{item_id}",
    response_model=ItemOut,
    tags=["items"],
)
def get_item(
    item_id: str,
    repo: ItemsRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.get_item(item_id)


@router.delete("/collections/{collection_id}/items/{item_id}", tags=["items"])
def delete_item(
    item_id: str,
    repo: ItemsRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.delete_item(item_id)


@router.put("/collections/{collection_id}/items/{item_id}", tags=["items"])
def update_item(
    item_id: str,
    item: ItemIn,
    collection_id: str,
    repo: ItemsRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.update_item(item_id, item)


@router.get(
    "/collections/{collection_id}/items", response_model=ItemListOut, tags=["items"]
)
def get_list_of_items(
    collection_id: str,
    repo: ItemsRepository = Depends(),
    token: str = Depends(oauth2_scheme),
):
    return repo.get_list_of_items(collection_id)
