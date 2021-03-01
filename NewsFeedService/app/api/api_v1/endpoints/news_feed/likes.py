from typing import Optional
from fastapi import APIRouter, Body, Depends, Path, Query
from .....db.mongodb import AsyncIOMotorClient,get_database
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import PaginationParams, Page
from fastapi_pagination.paginator import paginate
from .....crud.crud_likes import *
from .....model.user import *

router = APIRouter()


# @router.get("/testing_like",tags=["Post Likes"])
# async def test_api():
#     return {"Testing":"Done"}



@router.put("/like/{post_id}",tags=["Post Likes"])
async def Like(post_id:str,user_data:User,db: AsyncIOMotorClient = Depends(get_database)):
    try:
        data=await add_like_db(db,post_id,jsonable_encoder(user_data),1,"$push")
        if (data):
            return {"status_code":200,"message":"Success","Extra_message":"User Liked Successfully"}
        else:
            return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
    except:
        return {"status_code":500,"message":"Error","Extra_message":"Internal API Level Issues"}
        

        

@router.delete("/dislike/{post_id}",tags=["Post Likes"])
async def Dislike(post_id:str,user_data:delete_user_model,db: AsyncIOMotorClient = Depends(get_database)):
    try:
        data=await add_like_db(db,post_id,jsonable_encoder(user_data),-1,"$pull")
        if (data):
            return {"status_code":200,"message":"Success","Extra_message":"User Disliked Successfully"}
        else:
            return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
    except:
        return {"status_code":500,"message":"Error","Extra_message":"Internal API Level Issues"}