class Timeline:
    """
    For Verifying Transactions Before giving value to your customer, you \
    should verify the status of the transaction by passing the reference to the API.\
    args:
    ref: reference code
    ref(string) --> Unique transaction reference. It is a one-time key generated after initializing transaction.
    """
    def __init__(self, id_or_reference):
        self.id=id
        
    def __bool__(self):
        request=GET("https://api.paystack.co/transaction/timeline/:"+id_or_reference, headers=headers)
        data=request.json()
        return data['status']
