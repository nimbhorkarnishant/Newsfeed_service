from typing import Optional
from fastapi import APIRouter, Body, Depends, Path, Query
from .....model.news_feed import News_Feed,Response_News_Feed,Update_News_Feed
from .....core.config import database_name, newsfeed_collection
from .....db.mongodb import AsyncIOMotorClient,get_database
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import PaginationParams, Page
from fastapi_pagination.paginator import paginate
from .....crud.crud_news_feed import *

router = APIRouter()



# @router.get("/testing",tags=["Post"])
# async def test_api():
#     return {"Testing":"Done"}


@router.post("/news_posts",tags=["Post"])
async def News_Feed(post_data:News_Feed,db: AsyncIOMotorClient = Depends(get_database)):
    json_data = jsonable_encoder(post_data)
    data=await post_db(db,json_data)
    if data:
        return {"status_code":200,"message":"Success","Extra_message":"Post Added Successfully","post_id":post_data.id}
    else:
        return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}


@router.get("/get_news_posts",tags=["Post"])
async def Read_News_Feed(params: PaginationParams = Depends(),db: AsyncIOMotorClient = Depends(get_database)):
    posts=[]
    data=await read_db_sort_desc(db)
    if (data):
        async for document in data:
            posts.append(Response_News_Feed(**document))
        return {"status_code":200,"message":"Success","Extra_message":"Data Coming From DB","posts":paginate(posts,params)}
    else:
        return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}

@router.put("/update_news_post/{post_id}",tags=["Post"])
async def Update_News_Feed(post_id:str,post_data:Update_News_Feed,db: AsyncIOMotorClient = Depends(get_database)):
    data= await update_news_feed_db(db,post_id,jsonable_encoder(post_data))
    if (data):
        return {"status_code":200,"message":"Success","Extra_message":"Post Updated Successfully","post_id":post_id}
    else:
        return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}

@router.delete("/delete_news_post/{post_id}",tags=["Post"])
async def Delete_News_Feed(post_id:str,db: AsyncIOMotorClient = Depends(get_database)):
    data=await delete_news_feed_db(db,post_id)
    if (data):
        return {"status_code":200,"message":"Success","Extra_message":"Post Deleted Successfully"}
    else:
        return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}




