from ..core.config import database_name, newsfeed_collection



async def tag_untag_db(db,post_id,user_data,op):
    try:
        await db[database_name][newsfeed_collection].update_one({"id":post_id},{op:{"taggedCoWorkers":user_data}})
        return True
    except:
        return False
    


