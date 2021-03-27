from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class Response(BaseModel):
  code: int = Field(..., ge=100, le=599)
  message: str = Field(...)
  data: Optional[dict] = None
  error: Optional[str] = None