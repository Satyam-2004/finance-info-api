from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {"status": "ok"}

@app.get("/stocks/{symbol}")
def get_stock(symbol: str):
    return {"symbol": symbol}

@app.get("/stocks/{symbol}/history")
def get_stock_history(symbol: str, period: str = "1mo"):
    return {
        "symbol": symbol,
        "period" : period
    }

#################################

@app.get("/item/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

#################################
@app.get("/items/{items_id}")
async def read_items(items_id: str, q : str | None = None , short: bool = False):
    item = {"items_id": items_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item 