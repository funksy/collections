from fastapi import FastAPI
from routers import collections, items

app = FastAPI()

app.include_router(collections.router)
app.include_router(items.router)