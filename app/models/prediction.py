from pydantic import BaseModel, Field
from typing import Optional, List


class Prediction(BaseModel):
  query_recording: List[List[float]] = Field(...)