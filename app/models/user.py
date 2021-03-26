from pydantic import BaseModel, Field, EmailStr, UrlStr
from typing import Optional, List, Dict
from uuid import UUID


class User(BaseModel):
  user_id: UUID = Field(...)
  f_name: str = Field("John")
  l_name: str = Field("Doe")
  email: EmailStr = Field(...)
  profile_photo: Optional[Urlstr] = Field(None)


class UserInUpdate(BaseModel):
  f_name: str = Field("John")
  l_name: str = Field("Doe")
  email: EmailStr = Field(...)
  profile_photo: Optional[Urlstr] = Field(None)