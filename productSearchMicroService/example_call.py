import requests

results = requests.get("http://flip1.engr.oregonstate.edu:6363/productsearch?greenEnergyType='solar'&cost=leq400")
print(results.text)