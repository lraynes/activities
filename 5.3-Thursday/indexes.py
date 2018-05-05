import os
import csv


indexes = [1,2,3,4,5,6,7,8,9]
employees = ["John", "Sam", "Jerry", "Ralph", "Joseph"]
department = ["Management", "Sales", "Maintenence", "HR", "Cook"]

#zip pairs them up
roster = zip(indexes, employees, department)

output = os.path.join("output.csv")
"""with open(output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Index", "Employee", "Department"])
    writer.writerow(roster)
"""
for employees in roster:
    print(employees)