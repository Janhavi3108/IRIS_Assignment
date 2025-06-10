from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="IRIS Excel API",
    description="A FastAPI application to read and process Excel sheets.",
    version="1.0"
)

app.include_router(router)
