from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from uuid import UUID


class EEGRecordings(BaseModel):
  eeg_recordings: Dict[str, List[float]] = Field({
    "1": None,
    "2": None,
    "3": None,
    "4": None,
    "5": None,
    "6": None,
  })


class EEGRecordingsInDB(EEGRecordings):
  user_id: UUID = Field(...)