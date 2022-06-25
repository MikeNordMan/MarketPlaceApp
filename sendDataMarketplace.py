from places import market_placesDict
from Marketplace import Marketplase


for name in market_placesDict:
    name = Marketplase(name, market_placesDict[name])
    name.testClass()
    name.printHTML()
