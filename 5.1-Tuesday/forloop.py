#zero is always the first!
for x in range(5):
    print(x)
print("--------------")

for x in range(1,20,2):
    print(x)

words = "Grapes"
for letters in words:
    print(letters)

zoo = ["dog", "cat", "bear"]
for animal in zoo:
    print(animal)

#always have an iterator (the run portion) otherwise endless loop
run = "y"
while run == "y":
    print("Hi")
    run = input("To run again, enter y")

#start from the end, reverse. The list goes backwards!
words = "Peace"
print(words[::-1])