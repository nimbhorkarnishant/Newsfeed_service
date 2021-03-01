from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID

class group(BaseModel):
    id:str
    name:str
    profile:str
    
