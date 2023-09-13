stocks = {"aapl": 121, "amz": 3380, "msft": 219, "biib": 280, "qdel": 260, "lvgo": 140}

# gives a 2 percent return on the values
new_stock = {}
for names, value in stocks.items():
    new_stock[names] = value * 1.02
print(new_stock)

new_stock = {names: values * 1.02 for (names, values) in stocks.items()}
print(f"{new_stock} \n")
##################################################################################################################

# gives a list of stocks with values more than 200
new_stock = {}
for names, value in stocks.items():
    if value > 200:
        new_stock[names] = value
print(new_stock)

new_stock = {names: values for (names, values) in stocks.items() if values > 200}
print(f"{new_stock} \n")
#####################################################################################################################

# gives a return of 2 percent on stocks with more than 200 value
new_stock = {}
for names, values in stocks.items():
    if values > 200:
        new_stock[names] = values * 1.02
print(new_stock)

new_stock = {names: values * 1.02 for (names, values) in stocks.items() if values > 200}
print(f"{new_stock} \n")
#####################################################################################################################

# hold or sell depending on the value of the stock
new_stock = {}
for names, values in stocks.items():
    if values > 200:
        new_stock[names] = "sell"
    else:
        new_stock[names] = "hold"
print(new_stock)

new_stock = {names: ("sell" if values > 200 else "hold") for (names, values) in stocks.items()}
print(f"{new_stock} \n")
#####################################################################################################################

# iteraritng 2 different lists and creating a new dictionary of it
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
dct = {}
for i in list1:
    for j in list2:
        dct.update({(i, j): str(j)})
print(dct)

dct = {(i, j): str(j) for i in list1 for j in list2}
print(dct)