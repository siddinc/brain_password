from fastapi import APIRouter, status, Query, Path, Request, Body, File, UploadFile, HTTPException, Response
from typing import Optional, List, Dict
from pydantic import Field
from app.models.prediction import Prediction
from app.crud.eeg_recordings import retrieve_all_eeg_recordings_data


router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def get_user_prediction(
  request: Request,
  response: Response,
  eeg_file: UploadFile = File(...),
):
  
  all_eeg_recordings = await retrieve_all_eeg_recordings_data(request)
  query_file = await eeg.read()
  decoded_file = list(map(lambda e: float(e), query_file.decode("utf-8").split(",")))
  print(decoded_file)  
    
