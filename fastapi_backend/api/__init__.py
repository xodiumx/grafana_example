from fastapi import APIRouter
from . import test_urls

router = APIRouter()
router.include_router(test_urls.router, tags=["monitoring"])