from fastapi import APIRouter, status, Query, Path, Request, Body
from typing import Optional, List, Dict
from pydantic import Field
from uuid import UUID
from app.models.user import User, UserInDB


router = APIRouter()


@router.get("/get_user/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(
  request: Request,
  user_id: UUID = Path(...),
):
  pass


@router.get("/get_users", status_code=status.HTTP_200_OK)
async def get_users(
  request: Request,
):
  print(request.app.db)
  return {"mewo": "helo"}


@router.post("/register_user", status_code=status.HTTP_201_CREATED)
async def register_user(
  request: Request,
  user: User = Body(..., embed=True),
):
  pass


@router.put("/update_user/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(
  request: Request,
  user_id: UUID = Path(...),
  user: User = Body(..., embed=True),
):
  pass


@router.delete("/remove_user/{user_id}", status_code=status.HTTP_200_OK)
async def remove_user(
  request: Request,
  user_id: UUID = Path(...),
):
  pass