from fastapi import APIRouter, status, Query, Path, Request, Body
from typing import Optional, List, Dict
from pydantic import Field
from uuid import UUID
from app.models.eeg_recordings import EEGRecordings, EEGRecordingsInDB


router = APIRouter()


@router.get("/get_eeg_recordings/{user_id}", status_code=status.HTTP_200_OK)
async def get_eeg_recordings(
  request: Request,
  user_id: UUID = Path(...),
):
  pass


@router.post("/register_eeg_recordings/{user_id}", status_code=status.HTTP_201_CREATED)
async def register_eeg_recordings(
  request: Request,
  user_id: UUID = Path(...),
  eeg: EEGRecordings = Body(..., embed=True),
):
  pass


@router.put("/update_eeg_recordings/{user_id}", status_code=status.HTTP_200_OK)
async def update_eeg_recordings(
  request: Request,
  user_id: UUID = Path(...),
  eeg: EEGRecordings = Body(..., embed=True),
):
  pass


@router.delete("/remove_eeg_recordings/{user_id}", status_code=status.HTTP_200_OK)
async def remove_eeg_recordings(
  request: Request,
  user_id: UUID = Path(...),
):
  pass