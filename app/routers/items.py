from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/items")

@router.get("/all")
async def get_all_items():
   return {"message": "Retrieved all items"}

# list of item IDs for purchased items
class PurchaseRequest(BaseModel):
    item_ids: List[int]


@router.post("/purchase")
async def purchase_items(purchase: PurchaseRequest):
    return {"message": "Items purchased", "count": len(purchase.item_ids)}


