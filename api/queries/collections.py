import pymongo
import os
from fastapi import HTTPException
from bson.objectid import ObjectId
from pydantic import BaseModel
from typing import List


client = pymongo.MongoClient(os.environ.get("DATABASE_URL"))
db = client.collections_db


class Field(BaseModel):
    name: str
    data_type: str
    required: bool


class CollectionIn(BaseModel):
    name: str
    fields: List[Field]


class CollectionUpdate(BaseModel):
    name: str
    fields: List[Field]


class CollectionOut(CollectionIn):
    owner: str
    id: str


class CollectionListOut(BaseModel):
    collections: List[CollectionOut]


class CollectionRepository:
    def create_collection(self, owner, collection: CollectionIn) -> CollectionOut:
        new_collection = {
            "name": collection.name,
            "owner": owner,
            "fields": [field.dict() for field in collection.fields],
        }
        if db.collections.find_one({"name": collection.name, "owner": owner}):
            raise HTTPException(status_code=403, detail="collection name in use")
        db.collections.insert_one(new_collection)
        new_collection["id"] = str(new_collection["_id"])
        return CollectionOut(**new_collection)

    def get_collection(self, collection_id: str) -> CollectionOut:
        try:
            result = db.collections.find_one({"_id": ObjectId(collection_id)})
            result["id"] = collection_id
            return CollectionOut(**result)
        except:
            raise HTTPException(status_code=404, detail="invalid collection_id")

    def delete_collection(self, current_user: str, collection_id: str):
        try:
            collection = db.collections.find_one({"_id": ObjectId(collection_id)})
        except:
            raise HTTPException(status_code=404, detail="invalid collection_id")
        if collection["owner"] != current_user:
            raise HTTPException(
                status_code=401, detail="not authorized to delete specified collection"
            )
        deleted_items = db.items.delete_many({"collection_id": collection_id})
        result = db.collections.delete_one({"_id": ObjectId(collection_id)})
        if result.deleted_count > 0:
            return {"message": "collection deleted"}

    def update_collection(
        self, current_user: str, collection_id: str, collection_update: CollectionUpdate
    ) -> CollectionOut:
        try:
            collection = db.collections.find_one({"_id": ObjectId(collection_id)})
        except:
            raise HTTPException(status_code=404, detail="invalid collection_id")
        if collection["owner"] != current_user:
            raise HTTPException(
                status_code=401, detail="not authorized to update specified collection"
            )
        collection_update = {
            "name": collection_update.name,
            "owner": collection["owner"],
            "fields": [field.dict() for field in collection_update.fields],
        }
        result = db.collections.update_one(
            {"_id": ObjectId(collection_id)}, {"$set": collection_update}
        )
        return self.get_collection(collection_id)

    def get_list_of_collections_by_owner(self, username) -> CollectionListOut:
        collections = []
        db_cursor = db.collections.find({"owner": username})
        for collection in db_cursor:
            collection["id"] = str(collection["_id"])
            collections.append(collection)
        return CollectionListOut(collections=collections)
