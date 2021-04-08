from fastapi import APIRouter, status, Query, Path, Request, Body, File, UploadFile, HTTPException, Response
from typing import Optional, List, Dict
from pydantic import Field
import numpy as np
from app.models.prediction import Prediction
from app.models.response import CustomResponse, DataResponse
from app.core.configuration import settings
from time import time

router = APIRouter()

async def retrieve_all_eeg_recordings_data(request: Request) -> list:
  all_eeg_recordings = []
  async for eeg_recordings in request.app.db[settings.eeg_recordings_collection].find(projection={"_id": False}):
    all_eeg_recordings.append(eeg_recordings)

  if len(all_eeg_recordings) == 0:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EEG Recordings for the users not found")
  return all_eeg_recordings


@router.post("/", status_code=status.HTTP_200_OK)
async def get_user_prediction(
  request: Request,
  response: Response,
  eeg_file: UploadFile = File(...),
):
  start = time()
  all_eeg_recordings = await retrieve_all_eeg_recordings_data(request)
  # print(all_eeg_recordings[0].keys())
  end = time()
  return {"done": end - start}
