from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,Field
from datetime import datetime, time, timedelta
from .user import User 


class replies(BaseModel):
    isLiked:bool
    user:User
    comment:str
    createdAt:datetime
    
class comment(BaseModel):
    isLiked:bool
    user:User
    comment:str
    createdAt:datetime
    replies:list=[]
    
class comment_delete_model(BaseModel):
    id:str
    
class comment_reply_delete_model(BaseModel):
    id:str