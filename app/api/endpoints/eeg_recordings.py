from fastapi import APIRouter, status, Query, Path, Request, Response, Body, HTTPException, File, UploadFile
from typing import Optional, List, Dict
from pydantic import Field
from pymongo import ReturnDocument
from uuid import UUID, uuid4
from app.models.response import CustomResponse, DataResponse
from app.models.eeg_recordings import EEGRecordings, EEGRecordingsInDB
from app.crud.eeg_recordings import (
  retrieve_all_eeg_recordings_data,
  retrieve_eeg_recordings_data,
  create_eeg_recordings_data,
  update_eeg_recordings_data,
  delete_eeg_recordings_data,
)


router = APIRouter()


@router.get("/get_eeg_recordings/{user_id}", status_code=status.HTTP_200_OK)
async def retrieve_eeg_recordings(
  request: Request,
  response: Response,
  user_id: UUID = Path(...),
):
  try:
    eeg_recordings = await retrieve_eeg_recordings_data(request, user_id)
    return DataResponse(
      status_code=status.HTTP_200_OK,
      message="EEG recordings for the user retrieved successfully",
      data=eeg_recordings,
    )

  except HTTPException as e:
    response.status_code = e.status_code
    return CustomResponse(status_code=e.status_code, message=e.detail)


@router.get("/get_all_eeg_recordings", status_code=status.HTTP_200_OK)
async def retrieve_all_eeg_recordings(request: Request, response: Response,):
  try:
    all_eeg_recordings = await retrieve_all_eeg_recordings_data(request)
    return DataResponse(
      status_code=status.HTTP_200_OK,
      message="EEG Recordings for all users retrieved successfully",
      data=all_eeg_recordings,
    )

  except HTTPException as e:
    response.status_code = e.status_code
    return CustomResponse(status_code=e.status_code, message=e.detail)


@router.post("/register_eeg_recordings/{user_id}", status_code=status.HTTP_201_CREATED)
async def create_eeg_recordings(
  request: Request,
  response: Response,
  user_id: UUID = Path(...),
  eeg_files: List[UploadFile] = File(...),
):
  try:
    new_eeg_recordings = await create_eeg_recordings_data(request, user_id, eeg_files)
    return CustomResponse(
      status_code=status.HTTP_201_CREATED,
      message="EEG Recordings for the user created successfully"
    )

  except HTTPException as e:
    response.status_code = e.status_code
    return CustomResponse(status_code=e.status_code, message=e.detail)


@router.put("/update_eeg_recordings/{user_id}", status_code=status.HTTP_200_OK)
async def update_eeg_recordings(
  request: Request,
  response: Response,
  user_id: UUID = Path(...),
  eeg: EEGRecordings = Body(..., embed=True),
):
  try:
    updated_eeg_recordings = await update_eeg_recordings_data(request, user_id, eeg)
    return DataResponse(
      status_code=status.HTTP_200_OK,
      message="EEG Recordings for the user updated successfully",
      data=updated_eeg_recordings,
    )

  except HTTPException as e:
    response.status_code = e.status_code
    return CustomResponse(status_code=e.status_code, message=e.detail)


@router.delete("/remove_eeg_recordings/{user_id}", status_code=status.HTTP_200_OK)
async def delete_eeg_recordings(
  request: Request,
  response: Response,
  user_id: UUID = Path(...),
):
  try:
    deleted_eeg_recordings = await delete_eeg_recordings_data(request, user_id)
    return DataResponse(
      status_code=status.HTTP_200_OK,
      message="EEG Recodings for the user deleted successfully",
      data={"user_id": deleted_eeg_recordings["user_id"]},
    )

  except HTTPException as e:
    response.status_code = e.status_code
    return CustomResponse(status_code=e.status_code, message=e.detail)