#create a path
file = ".\\Resources\\input.txt"

#opens file
with open(file, "r") as text:
    print(text)
    
    #prints the text of the file
    lines = text.read() #puts file into list you can iterate over
    print(lines)

#  \t = tab     \n = new line   \\ = \      \" = "        \' = '