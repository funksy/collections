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


class CollectionOut(CollectionIn):
    id: str


class CollectionListOut(BaseModel):
    collections: List[CollectionOut]


class CollectionRepository:
    def create_collection(self, collection: CollectionIn) -> CollectionOut:
        new_collection = {
            "name": collection.name,
            "fields": [field.dict() for field in collection.fields],
        }
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

    def delete_collection(self, collection_id: str):
        try:
            result = db.collections.delete_one({"_id": ObjectId(collection_id)})
            if result.deleted_count > 0:
                return {"message": "collection deleted"}
        except:
            raise HTTPException(status_code=404, detail="invalid collection_id")

    def update_collection(
        self, collection_id: str, collection: CollectionIn
    ) -> CollectionOut:
        try:
            result = db.collections.update_one(
                {"_id": ObjectId(collection_id)}, {"$set": collection.dict()}
            )
            return self.get_collection(collection_id)
        except:
            raise HTTPException(status_code=404, detail="invalid collection_id")

    def get_list_of_collections(self) -> CollectionListOut:
        collections = []
        db_cursor = db.collections.find()
        for collection in db_cursor:
            collection["id"] = str(collection["_id"])
            collections.append(collection)
        return CollectionListOut(collections=collections)
