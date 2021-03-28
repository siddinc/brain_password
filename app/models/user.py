from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List, Dict
from uuid import UUID


class User(BaseModel):
  f_name: str = Field(None)
  l_name: str = Field(None)
  email: EmailStr = Field(...)
  profile_photo: Optional[HttpUrl] = Field(None)


class UserInDB(User):
  user_id: UUID = Field(...)


class UserInUpdate(BaseModel):
  f_name: Optional[str] = Field(None)
  l_name: Optional[str] = Field(None)
  profile_photo: Optional[HttpUrl] = Field(None)