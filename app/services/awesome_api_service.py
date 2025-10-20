import requests
from fastapi import HTTPException
from typing import Dict, Any


class AwesomeAPIService:
    """Service to interact with AwesomeAPI for exchange rates"""

    BASE_URL = "https://economia.awesomeapi.com.br/json/last"

    @staticmethod
    def get_exchange_rate(currency_from: str, currency_to: str) -> Dict[str, Any]:
        """
        Fetch exchange rate from AwesomeAPI

        Args:
            currency_from: Source currency code (e.g., 'USD')
            currency_to: Target currency code (e.g., 'BRL')

        Returns:
            Dictionary with exchange rate data

        Raises:
            HTTPException: If API call fails or rate not found
        """
        url = f"{AwesomeAPIService.BASE_URL}/{currency_from.upper()}-{currency_to.upper()}"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            # A chave é a concatenação das moedas sem hífen
            key = f"{currency_from.upper()}{currency_to.upper()}"

            if key not in data:
                raise HTTPException(
                    status_code=404,
                    detail=f"Exchange rate for {currency_from}/{currency_to} not found"
                )

            return data[key]

        except requests.HTTPError as e:
            raise HTTPException(
                status_code=e.response.status_code,
                detail="Error fetching exchange rate from AwesomeAPI"
            )
        except requests.RequestException as e:
            raise HTTPException(
                status_code=503,
                detail="Service temporarily unavailable"
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Internal server error: {str(e)}"
            )
