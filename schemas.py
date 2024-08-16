from datetime import datetime , date
from operator import le
from pydantic import BaseModel, EmailStr , conint
from typing import Optional
from pydantic.types import conlist

class ScreenerDataFetch(BaseModel):
  nsecode: str
  per_chg: float
  close: float
  # volume: float

class ScreenerData(BaseModel):
  conditionName: str