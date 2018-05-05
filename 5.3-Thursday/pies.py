pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffe", "Black Bun", "Blueberry", "Buko", "Burek", "Tamal", "Steak"]

shopping = "y"

order_form = []

#to escape a while loop with no iterator, type ctrl+z and click enter



while shopping == "y":
    print("Welcome to the House of Pies! Here are our pies:")
    print("---------------")

    for pies in pie_list:
        print("(" + str(pie_list.index(pies)+1) + ")", pies, end=" ")

    order = int(input("\nWhich would you like to order? "))
    order_form.append(order)

    print("Great! We'll have that " + str(pie_list[order - 1]) + " pie right out for you.")

    shopping = str(input("Would you like to continue shopping? y/n "))

print("------")
print("You have purchased " + str(len(order_form)) + " pies:")

for i in order_form:
    print(pie_list[i-1])