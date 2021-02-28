from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID
from datetime import datetime, time, timedelta

class replies(BaseModel):
    commentId:str
    isLiked:bool
    user:dict={}
    comment:str
    createdAt:datetime
    
class comment(BaseModel):
    commentId:UUID
    isLiked:bool
    user:dict={}
    comment:str
    createdAt:datetime
    replies:list=[]
    