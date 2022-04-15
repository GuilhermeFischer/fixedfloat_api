# -*- coding: utf-8 -*-

from typing import Optional
import requests, hmac, hashlib
from urllib.parse import urlencode

# API Documentation: https://fixedfloat.com/api
# Get your API KEY: https://fixedfloat.com/?ref=a7u3rzvc

class FixedFloat():
    def __init__(self, API_KEY: str, SECRET_KEY: str) -> None:
        self._API_KEY = API_KEY
        self._SECRET_KEY = SECRET_KEY
        self._MAIN_URL = "https://fixedfloat.com/api/v1/"
    
    def _sendRequest(self, reqMethod: str = None, apiMethod: str = None, body: str = "") -> Optional[dict]:
        if(reqMethod and apiMethod):
            headers = {
                "X-API-KEY": self._API_KEY,
                "X-API-SIGN": hmac.new(self._SECRET_KEY.encode("utf-8"), body.encode("utf-8"), hashlib.sha256).hexdigest(),
                "Content-Type": "application/x-www-form-urlencoded"
            }
            if(reqMethod == "GET"):
                r = requests.get(self._MAIN_URL + apiMethod + "?" + body, headers=headers, data="")
            elif(reqMethod == "POST" and body != ""):
                r = requests.post(self._MAIN_URL + apiMethod, headers=headers, data=body)
            else:
                return None
            
            if(r.status_code == 200):
                return r.json()
            else:
                return None

    def getCurrencies(self):
        """ Getting a list of all currencies that are available on FixedFloat.com """ 
        return self._sendRequest("GET", "getCurrencies")

    def getPrice(self, fromCurrency: str, toCurrency: str, fromQty: float, toQty: float = 0.00, type: str = "float"):
        """ Information about a currency pair with a set amount of funds """
        body = urlencode({"fromCurrency": fromCurrency, "toCurrency": toCurrency, "fromQty": float(fromQty), "toQty": float(toQty), "type": type})
        return self._sendRequest("POST", "getPrice", body)

    def getOrder(self, id: str, token: str) -> list:
        """ Receiving information about the order """
        body = urlencode({"id": id, "token": token})
        return self._sendRequest("GET", "getOrder", body)

    def setEmergency(self, id: str, token: str, choice: str, address: str = ""):
        """ Emergency Action Choice """
        body = urlencode({"id": id, "token": token, "choice": choice, "address": address})
        return self._sendRequest("GET", "setEmergency", body)

    def createOrder(self, fromCurrency: str, toCurrency: str, toAddress: str, fromQty: float, toQty: float = 0.00, type: str = "float", extra: str = ""):
        """ Creating exchange orders """
        body = urlencode({"fromCurrency": fromCurrency, "toCurrency": toCurrency, 
            "fromQty": float(fromQty), "toQty": float(toQty), "toAddress": toAddress, "extra": extra, "type": type})
        return self._sendRequest("POST", "createOrder", body)
