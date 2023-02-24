#lib de router
from fastapi import APIRouter

#crear router
router = APIRouter(
    prefix="",#nombre de identificacion de api o url
    tags=["Homes"]#nombre para el docs url
)

@router.get("/")
async def Home():
    return "index"