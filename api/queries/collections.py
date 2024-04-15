import pymongo
import os
from bson.objectid import ObjectId
from pydantic import BaseModel, create_model
from typing import List


client = pymongo.MongoClient(os.environ.get('DATABASE_URL'))
db = client.collections_db


class CollectionIn(BaseModel):
    name: str
    fields: dict


class CollectionOut(CollectionIn):
    id: str


class CollectionListOut(BaseModel):
    collections: List[CollectionOut]


class CollectionRepository:
    def create_collection(self, collection: CollectionIn) -> CollectionOut:
        new_collection = {
            "name": collection.name,
            "fields": collection.fields
        }
        db.collections.insert_one(new_collection)
        new_collection["id"] = str(new_collection["_id"])
        return new_collection


    def get_collection(self, collection_id: str) -> CollectionOut:
        result = db.collections.find_one({"_id": ObjectId(collection_id)})
        result["id"] = collection_id
        return result


    def delete_collection(self, collection_id: str):
        result = db.collections.delete_one({"_id": ObjectId(collection_id)})
        if result.deleted_count > 0:
            return {"message": "Successfully deleted"}


    # TODO need to update to check what changes are present if any
    def update_collection(self, collection_id: str, collection: CollectionIn):
        result = db.collections.update_one({"_id": ObjectId(collection_id)}, {"$set": collection.dict()})
        if result.modified_count > 0:
            return {"message": "Successfully updated"}
        elif result.matched_count > 0:
            return {"message": "No changes made to existing collection"}


    def get_list_of_collections(self) -> CollectionListOut:
        collections = []
        db_cursor = db.collections.find()
        for collection in db_cursor:
            collection["id"] = str(collection["_id"])
            collections.append(collection)
        return {'collections': collections}