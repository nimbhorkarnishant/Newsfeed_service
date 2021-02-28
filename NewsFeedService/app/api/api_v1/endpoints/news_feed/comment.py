from typing import Optional
from fastapi import APIRouter, Body, Depends, Path, Query
from .....db.mongodb import AsyncIOMotorClient,get_database
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import PaginationParams, Page
from fastapi_pagination.paginator import paginate
from .....crud.crud_likes import *
from .....model.user import User

router = APIRouter()

@router.get("/testing_like",tags=["Post Comments"])
async def test_api():
    return {"Testing":"Done"}