from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID

class User(BaseModel):    
    id:str
    profileImg: str
    firstName: str
    lastName:str