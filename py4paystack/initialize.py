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
    def __init__(self, redirect_url=r_url,payment_options=None, ref=None, currency=None):
        self.redirect_url=redirect_url
        self.payment_options=payment_options or po_all
        self.currency=currency if currency else'NGN'
        self.ref=ref if ref else uuid.uuid4().hex
    def getLink(self, amount, email,  **kwargs):
        """
        
        amount(string): amount to be charged
        email(string): email address
        kwarg:
            first_name(string) --> None
            last_name(string) --> None
            phone(string) --> None
        callback_url(string) --> None: url to redirect to after successful transaction
        """
        data={"amount": amount,
              "email": email,
              "currency":self.currency,
              "ref":self.ref,
              'callback_url':self.redirect_url,
              "metadata": {
        'custom_fields': [kwargs]
      }
              }
        req=POST(endpoint, headers=headers, json=data)
        response=req.json()
        if req.status_code==200:
            return response['data']['authorization_url']
        else:
            return errors.errormsg(self.__int__(), response['meessage'])
if __name__ =='__main__':
    x=Transaction()
    print(x.getLink(1000, 'fikifaka@gmail.com'))
