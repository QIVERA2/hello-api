from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="我的第一个 API")


class Item(BaseModel):
    name: str
    done: bool = False


items: list[Item] = []


@app.get("/")
def root():
    return {"message": "hello，我的第一个 API 跑起来了"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/items")
def add_item(item: Item):
    items.append(item)
    return {"total": len(items), "item": item}


@app.get("/items")
def list_items():
    return items
