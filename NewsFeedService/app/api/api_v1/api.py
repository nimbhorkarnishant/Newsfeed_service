from fastapi import APIRouter
from .endpoints.news_feed.news_feed import router as news_feed_router
from .endpoints.news_feed.likes import router as likes_router
from .endpoints.news_feed.comment import router as comment_router
from .endpoints.news_feed.group import router as group_router
from .endpoints.news_feed.tagcoworkers import router as tag_router
from .endpoints.news_feed.media import router as media_router

router = APIRouter()
router.include_router(news_feed_router)
router.include_router(likes_router)
router.include_router(group_router)
router.include_router(tag_router)
router.include_router(comment_router)
router.include_router(media_router)





