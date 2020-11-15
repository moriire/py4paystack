import requests
import uuid
import settings
import errors
endpoint="https://api.paystack.co/transaction/initialize"
GET, POST=requests.get, requests.post

headers=settings.headers
class Transaction:
    """
    For Verifying Transactions Before giving value to your customer, you \
    should verify the status of the transaction by passing the reference to the API.\
    args:
    ref: reference code
    ref(string) --> The transaction reference used to intiate the transaction"""
    def __init__(self, ref='491336026'):
        self.ref=ref# if isinstance(ref, string) else 1
        self.req=GET("https://api.paystack.co/transaction/verify/"+self.ref, headers=headers)
        self.resp=self.req.json()
    
    def __int__(self):
        return self.req.status_code
        
    def __str__(self):
        if self.__int__()==200:
            return self.resp['data']['status']
        else:
            raise errors.errormsg(self.__int__(), self.resp['message'])

x=Transaction()
print(x)
