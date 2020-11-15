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
    ref(string) --> Unique transaction reference. It is a one-time key generated after initializing transaction.
    """
    def __init__(self, id='39415032'):
        self.id=id
        self.req=GET("https://api.paystack.co/transaction/:"+id, headers=headers)
    def __comp__(self):
        if self.req.status_code==200: return response['status']
        else: return response

    def json(self):
        response=self.req.json()

