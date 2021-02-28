from ..core.config import database_name, newsfeed_collection



async def update_group_db(db,post_id,group_data):
    try:
        await db[database_name][newsfeed_collection].update_one({"id":post_id},{"$set":{"group":group_data}})
        return True
    except:
        return False
    

async def delete_group_db(db,post_id):
    try:
        await db[database_name][newsfeed_collection].update_one({"id":post_id},{"$set":{"group":{}}})
        return True
    except:
        return False
    