#settings.py
secret_key='sk_test_e4e73202952f186dde677ddf47d7df5a780da525'
headers={"Authorization":"Bearer %s"%secret_key, "Content-Type": "application/json"}
r_url='https://halal.pythonanywhere.com/kiip/status'
po_all=[
		"card",
		 "bank"
		 ]
