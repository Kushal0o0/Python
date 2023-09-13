dict1 ={"name": "Mike", "salary": 8000000000}
dict1.update({"name": "kushal", "color": "[red, blue]"})
print(dict1.items())


stocks = {"aapl": 121, "amz": 3380, "msft": 219, "biib": 280, "qdel": 260, "lvgo": 140}

new_stock = {}
for names, value in stocks.items():
    new_stock[names] = value * 1.02
print(new_stock)
