# Import Numpy for calculations and matplotlib for charting
import numpy as np
import matplotlib.pyplot as plt

# Creates a list from 0 to 10 with each step being 0.1 higher than the last
x_axis = np.arange(0,5, 0.1)
x_axis

# Creates an exponential series of values which we can then chart
e_x = [np.exp(x) for x in x_axis]
e_x

# Creates a list based on the sin of our x_axis values
sin = np.sin(x_axis)
sin

# Plot the line
plt.plot(x_axis, y_axis)
plt.xlabel("Month")
plt.ylabel("Avg Temp")

# Convert to Celsius C = (F-32) * 0.56
y_celcius = [(temp - 32) * 0.56 for temp in y_axis] #one line for loop
y_celcius

# Plot both on the same chart
plt.plot(x_axis, y_celcius, "-b", label = "Celsius") #-b is blue, -r is green
plt.plot(x_axis, y_axis, "-r", label = "Fahrenheit")
plt.legend(loc = "upper left")
plt.xlabel("Month")
plt.ylabel("Avg Temp")

# Each point on the sine chart is marked by a blue circle
sine_handle = plt.plot(x_axis, sin, marker ='o', color='blue', label="Sine")
# Each point on the cosine chart is marked by a red triangle
cosine_handle = plt.plot(x_axis, cos, marker='^', color='red', label="Cosine")
# Adds a legend and sets its location to the lower right
plt.legend(loc="lower right")

# Saves an image of our chart so that we can view it in a folder
plt.savefig("Images/lineConfig.png")

# Create a handle for each plot
celcius_handle, = plt.plot(x_axis, y_celcius, marker ='s', color='red', label="Celsius") #need comma after variable
# Each point on the cosine chart is marked by a red triangle
fahrenheit_handle, = plt.plot(x_axis, y_axis, marker='+', color='blue', label="Fahrenheit") #need comma after variable
# Set our legend to where the chart thinks is best
plt.legend(handles = [celcius_handle, fahrenheit_handle], loc = "best")

# Add labels to the x and y axes
plt.title("Speed of Danger Drop and Rail Gun")
plt.xlabel("Seconds")
plt.ylabel("Speed")

#BAR GRAPH
# Tell matplotlib that we will be making a bar chart
# Users is our y axis and x_axis is, of course, our x axis
# We apply align="edge" to ensure our bars line up with our tick marks
plt.bar(x_axis, users, color='r', alpha=0.5, align="center")
# Tell matplotlib where we would like to place each of our x axis headers
tick_locations = [value for value in x_axis]
plt.xticks(tick_locations, ["Java", "C++", "Python", "Ruby", "Clojure"])
# Sets the x limits of the current chart
plt.xlim(-0.75, len(x_axis)-0.25) #length minus .25
# Sets the y limits of the current chart
plt.ylim(0, max(users)+5000) #max plus 5k for buffer
# Give our chart some labels and a tile
plt.title("Popularity of Programming Languages")
plt.xlabel("Programming Language")
plt.ylabel("Number of People Using Programming Languages")

#PIE CHART
# Labels for the sections of our pie chart
labels = ["Python", "C++", "Ruby", "Java"]
# The values of each section of the pie chart
sizes = [185, 172, 100, 110]
# The colors of each section of the pie chart
colors = ["yellowgreen", "red", "lightcoral", "lightskyblue"]
# Tells matplotlib to seperate the "Python" section from the others bc it's the first thing listed
explode = (0.1, 0, 0, 0)
# Creates the pie chart based upon the values above
# Automatically finds the percentages of each part of the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=140)
# Tells matplotlib that we want a pie chart with equal axes
plt.axis("equal")

#SCATTER PLOT
# Tells matplotlib that we want to make a scatter plot
# The size of each point on our plot is determined by their x value
plt.scatter(x_axis, data, marker="*", facecolors="red", edgecolors="black", s=x_axis, alpha=0.75) 
#s = scale, size of dots. can be a third variable affecting it
# The y limits of our scatter plot is 0 to 1
plt.ylim(0, 1)
# The x limits of our scatter plot is 0 to 100
plt.xlim(0, x_limit)