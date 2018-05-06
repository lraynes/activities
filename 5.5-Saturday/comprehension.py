prices= ["24", "13", "16000", "1400"]
#convert string to integer within all of list by looping through
price_nums = [int(price) for price in prices]
print(prices)
print(price_nums)


dog = "poodle"
letters = [letter for letter in dog]
print(letters)
print(f"we iterate over a string into a list: {letters}")

#capitalize by looping through each letter
capital_letters = [letter.upper() for letter in letters]
print(capital_letters)
#OR
capital_letters = []
for letter in letters:
    capital_letters.append(letter.upper())

#eliminate a letter
no_o = [letter for letter in letters if letter != "o"]
print(no_o)
#or
no_o = []
for letter in letters:
    if letter != "o":
        no_o.append(letter)

june_temperature = [72,65,59,87]
july_temperature = [87,85,92,72]
august_temperature = [88,77,66,100]

temperature = [june_temperature,july_temperature,august_temperature]

low_temp = [min(temp) for temp in temperature]
print(low_temp)
#OR longhand
low_temp = []
for temp in temperature:
    low_temp.append(min(temp))

#average
print(sum(low_temp)/len(low_temp))
print(low_temp[0])
print(low_temp[1]) 
print(low_temp[2])

max_temp = max(temp for temp in temperature)
print(max_temp)

#difference btn defining a function and calling a function

def name(parameter):
    return "Hello " + parameter
print(name("Laura"))

#create average; sum function only works with list
def average(data):
    return sum(data)/len(data)

print(average([1,2,3,4,5]))

#can have conditional in a function as long as only one return can happen at a time, no overlap
def mutiple3(a):
    if(a % 3 == 0):
        return True
    else:
        return False