from fastapi import FastAPI
from src.routers.ip_router import router as ip_router

app = FastAPI()

app.include_router(ip_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the IP Router API"}