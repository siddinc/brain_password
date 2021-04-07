from fastapi import APIRouter, status, Query, Path, Request, Body, File, UploadFile, HTTPException, Response
from typing import Optional, List, Dict
from pydantic import Field
from app.models.prediction import Prediction
from app.models.response import CustomResponse, DataResponse
from app.crud.prediction import get_user_prediction_data

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def get_user_prediction(
  request: Request,
  response: Response,
  eeg_file: UploadFile = File(...),
):
  try:
    user_prediction_scores = await get_user_prediction_data(request, eeg_file)
    return CustomResponse(
      status_code=status.HTTP_200_OK,
      message="User recognized successfully",
      data=user_prediction_scores,
    )

  except HTTPException as e:
    response.status_code = e.status_code
    return CustomResponse(status_code=e.status_code, message=e.detail)