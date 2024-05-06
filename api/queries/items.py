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
    val: str | int | bool


class ItemIn(BaseModel):
    name: str
    fields: List[Field]


class ItemUpdate(BaseModel):
    fields: List[Field]


class ItemOut(ItemIn):
    id: str
    owner: str
    collection_id: str


class ItemListOut(BaseModel):
    items: List[ItemOut]


class ItemsRepository:
    def __init__(self, collections_repo: CollectionRepository = Depends()):
        self.collections_repo = collections_repo

    def field_decoder(self, field):
        match field.data_type:
            case 'str':
                return str
            case 'int':
                return int
            case 'bool':
                return bool
    
    def check_fields(self, item: ItemIn, collection_id: str):
        try:
            collection = self.collections_repo.get_collection(
                collection_id=collection_id
            )
        except:
            raise HTTPException(
                status_code=403, detail="invalid collection_id provided"
            )
        
        collection_field_names, collection_field_data_types = [], []
        for field in collection.fields:
            collection_field_names.append(field.name)
            collection_field_data_types.append((self.field_decoder(field)))
        collection_required_fields = [
            field.name for field in collection.fields if field.required == True
        ]
        
        item_field_names, item_field_data_types = [], []
        for field in item.fields:
            item_field_names.append(field.name)
            item_field_data_types.append(type(field.val))

        if collection_field_names != item_field_names:
            name_mismatch = True
        else:
            name_mismatch = False

        if collection_field_data_types != item_field_data_types:
            data_type_mismatch = True
        else:
            data_type_mismatch = False
        
        if name_mismatch or data_type_mismatch:
            raise HTTPException(status_code=403, detail="invalid data structure")
        for field in collection_required_fields:
            if field not in item_field_names:
                raise HTTPException(status_code=403, detail="required field incomplete")

    def create_item(self, owner: str, collection_id: str, item: ItemIn) -> ItemOut:
        self.check_fields(item=item, collection_id=collection_id)
        new_item = {
            "name": item.name,
            "owner": owner,
            "fields": [field.dict() for field in item.fields],
            "collection_id": collection_id,
        }
        if db.items.find_one({"name": item.name, "owner": owner}):
            raise HTTPException(status_code=403, detail="item name in use")
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

    def delete_item(self, current_user: str, item_id: str):
        try:
            item = db.items.find_one({"_id": ObjectId(item_id)})
        except:
            raise HTTPException(status_code=404, detail="invalid item_id")
        if item["owner"] != current_user:
            raise HTTPException(
                status_code=401, detail="not authorized to delete specified item"
            )
        result = db.items.delete_one({"_id": ObjectId(item_id)})
        if result.deleted_count > 0:
            return {"message": "Successfully deleted"}

    def update_item(self, current_user: str, item_id: str, item_update: ItemUpdate):
        try:
            item = db.items.find_one({"_id": ObjectId(item_id)})
        except:
            raise HTTPException(status_code=404, detail="invalid item_id")
        if item["owner"] != current_user:
            raise HTTPException(
                status_code=401, detail="not authorized to update specified item"
            )
        item_update = {
            "name": item["name"],
            "owner": item["owner"],
            "collection_id": item["collection_id"],
            "fields": [field.dict() for field in item_update.fields],
        }
        self.check_fields(
            item=ItemIn(**item_update), collection_id=item["collection_id"]
        )
        result = db.items.update_one({"_id": ObjectId(item_id)}, {"$set": item_update})
        return self.get_item(item_id)

    def get_list_of_items(self, collection_id) -> ItemListOut:
        items = []
        db_cursor = db.items.find({"collection_id": collection_id})
        for item in db_cursor:
            item["id"] = str(item["_id"])
            items.append(item)
        return ItemListOut(items=items)
