ERR={
        'E400':"""A validation or client side error occurred and the request was not fulfilled.""",
         'E401':"""The request was not authorized. This can be triggered by passing an invalid secret key in the authorization header or the lack of one""",
        'E404':"""Request could not be fulfilled as the request resource does not exist.""",
        'E500S':"""Request could not be fulfilled due to an error on Paystack's end. This shouldn't happen so please report as soon as you encounter any instance of this."""
        }
class Errors(Exception):
    pass

class ValueTooSmallError(Errors):
    def __init__(self, value, msg):
        self.value=value
        self.msg=msg
    def __str__(self):
        return f"{self.msg}, {self.value} is too small. it must be greater than 100"

class ValidationError(Errors):
    def __init__(self, value, msg):
        self.value=value
        self.msg=msg
    def __str__(self):
        return f"Error {self.value}.{self.msg}"

class UnfulfilledRequestError(Errors):
    def __init__(self, value, msg):
        self.value=value
        self.msg=msg
    def __str__(self):
        return f"Error {self.value}. {self.msg}"

class UnauthorizedRequestError(Errors):
    def __init__(self, value, msg):
        self.value=value
        self.msg=msg
    def __str__(self):
                return f"Error {self.value}. {self.msg}"
        
class PaystackError(Errors):
    def __init__(self, value, msg):
        self.value=value
        self.msg=msg
    def __str__(self):
        return f"Error {self.value}. {self.msg}"

def accessValidity(errCode):
        errMsg=ERR[f"E{errCode}"]
        if errCode==200:
                True
        elif errCode==400:
                raise ValidationError(errCode, errMsg)
        elif errCode==401:
                raise UnfulfilledRequestError(errCode, errMsg)
        elif errCode==404:
                raise UnauthorizedRequestError(errCode, errMsg)
        """
        elif errCode in (500, 501, 502, 503,504):
                raise PaystackError(500, ERR[f"E{errCode}S"])
        """

def errormsg(errCode, errMsg):
        if errCode==400:
                raise ValidationError(errCode, errMsg)
        elif errCode==401:
                raise UnfulfilledRequestError(errCode, errMsg)
        elif errCode==404:
                raise UnauthorizedRequestError(errCode, errMsg)
        
        elif errCode in (500, 501, 502, 503,504):
                raise PaystackError(500, errMsg)
        """

def hey(a):
    if a==1: raise ValueTooSmallError(a, 'The value has to be greater than 20')

def eCode(n):
    return accessValidity(n)

x=eCode(400)
print(x)
"""