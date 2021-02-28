from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID
from datetime import datetime, time, timedelta
from bson import ObjectId
from .user import User
from .group import group
from .taggedcoworkers import taggedCoWorkers
from .media import media
from .comment import comment
from .group import group



class News_Feed(BaseModel):
    id:UUID
    user:User
    isLiked:Optional[bool]=False
    createdAt:datetime
    group:group 
    media:Optional[list]=[]
    description:Optional[str]
    taggedCoWorkers:Optional[list]=[]
    totalComments:Optional[int]=0
    likes:Optional[list]=[]
    totallikes:Optional[int]=0
    comments:Optional[list]=[]
    
class Response_News_Feed(BaseModel):
    id:UUID
    user:User
    isLiked:Optional[bool]=False
    createdAt:datetime
    group:group 
    media:Optional[list]=[]
    description:Optional[str]
    taggedCoWorkers:Optional[list]=[]
    totalComments:Optional[int]=0
    likes:Optional[list]=[]
    totallikes:Optional[int]=0
    comments:Optional[list]=[]



    
class Update_News_Feed(BaseModel):
    isLiked:Optional[bool]=False
    createdAt:datetime
    description:Optional[str]