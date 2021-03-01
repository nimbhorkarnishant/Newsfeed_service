from typing import Optional
from fastapi import APIRouter, Body, Depends, Path, Query
from .....db.mongodb import AsyncIOMotorClient,get_database
from fastapi.encoders import jsonable_encoder
from fastapi_pagination import PaginationParams, Page
from fastapi_pagination.paginator import paginate
from .....crud.crud_comment import *
from .....model.user import User
from .....model.comment import *
import uuid

router = APIRouter()



@router.post("/add_comment/{post_id}",tags=["Post Comments"])
async def Add_Comment(post_id:str,comment_data:comment,db: AsyncIOMotorClient = Depends(get_database)):
    try:
        _id=uuid.uuid4()
        commentdata=jsonable_encoder(comment_data)
        commentdata['id']=str(_id)
        data=await post_comment_db(db,post_id,commentdata,1,"$push")
        if (data):
            return {"status_code":200,"message":"Success","Extra_message":"Comment Added Successfully"}
        else:
            return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
    except:
        return {"status_code":500,"message":"Error","Extra_message":"Internal API Level Issues"}


@router.delete("/delete_comment/{post_id}",tags=["Post Comments"])   
async def Delete_Comment(post_id:str,commentdata:comment_delete_model,db: AsyncIOMotorClient = Depends(get_database)):
    try:
        data=await post_comment_db(db,post_id,jsonable_encoder(commentdata),-1,"$pull")
        if (data):
            return {"status_code":200,"message":"Success","Extra_message":"Comment Delete Successfully"}
        else:
            return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
    except:
        return {"status_code":500,"message":"Error","Extra_message":"Internal API Level Issues"}
    

@router.post("/add_reply/{post_id}/{comment_id}",tags=["Post Comments"])
async def Add_comment_reaply(post_id:str,comment_id:str,reply_data:replies,db:AsyncIOMotorClient=Depends(get_database)):
    try:
        _id=uuid.uuid4()
        commentdata=jsonable_encoder(reply_data)
        commentdata['id']=str(_id)
        data=await comment_reply_db(db,post_id,comment_id,commentdata,"$push")
        if (data):
            return {"status_code":200,"message":"Success","Extra_message":"Comment Reply Added Successfully"}
        else:
            return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
    except:
        return {"status_code":500,"message":"Error","Extra_message":"Internal API Level Issues"}


@router.delete("/delete_reply/{post_id}/{comment_id}",tags=["Post Comments"])
async def Add_comment_reaply(post_id:str,comment_id:str,reply_data:comment_reply_delete_model,db:AsyncIOMotorClient=Depends(get_database)):
    try:
        commentdata=jsonable_encoder(reply_data)
        data=await comment_reply_db(db,post_id,comment_id,commentdata,"$pull")
        if (data):
            return {"status_code":200,"message":"Success","Extra_message":"Comment Reply deleted Successfully"}
        else:
            return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
    except:
        return {"status_code":500,"message":"Error","Extra_message":"Internal API Level Issues"}
    