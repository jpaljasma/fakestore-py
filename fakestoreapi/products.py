from typing import List
from fakestoreapi.base import Base

class Products(Base):
    def __init__(self) -> None:
        super().__init__()
        self.API_ENDPOINT += "products"

    def list(self) -> List[dict]:
        return self._json_req()