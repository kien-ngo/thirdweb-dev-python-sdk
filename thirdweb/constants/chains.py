from enum import Enum

# Only include supported chains since python doesn't support enum extension
class ChainId(Enum):
    MAINNET = 1
    RINKEBY = 4
    GOERLI = 5
    POLYGON = 137
    MUMBAI = 80001
    FANTOM = 250
    AVALANCHE = 43114
