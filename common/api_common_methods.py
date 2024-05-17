import requests, json

class APICommonMethods:

    BaseURL = "https://swapi.dev"

    def __init__(self) -> None:
        pass

    def api_get(self, endPoint: str):
        response= requests.get(self.BaseURL + endPoint)
        return response.json()
