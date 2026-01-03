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