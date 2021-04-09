from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from motor.motor_asyncio import AsyncIOMotorClient
from app.api.api import router as api_router
from app.core.configuration import settings
from app.core.utils import load_network
import os


app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
  app.db_client = AsyncIOMotorClient(settings.db_url, uuidRepresentation="standard")
  app.db = app.db_client[settings.db_name]
  print("INFO:     Connected to Database")


@app.on_event("shutdown")
async def shutdown_db_client():
  app.db_client.close()
  print("INFO:     Disconnected from Database")


app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
  allow_headers=["*"],
)


app.include_router(api_router, prefix="/api")


@app.get("/", tags=["Root"], status_code=status.HTTP_200_OK)
async def root():
  return {"message": "Brain Password Backend"}


@app.get("*", tags=["404 Not found"], status_code=status.HTTP_404_NOT_FOUND)
async def not_found():
  return {"message": "Requested resource not found"}