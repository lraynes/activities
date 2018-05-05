def pow(base, exp):
    return base ** exp
    
operation = int(input("To what power do you want to raise this number: "))
grapes = int(input("Input your number: "))
print(pow(grapes, operation))