from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/5a3bf6cd8ee1469294261c225f81a006"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())
print(web3.eth.blockNumber)
