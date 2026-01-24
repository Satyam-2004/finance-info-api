from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd
import yfinance as yf
from typing import Optional

app = FastAPI()

@app.get("/save-stock/{ticker}")
def save_stocks_data(ticker: str, period: Optional[str] = "1mo"):
    
    data = yf.download(ticker, period=period)

    if data.empty:
        return {"message" : "No data found for ticker"}
    
    filename = f"{ticker}_{period}.csv"
    data.to_csv(filename)

    return {"message" : f"Stock data for {ticker} has been for {period} period"}

@app.get("/display")
def display_data(ticker: str, period: str):
    csv_file = f"{ticker}_{period}.csv"

    return FileResponse(
        path=csv_file,
        media_type="text/csv",
        filename="data_download.csv"
    )