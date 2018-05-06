dictionary = {
    "name": "Laura", 
    "age": 42, 
    "hobbies": ["swing dancing", "crochet", "reading"], 
    "wake_up": ["8:45", "8:40", "9:00"]
    }

print("My name is " + str(dictionary["name"]))
print("My age is " + str(dictionary["age"]))
print("I have " + str(len(dictionary["hobbies"])) + " hobbies")
print("I sometimes wake up at " + str(dictionary["wake_up"][1]))

#another way to list out the things in the dictionary w/o brackets
#for hobby in dictionary["hobbies"]:
    #print(hobby)

#look up 
    #.values for all values, 
    #.items references whole thing and create a tuple to extract keys and values
#for time in dictionary["wake_up"].items():
    #print(time)