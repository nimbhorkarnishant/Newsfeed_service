from ..core.config import database_name, newsfeed_collection



async def post_media_db(db,post_id,media_data,op):
    try:
        await db[database_name][newsfeed_collection].update_one({"id":post_id},{op:{"media":media_data}})
        return True
    except:
        return False
    
