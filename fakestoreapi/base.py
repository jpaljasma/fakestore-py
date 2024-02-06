from typing import List
import requests


class Base:
    API_ENDPOINT = "https://fakestoreapi.com/"

    def __init__(self) -> None:
        pass

    def _json_req(self, url: str = None) -> List[dict]:
        """
        Calls the API endpoint
        """
        if url is None:
            url = self.API_ENDPOINT

        print(f"[DEBUG]\tAccessing API Endpoint {url} ...")

        hdrs = {
            "Accept-Language": "en-US,en;q=0.9,et;q=0.8,la;q=0.7",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }

        response = requests.get(f"{self.API_ENDPOINT}", headers=hdrs)

        if response.status_code == 200:
            return response.json()
        else:
            raise ApiRequestException(response.status_code)


class ApiRequestException(Exception):
    pass
