#lib de router
from fastapi import APIRouter

#crear router
router = APIRouter(
    prefix="/index",#nombre de identificacion de api o url
    tags=["indexs"]#nombre para el docs url
)

@router.get("/")
async def index():
    return "index"