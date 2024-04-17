import pymongo
import os
from fastapi import HTTPException, Depends
from bson.objectid import ObjectId
from pydantic import BaseModel
from typing import List
from queries.collections import CollectionRepository


client = pymongo.MongoClient(os.environ.get("DATABASE_URL"))
db = client.collections_db


class DataStructureException(ValueError):
    pass


class InvalidCollectionIdException(ValueError):
    pass


class RequiredFieldException(ValueError):
    pass


class Field(BaseModel):
    name: str
    val: str


class ItemIn(BaseModel):
    name: str
    fields: List[Field]


class ItemOut(ItemIn):
    id: str
    collection_id: str


class ItemListOut(BaseModel):
    items: List[ItemOut]


class ItemsRepository:
    def __init__(self, collections_repo: CollectionRepository = Depends()):
        self.collections_repo = collections_repo

    def check_fields(self, item: ItemIn, collection_id: str):
        try:
            collection = self.collections_repo.get_collection(
                collection_id=collection_id
            )
        except:
            raise InvalidCollectionIdException()
        collection_field_names = [field.name for field in collection.fields]
        collection_required_fields = [
            field.name for field in collection.fields if field.required == True
        ]
        item_field_names = [field.name for field in item.fields]
        for field in item_field_names:
            if field not in collection_field_names:
                raise DataStructureException()
        for field in collection_required_fields:
            if field not in item_field_names:
                raise RequiredFieldException()

    def create_item(self, collection_id: str, item: ItemIn) -> ItemOut:
        self.check_fields(item=item, collection_id=collection_id)
        new_item = {
            "name": item.name,
            "fields": [field.dict() for field in item.fields],
            "collection_id": collection_id,
        }
        db.items.insert_one(new_item)
        new_item["id"] = str(new_item["_id"])
        return ItemOut(**new_item)

    def get_item(self, item_id: str) -> ItemOut:
        try:
            item = db.items.find_one({"_id": ObjectId(item_id)})
            item["id"] = str(item["_id"])
            return ItemOut(**item)
        except:
            raise HTTPException(status_code=404, detail="invalid item_id")

    def delete_item(self, item_id: str):
        try:
            result = db.items.delete_one({"_id": ObjectId(item_id)})
            if result.deleted_count > 0:
                return {"message": "Successfully deleted"}
        except:
            raise HTTPException(status_code=404, detail="invalid item_id")

    def update_item(self, item_id: str, item: ItemIn, collection_id: str):
        self.check_fields(item=item, collection_id=collection_id)
        try:
            updated_item = {
                "name": item.name,
                "fields": [field.dict() for field in item.fields],
            }
            result = db.items.update_one(
                {"_id": ObjectId(item_id)}, {"$set": updated_item}
            )
            return self.get_item(item_id)
        except:
            raise HTTPException(status_code=404, detail="invalid item_id")

    def get_list_of_items(self, collection_id) -> ItemListOut:
        items = []
        db_cursor = db.items.find({"collection_id": collection_id})
        for item in db_cursor:
            item["id"] = str(item["_id"])
            items.append(item)
        return ItemListOut(items=items)
