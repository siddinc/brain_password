from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from uuid import UUID


class EEGRecordings(BaseModel):
  eeg_recording_1: Optional[List[List[float]]] = None
  eeg_recording_2: Optional[List[List[float]]] = None
  eeg_recording_3: Optional[List[List[float]]] = None
  eeg_recording_4: Optional[List[List[float]]] = None
  eeg_recording_5: Optional[List[List[float]]] = None
  eeg_recording_6: Optional[List[List[float]]] = None


class EEGRecordingsInDB(EEGRecordings):
  user_id: UUID = Field(...)