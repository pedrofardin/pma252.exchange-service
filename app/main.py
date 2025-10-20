from fastapi import FastAPI
from app.routers import exchange


app = FastAPI(
    title="Exchange Service API",
    description="Microservice for currency exchange rates",
    version="1.0.0"
)


@app.get("/health", tags=["health"])
def health():
    """Health check endpoint"""
    return {"status": "ok"}


app.include_router(exchange.router)
