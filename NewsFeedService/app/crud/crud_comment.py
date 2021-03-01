from ..core.config import database_name, newsfeed_collection



async def post_comment_db(db,post_id,comment_data,counter,op):
    try:
        await db[database_name][newsfeed_collection].update_one({"id":post_id},{"$inc":{"totalComments":counter},op:{"comments":comment_data}})
        return True
    except:
        return False
    

async def comment_reply_db(db,post_id,comment_id,reply_data,op):
    try:
        await db[database_name][newsfeed_collection].update_one({"id":post_id,"comments.id":comment_id},{op:{"comments.$.replies":reply_data}})
        return True
    except:
        return False