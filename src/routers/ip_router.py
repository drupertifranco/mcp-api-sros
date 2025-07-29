from fastapi import APIRouter, HTTPException
from src.types.index import IPPrefix
from src.services.sros_service import add_ip_prefix, delete_ip_prefix

router = APIRouter()

@router.post("/add-ip")
async def add_ip(ip_prefix: IPPrefix):
    try:
        result = await add_ip_prefix(ip_prefix.prefix_name, ip_prefix.prefix)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete-ip")
async def delete_ip(ip_prefix: IPPrefix):
    try:
        result = await delete_ip_prefix(ip_prefix.prefix_name, ip_prefix.prefix)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))