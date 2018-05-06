lst = ["A", "B", "C"]

item = {"key": "value"}
print(item["key"])

item2 = {"name": "Drew"}
print(item2["name"])

#dictionary can contain multiple pair of information
hero = {"name": "Iron Man", "nationality": "United States", "type": False}

item3 = {"bag": ["laptop", "usb", "food"], "pocket": [5.00, 1.00, 'gum'],
    "reddit": {"key": [1,2,3,4]}}

print(item3["bag"])
print(item3["pocket"])
print(item3["reddit"]["key"][3])

#loop through dictionary
for keys in item3:
    print(keys)