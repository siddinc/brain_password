from fastapi import APIRouter, status, Query, Path, Request, Body, HTTPException, UploadFile, File
from typing import Optional, List, Dict
from pydantic import Field
from uuid import UUID, uuid4
from app.models.prediction import Prediction
from app.core.configuration import settings
from app.core.utils import create_chunks
import csv


async def get_user_prediction_data():
  pass