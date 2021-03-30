from fastapi import APIRouter, status, Query, Path, Request, Body, File, UploadFile
from typing import Optional, List, Dict
from pydantic import Field
from app.models.prediction import Prediction


router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def get_user_prediction(
  request: Request,
  eeg: Prediction = Body(..., embed=True),
):
  pass