import json
import requests

class ApiRequest:

    def __init__(self, link):
        self.link = link

    def request(self, params):
        """Send a request to an api

        :param params: the parameters sent to the api
        :return: A hashmap with the results sent by the api
        """
        return requests.get(self.link, params=params).json()

