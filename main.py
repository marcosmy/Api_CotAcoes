from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cotacao/{ticker}")
def get_cotacao(ticker: str):
    try:
        acao = yf.Ticker(ticker)
        info = acao.info
        return {
            "ticker": ticker,
            "preco": info.get("regularMarketPrice"),
            "nome": info.get("shortName"),
            "moeda": info.get("currency")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
