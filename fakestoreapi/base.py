class Base:
    API_ENDPOINT = "https://fakestoreapi.com/"

    def __init__(self) -> None:
        pass

class ApiRequestException(Exception):
    pass