from typing import Optional
from fastapi import APIRouter, Body, Depends, Path, Query
from .....db.mongodb import AsyncIOMotorClient,get_database
from fastapi.encoders import jsonable_encoder
from .....crud.crud_media import *
from .....model.media import * 
import uuid
from typing import List
router = APIRouter()


def generate_uuid():
    _id=uuid.uuid4()
    return str(_id)

@router.put("/add_media/{post_id}",tags=["Post Media"])
async def add_media(post_id:str,media_data:multiple_media,db: AsyncIOMotorClient = Depends(get_database)):
    try:
        json_data = jsonable_encoder(media_data.media)
        for i in range(len(json_data)):
            json_data[i]['id']=generate_uuid()
        data=await post_media_db(db,post_id,json_data,"$push")
        if (data):
            return {"status_code":200,"message":"Success","Extra_message":"Media Added Successfully"}
        else:
            return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
    except:
        return {"status_code":500,"message":"Error","Extra_message":"Internal API Level Isuues"}


        

@router.delete("/delete_media/{post_id}",tags=["Post Media"])
async def delete_media(post_id:str,media_data:delete_media_model,db: AsyncIOMotorClient = Depends(get_database)):
    try:
        data=await post_media_db_delete(db,post_id,jsonable_encoder(media_data),"$pull")
        if (data):
            return {"status_code":200,"message":"Success","Extra_message":"Media Removed Successfully"}
        else:
            return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
    except:
        return {"status_code":500,"message":"Error","Extra_message":"Internal API Level Isuues"}