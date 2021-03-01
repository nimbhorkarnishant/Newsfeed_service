from typing import Optional,List
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID

class media(BaseModel):
    media_type:str
    url:str
    
class delete_media_model(BaseModel):
    id:str
    
class multiple_media(BaseModel):
    media:List[media]