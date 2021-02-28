from fastapi import APIRouter
from .endpoints.news_feed.news_feed import router as news_feed_router
from .endpoints.news_feed.likes import router as likes_router
from .endpoints.news_feed.comment import router as comment_router


router = APIRouter()
router.include_router(news_feed_router)
router.include_router(likes_router)
router.include_router(comment_router)



