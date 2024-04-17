import pymongo
import os
import jwt
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from bson.objectid import ObjectId
from pydantic import BaseModel
from typing import List

JWT_SECRET = os.environ.get("JWT_SECRET")

client = pymongo.MongoClient(os.environ.get("DATABASE_URL"))
db = client.collections_db


class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: str
    username: str


class UserRepository:
    def authenticate_user(self, username: str, password: str) -> bool | UserOut:
        user = db.users.find_one({"username": username})
        if not user:
            return False
        if not bcrypt.verify(password, user["password_hash"]):
            return False
        user["id"] = str(user["_id"])
        return UserOut(**user)

    def create_user(self, user: UserIn) -> UserOut:
        if db.users.find_one({"username": user.username}) or user.username == 'me':
            raise HTTPException(status_code=400, detail='cannot create an account with those credentials')
        new_user = {
            "username": user.username,
            "password_hash": bcrypt.hash(user.password),
        }
        db.users.insert_one(new_user)
        new_user["id"] = str(new_user["_id"])
        return UserOut(**new_user)

    def get_user(self, username: str) -> UserOut:
        try:
            user = db.users.find_one({"username": username})
            user["id"] = str(user["_id"])
            return UserOut(**user)
        except:
            raise HTTPException(status_code=404, detail="invalid credentials")

    def get_current_user(self, token: str):
        print('****************************', token)
        # try:
        #     payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        #     print('*******************************************', payload)
        #     user = self.get_user(payload.get('username'))
        #     user["id"] = str(user["_id"])
        # except:
        #     raise HTTPException(status_code=401, detail='unauthorized')
        # return UserOut(**user)
        return {'message': token}

    def generate_token(self, form_data: OAuth2PasswordRequestForm):
        user = self.authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=401, detail="invalid credentials")

        token = jwt.encode(user.dict(), JWT_SECRET)
        return {"access_token": token, "token_type": "bearer"}
