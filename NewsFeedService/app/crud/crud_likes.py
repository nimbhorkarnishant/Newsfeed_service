from ..core.config import database_name, newsfeed_collection



async def add_like_db(db,post_id,user_data,counter,op):
    try:
        await db[database_name][newsfeed_collection].update_one({"id":post_id},{"$inc":{"totallikes":counter},op:{"likes":user_data}})
        return True
    except:
        return False
    


