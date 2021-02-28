from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID

class media(BaseModel):
    id:UUID
    media_type:str
    url:str