
class Transaction:
    """
    For Verifying Transactions Before giving value to your customer, you \
    should verify the status of the transaction by passing the reference to the API.\
    args:
    ref: reference code
    ref(string) --> Unique transaction reference. It is a one-time key generated after initializing transaction.
    """
    def __init__(self, id='283868400'):
        self.id=id
        
    def __bool__(self):
        req=GET("https://api.paystack.co/transaction/:"+id, headers=headers)
        response=req.json()
        #errors.accessValidity(req.status_code)
        if req.status_code==200:
            return response['status']
        else:
            return response
