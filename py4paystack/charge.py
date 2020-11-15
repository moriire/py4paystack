class Auth:
    def __init__(self, redirect_url=r_url,payment_options=None, ref=None, currency=None):
        self.redirect_url=redirect_url
        self.payment_options=payment_options or po_all
        self.currency=currency or 'NGN'
        self.ref=ref or uuid.uuid4().hex
        
    def getLink(self, amount, email, authorization_code=None, **kwargs):
        """
        kwargs:
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
              "authorization_code":authorization_code,
              "currency":self.currency,
              "ref":self.ref,
              'callback_url':self.redirect_url,
              "metadata": {
        'custom_fields': [kwargs]
      }
              }
        req=POST("https://api.paystack.co/transaction/charge_authorization", headers=headers, json=data)
        response=req.json()
        if req.status_code==200:
            return response['data']['authorization_url']
        else:
            return response
        

