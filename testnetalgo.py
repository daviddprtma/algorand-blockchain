from algosdk.v2client import algod

# Connecting to the Algod Client on the Algorand sandbox
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)

# Declare your Address
my_address = "AIEAJFEUAM4LJ6VCZHRKAX6YOBSNK46JGALXIYXGIB4BJFD5XJEMLQOHXY"

account_info = algod_client.account_info(my_address)
print("Account balance: {} microAlgos".format(account_info.get('amount')))