from pydantic import BaseModel, Field, EmailStr, HttpUrl
from typing import Optional, List, Dict
from uuid import UUID


class User(BaseModel):
  f_name: str = Field("John")
  l_name: str = Field("Doe")
  email: EmailStr = Field(...)
  profile_photo: Optional[HttpUrl] = Field(None)


class UserInDB(User):
  user_id: UUID = Field(...)