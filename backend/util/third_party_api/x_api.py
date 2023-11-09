from requests_oauthlib import OAuth1Session
from app.settings.local import *


class XApi:
    def __init__(self):
        self.__logger = ""

    def search(self):
        x = OAuth1Session(
            X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
        )
        url = "https://api.twitter.com/2/users/me"
        res = x.get(url)
        return res
