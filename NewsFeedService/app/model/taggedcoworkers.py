from typing import Optional,List
from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID


class taggedCoWorkers(BaseModel):
    id:str
    firstname:str
    lastname:str
    profile:str
    
