def printHello():
    print("Hello")
printHello()

print("--------")

def printName(name):
    print("Hello " + name + "!")
printName("Emma")

print("-------")

listOne = [1,2,3,4,5,6]
print("------")

listTwo = [11,12,13,14]
print("------")

def listInfo(lst):
    print("The values within the list are...")
    for value in lst:
        print(value)
    print("length = " + str(len(lst)))

listInfo(listOne)
listInfo(listTwo)
listInfo([1,2,3,4,5])


a = [1,2,3]
x, y, z = a
print(x) #1
print(y) #2
print(z) #3

a = ["Hello", "World"]
print(" ".join(a))




a = 8
b = 5
b, a = a, b #b now equals 8, a now equals 5