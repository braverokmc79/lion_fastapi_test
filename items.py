from fastapi import  HTTPException, APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()




# Pydantic 모델
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# 임시 DB (메모리 기반)
fake_items_db: List[Item] = []



# 아이템 생성
@router.post("/items/", response_model=Item)
def create_item(item: Item):
    fake_items_db.append(item)
    return item



# 전체 조회
@router.get("/items/", response_model=List[Item])
def read_item_list():
    return fake_items_db





# 단일 아이템 조회
@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in fake_items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")






# 아이템 수정
@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(fake_items_db):
        if item.id == item_id:
            fake_items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")




# 아이템 삭제
@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(fake_items_db):
        if item.id == item_id:
            del fake_items_db[index]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")



