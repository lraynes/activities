#creating prompts
name = input("What is your name?")
age = int(input("How old are you?"))
true_false = bool(input("True or False: Is this statement true?"))

print("My name is " + str(name))
print("My age is " + str(age))
print ("I will be " + str(age + 1) + " this year")
print("This statement is " + str(true_false))