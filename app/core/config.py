from decouple import config
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient


debug_mode = config("DEBUG_MODE", cast=bool)
host = config("HOST", cast=str)
db_url = config("DB_URL", cast=str)
db_name = config("DB_NAME", cast=str)

host = config("HOST", cast=str)
port = config("PORT", cast=int)
user_collection = config("USER_COLLECTION_NAME", cast=str)
recordings_collection = config("RECORDINGS_COLLECTION_NAME", cast=str)

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
  app.db_client = AsyncIOMotorClient(db_url)
  app.db = app.db_client[db_name]


@app.on_event("shutdown")
async def shutdown_db_client():
  app.db_client.close()