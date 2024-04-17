from fastapi import FastAPI
from routers import collections, items, users

app = FastAPI()

app.include_router(collections.router)
app.include_router(items.router)
app.include_router(users.router)
