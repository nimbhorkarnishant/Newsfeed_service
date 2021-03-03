from ..core.config import database_name, newsfeed_collection



async def read_db_sort_desc(db):
    try:
        data= db[database_name][newsfeed_collection].find().sort('createdAt',-1)
        return data
    except:
        return False

async def post_db(db,json_data):
    try:
        await db[database_name][newsfeed_collection].insert_one(json_data)
        return True
    except:
        return False
    
async def update_news_feed_db(db,post_id,post_data):
    try:
        await db[database_name][newsfeed_collection].update_one({"id":post_id},{"$set":post_data})
        return True
    except:
        return False
    
async def delete_news_feed_db(db,post_id):
    try:
        await db[database_name][newsfeed_collection].delete_one({"id":post_id})
        return True
    except:
        return False