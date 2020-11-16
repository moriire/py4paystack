# py4paystack
[![N|Solid](https://cldup.com/dTxpPi
9lDf.thumb.png)](https://nodesource.
com/products/nsolid)
[![Build Status](https://travis-ci.o
rg/joemccann/dillinger.svg?branch=ma
ster)](https://travis-ci.org/joemcca
nn/dillinger)
py4paystack is a python sdk for
connecting to paystack payment sol
It currently supports:
- [Payment
  Initialization]("https://paystack.
  com/docs/api/#transaction-initiali
  ze") - Initialize a transaction
  from your backend through the
  generation of a secure payment
  link
- [payment
  Verification]("paystack.com") -
  Confirm the status of a
  transaction
- [Charge authorization]() - All
  authorizations marked as reusable
  can be charged with this endpoint
  whenever you need to recieve
  payments.
- [transfer listings]() - List
  transactions carried out on your
  integration.
- transaction fetching
### Installation
```sh
python3 -m pip install --upgrade
py4paystack
```
For production environments...
```sh
cd ~/my-project-dir
echo "export SECRET_KEY=secretvalue"
>> .env
echo "export
PUBLIC_SECRET=othersecretkeys" >>
.env
```
