import os
import csv

csvpath = os.path.join(".", "employees.csv")

new_employee_data = []

with open(csvpath, newline="") as csvfile:
    #read data into dictionary
    csvreader = csv.DictReader(csvfile)
    
    #create new email
    for row in csvreader:
        first_name = row["First Name"]
        last_name = row["Last Name"]
        ssn = row["SSN"]

        email = str(first_name) + "." + str(last_name) + "@example.com"
        #OR use formatter email = f"{first_name}.{last_name}@example.com"
        #print(email)

        new_employee_data.append({
            "First Name": first_name,
            "Last Name": last_name,
            "SSN": ssn,
            "Email": email           
        })

print(new_employee_data)

#grab file name from original path
_ , filename = os.path.split(csvpath)
print(_)
print(csvpath)

newpath = os.path.join("output", filename)
with open(newpath, "w") as csvfile:
    field_name = ["Last Name", "First Name", "SSN", "Email"]
    writer = csv.DictWriter(csvfile, fieldnames = field_name)
    writer.writeheader()
    writer.writerows(new_employee_data)
    #OR
    #for data in new_employee_data:
        #writer.writerow(data)