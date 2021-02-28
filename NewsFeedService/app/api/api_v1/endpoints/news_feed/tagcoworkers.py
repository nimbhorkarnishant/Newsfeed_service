from typing import Optional
from fastapi import APIRouter, Body, Depends, Path, Query
from .....db.mongodb import AsyncIOMotorClient,get_database
from fastapi.encoders import jsonable_encoder
from .....crud.crud_tagcoworkers import *
from .....model.user import User
router = APIRouter()



@router.put("/tag_coworkers/{post_id}",tags=["Tag Coworkers"])
async def Tag(post_id:str,user_data:User,db: AsyncIOMotorClient = Depends(get_database)):
    data=await tag_untag_db(db,post_id,jsonable_encoder(user_data),"$push")
    if (data):
        return {"status_code":200,"message":"Success","Extra_message":"User Tagged Successfully"}
    else:
        return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
        

        

@router.delete("/untag_coworkers/{post_id}",tags=["Tag Coworkers"])
async def Untag(post_id:str,user_data:User,db: AsyncIOMotorClient = Depends(get_database)):
    data=await tag_untag_db(db,post_id,jsonable_encoder(user_data),"$pull")
    if (data):
        return {"status_code":200,"message":"Success","Extra_message":"User Untagged Successfully"}
    else:
        return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}