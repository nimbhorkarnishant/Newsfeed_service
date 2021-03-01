from typing import Optional,List
from fastapi import FastAPI
from pydantic import BaseModel,Field

class User(BaseModel):    
    id:str
    profileImg: str
    firstName: str
    lastName:str
    
class delete_user_model(BaseModel):
    id:str
    
class tag_coworker_post_model(BaseModel):
    taggedCoWorkers:List[User]