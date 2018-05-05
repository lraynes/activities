list = ["Snickers", "Twix", "M&Ms", "Laffy Taffy", "Skittles"]

allowance = 3

candy_cart = []

for candy in list:
    print("[" + str(list.index(candy)) + "]", candy)

for x in range(allowance): #use range if there's a start and end
    selected = int(input("which candy would you like? "))
    candy_cart.append(list[selected])
    print(candy_cart)

print("I brought home:")
for candy in candy_cart:
    print(candy, end=" ")