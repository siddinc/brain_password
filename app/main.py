from fastapi import FastAPI, Request, status
from motor.motor_asyncio import AsyncIOMotorClient
from app.api.api import router as api_router
from app.core.configuration import db_url, db_name
# from app.core.utils import load_network
import os


# network = load_network("../networks/model-c_63-vl_0.0134.h5")
# network.summary()

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
  app.db_client = AsyncIOMotorClient(db_url, uuidRepresentation="standard")
  app.db = app.db_client[db_name]


@app.on_event("shutdown")
async def shutdown_db_client():
  app.db_client.close()


app.include_router(api_router, prefix="/api")


@app.get("/", tags=["Root"], status_code=status.HTTP_200_OK)
async def root():
  return {"message": "hello world"}


@app.get("*", tags=["404 Not found"], status_code=status.HTTP_404_NOT_FOUND)
async def not_found():
  return {"message": "Resource not found"}