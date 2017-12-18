"""
Script to demonstrate issue 493
NOTE:  This only works with a fresh set of testrpc accounts.
It relies on having enough
ether in there to make the transaction happen.
"""

from web3 import Web3, HTTPProvider, TestRPCProvider

# web3.py instance
w3 = Web3(HTTPProvider('http://testrpc:8545'))
# w3 = Web3(TestRPCProvider())

# Print out gas price
print(f'Gas price: {w3.eth.gasPrice}')

# Create new local account
acct = w3.eth.account.create()
print(f'Local account created: {acct.address}')

# Print out initial testrpc balances
print('Initial TestRpc balances:')
for i in range(5):
    print(f'Account: {i}, Balance: {w3.eth.getBalance(w3.eth.accounts[i])}')

# Put some ether in the account
for i in range(5):
    value = w3.eth.getBalance(w3.eth.accounts[i]) - w3.eth.gasPrice
    w3.eth.sendTransaction({'to': acct.address,
                            'from': w3.eth.accounts[i],
                            'value': value
                            })
    print(f'Added {value} to local account')


# Print out new local account balance
print(f'New Local account balance: {w3.eth.getBalance(acct.address)}')

# Duplicate issue_493
try:
    w3.eth.sendTransaction({'from': acct.address, 'to': w3.eth.accounts[0], 'value': 1})
except ValueError as e:
    pass

# To solve this, need to sign the raw transaction using local account, and send a rawTransaction
transaction = {
        'to': w3.eth.accounts[0],
        'from': acct.address,
        'value': 100,
        'gas': 2000000,
        'gasPrice': 234567897654321,
        'nonce': 0,
        'chainId': 1
    }

# Sign the raw transaction using the local account
signed = w3.eth.account.signTransaction(transaction, acct.privateKey)

# Can also do
# signed = acct.sign(transaction)

# Balances before transaction
print('Balances before raw transaction from local account to TestRpc:')
print(f'Local Account Balance: {w3.eth.getBalance(acct.address)}')
print(f'TestRpc Account[0] Balance: {w3.eth.getBalance(w3.eth.accounts[0])}')

# Send the raw transaction
receipt = w3.eth.sendRawTransaction(signed.rawTransaction)

print(f'Transaction receipt: {receipt}')

# Balances after transaction
print('Balances after raw transaction from local account to TestRpc:')
print(f'Local Account Balance: {w3.eth.getBalance(acct.address)}')
print(f'TestRpc Account[0] Balance: {w3.eth.getBalance(w3.eth.accounts[0])}')
