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
    For Verifying Transactions Before giving value to your customer, you 
    should verify the status of the transaction by passing the reference to the API.
    args:
    ref: reference code
    ref(string) --> Unique transaction reference. It is a one-time key generated after initializing transaction.
    """
    
    def __init__(self, **kwargs):
        self.data=kwargs
        if not self.data:
            self.data["perPage"]=50
            self.data["page"]=1
        self.req=GET("https://api.paystack.co/transaction", headers=headers)
        
    def json(self):
        data=self.req.json()
        return data['data'][0]
