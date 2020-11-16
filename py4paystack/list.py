import requests
import uuid
import settings
import errors
endpoint="https://api.paystack.co/transaction/initialize"
GET, POST=requests.get, requests.post

headers=settings.headers
r_url=settings.r_url
po_all=settings.po_all

class Transaction:
    """
    List transactions carried out on your integration.
    args:
    ref: reference code
    ref(string) --> Unique transaction reference. It is a one-time key generated after initializing transaction.
    """
    
    def __init__(self, perPage = None, page = None, **kwargs):
        self.data=kwargs:
        self.req=GET("https://api.paystack.co/transaction", json=self.data, headers=headers) if self.data else GET("https://api.paystack.co/transaction", json=self.data, headers=headers)
    def json(self):
        data=self.req.json()
        return data['data'][0]
