import pymongo
import os
from bson.objectid import ObjectId
from pydantic import BaseModel, create_model
from typing import List


client = pymongo.MongoClient(os.environ.get('DATABASE_URL'))
db = client.collections_db


class ItemIn(BaseModel):
    data: dict


class ItemOut(BaseModel):
    id: str
    collection_id: str
    data: dict


class ItemListOut(BaseModel):
    items: List[ItemOut]


class ItemsRepository:
    def create_item(self, collection_id: str, item: ItemIn) -> ItemOut:
        new_item_data = {}
        new_item_data["collection_id"] = collection_id
        new_item_data["data"] = item.data
        new_item_id = db.items.insert_one(new_item_data).inserted_id
        new_item = db.items.find_one({"_id": new_item_id})
        new_item["id"] = str(new_item["_id"])
        return new_item


    def get_item(self, item_id: str) -> ItemOut:
        item = db.items.find_one({"_id": ObjectId(item_id)})
        item["id"] = str(item["_id"])
        return item


    def delete_item(self, item_id: str):
        result = db.items.delete_one({"_id": ObjectId(item_id)})
        if result.deleted_count > 0:
            return {"message": "Successfully deleted"}


    def update_item(self, item_id: str, item: ItemIn):
        updated_item = {}
        updated_item["data"] = item.data
        result = db.items.update_one({"_id": ObjectId(item_id)}, {"$set": updated_item})
        if result.modified_count > 0:
            return {"message": "Successfully updated"}
        elif result.matched_count > 0:
            return {"message": "No changes made to existing item"}


    def get_list_of_items(self, collection_id) -> ItemListOut:
        items = []
        db_cursor = db.items.find({"collection_id": collection_id})
        for item in db_cursor:
            item["id"] = str(item["_id"])
            items.append(item)
        return {'items': items}