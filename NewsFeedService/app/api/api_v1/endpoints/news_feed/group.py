from typing import Optional
from fastapi import APIRouter, Body, Depends, Path, Query
from .....db.mongodb import AsyncIOMotorClient,get_database
from fastapi.encoders import jsonable_encoder
from .....crud.crud_group import *
from .....model.group import group

router = APIRouter()




@router.put("/update_group/{post_id}",tags=["Group"])
async def Update_group(post_id:str,group_data:group,db: AsyncIOMotorClient = Depends(get_database)):
    try:
        data=await update_group_db(db,post_id,jsonable_encoder(group_data))
        if (data):
            return {"status_code":200,"message":"Success","Extra_message":"Group Updated Successfully"}
        else:
            return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
    except:
        return {"status_code":500,"message":"Error","Extra_message":"Internal API Level Issues"}
    
    
        
@router.delete("/delete_group/{post_id}",tags=["Group"])
async def Update_group(post_id:str,db: AsyncIOMotorClient = Depends(get_database)):
    try:
        data=await delete_group_db(db,post_id)
        if (data):
            return {"status_code":200,"message":"Success","Extra_message":"Group Deleted Successfully"}
        else:
            return {"status_code":400,"message":"Error","Extra_message":"DB Operation Issues"}
    except:
        return {"status_code":500,"message":"Error","Extra_message":"Internal API Level Issues"}
