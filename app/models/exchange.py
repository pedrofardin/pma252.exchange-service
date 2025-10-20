from pydantic import BaseModel, Field


class ExchangeResponse(BaseModel):
    """Response model for exchange rate"""
    from_: str = Field(..., alias="from", serialization_alias="from")
    to: str
    sell: float
    buy: float
    date: str
    id_account: str = Field(..., alias="id-account")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "from": "USD",
                "to": "BRL",
                "sell": 5.40,
                "buy": 5.41,
                "date": "2025-10-19 12:00:00",
                "id_account": "123"
            }
        }
