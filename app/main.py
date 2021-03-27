from fastapi import FastAPI, Request
from app.api.api import router as api_router


app = FastAPI()

app.include_router(api_router, prefix="/api")


@app.get("/")
async def root(request: Request):
  print(request.app.db)
  return {"message": "hello world"}