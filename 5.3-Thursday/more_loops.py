for x in range(10):
    print (x)

print("------------")

for x in range (20,30):
    print(x)

print("------------")

for x in range (20,30,2):
    print(x)

print("-----------")

#prints list going through elements of loop
words = ["Iron Man,", "Captain America", "Hulk", "Gamora"]
for word in words:
    print (word)

print("-----x------")

#calculates length printing out by index
for i in range(len(words)):
    print(words[i])

print("-----------")

sentence = "Hello world"
for letter in sentence:
    print (letter)

print("-----------")

#case sensitive; while loop
x = "Yes"
while x == "Yes":
    print("Nice!")
    x = input("Try again (Yes/No")

print("-----------")

#more readable but slow
lst = []
for i in range(10):
    lst.append(i)
print(lst)

#faster; imbed using for loop
lst2 = [i for i in range(10)]
print(lst2)