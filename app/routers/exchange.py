from fastapi import APIRouter, Header
from app.models.exchange import ExchangeResponse
from app.services.awesome_api_service import AwesomeAPIService


router = APIRouter(
    prefix="/exchange",
    tags=["exchange"]
)


@router.get("/{currency_from}/{currency_to}", response_model=ExchangeResponse)
def get_exchange_rate(
    currency_from: str,
    currency_to: str,
    authorization: str = Header(...),
    id_account: str = Header(..., alias="id-account")
) -> ExchangeResponse:
    """
    Get exchange rate between two currencies

    - **currency_from**: Source currency code (e.g., USD)
    - **currency_to**: Target currency code (e.g., BRL)
    - **authorization**: Bearer token (required)
    - **id-account**: Account ID from gateway (required)
    """
    # Fetch exchange rate from AwesomeAPI
    exchange_data = AwesomeAPIService.get_exchange_rate(currency_from, currency_to)

    # Build response
    return ExchangeResponse(
        from_=currency_from.upper(),
        to=currency_to.upper(),
        sell=float(exchange_data["bid"]),
        buy=float(exchange_data["ask"]),
        date=exchange_data["create_date"],
        id_account=id_account
    )
