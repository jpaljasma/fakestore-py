from typing import List
from fakestoreapi.base import Base, ApiRequestException
import requests


class Products(Base):
    def __init__(self) -> None:
        super().__init__()
        self.API_ENDPOINT += "products"

    def list(self) -> List[dict]:
        response = requests.get(f"{self.API_ENDPOINT}")
        if response.status_code == 200:
            return response.json()
        else:
            raise ApiRequestException(response.status_code)
