import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import collections, items, users
from tags import tags_metadata

app = FastAPI(
    title="Collections",
    description="A place to track and share things you collect",
    contact={
        "name": "John Lukich",
        "url": "http://john-lukich.mooo.com",
    },
    openapi_tags=tags_metadata,
)

app.include_router(collections.router)
app.include_router(items.router)
app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
