import uvicorn
from fastapi import FastAPI
from finally import config

app = FastAPI(
    title="FinAlly API",
    description="API para o Sistema de Gestão Financeira Familiar",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API do FinAlly!"}

if __name__ == "__main__":
    uvicorn.run(
        "finally.api.main:app",
        host=config.API_HOST,
        port=config.API_PORT,
        reload=config.ENV == "development"
    )
