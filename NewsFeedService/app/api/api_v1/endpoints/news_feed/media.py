from typing import Optional
from fastapi import APIRouter, Body, Depends, Path, Query
from .....db.mongodb import AsyncIOMotorClient,get_database
from fastapi.encoders import jsonable_encoder
from .....crud.crud_media import *
from .....model.media import media 
router = APIRouter()



@router.put("/add_media/{post_id}",tags=["Post Media"])
async def add_media(post_id:str,media_data:media,db: AsyncIOMotorClient = Depends(get_database)):
    data=await post_media_db(db,post_id,jsonable_encoder(media_data),"$push")
    if (data):
        return {"status_code":200,"message":"Success","Extra_message":"Media Added Successfully"}
    else:
        return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
        

        

@router.delete("/delete_media/{post_id}",tags=["Post Media"])
async def delete_media(post_id:str,media_data:media,db: AsyncIOMotorClient = Depends(get_database)):
    data=await post_media_db(db,post_id,jsonable_encoder(media_data),"$pull")
    if (data):
        return {"status_code":200,"message":"Success","Extra_message":"Media Removed Successfully"}
    else:
        return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}