# 1. Create a dictionary containing details of an employee. Print Employee Name,
# Department, Salary, Designation by accessing the values using their keys.

# a = {1:("dhruv","it",20000,"ghaziabad"),2:("yash","ds",15000,"ghaziabad")}

# print(a[1])
# print (a[2])

# employee = {
#     "Name": "Dhruv",
#     "Department": "IT",
#     "Salary": 50000,
#     "Designation": "Software Developer"
# }

# print("Employee Name:", employee["Name"])
# print("Department:", employee["Department"])
# print("Salary:", employee["Salary"])
# print("Designation:", employee["Designation"])


# 2. Write a program to add the following new key-value pairs to an existing dictionary:
# * Email * Phone Number. Print the updated dictionary.


# employee = {
#     "Name": "Dhruv",
#     "Department": "IT",
#     "Salary": 50000,
#     "Designation": "Software Developer"
# }

# employee["email"]= "dhruvpar34@gmail.com"
# employee["mobile number"]= 9650864128

# print(employee)

# 3. Write a program to update the salary of an employee stored in a dictionary.
# Example: Before: {'Name':'Amit','Salary':45000}
# After: {'Name':'Amit','Salary':52000}

# a = {1:{"name":"dhruv","salary":45000}}
# a[1]["salary"]= 52000

# print(a)

# 4. Write a Python program to remove: * specific key * last inserted item
# Display the dictionary after each operation.

# a = {1:"dhruv",2:"yash",3:"lavish"}

# a.pop(2)
# print(a)
# a[4] = "hello"
# print(a)


# 5. Given the dictionary: student = {"Roll":101,"Name":"Rahul","Branch":"CSE", "Sem":5}
# Write a program to: * Print all keys, all values and all key-value pairs.

# student = {"Roll":101,"Name":"Rahul","Branch":"CSE", "Sem":5}

# print(student.keys())
# print(student.values())
# print(student.items())


# 6. Write a Python program to check whether a given key exists in a dictionary.
# Example: Input Key: Name Output: Key Found
# Otherwise display: Key Not Found

# a = {1:"dhruv",2:"yash",3:"lavish"}

# b = int(input("enter the key"))

# if b not in (a.keys()):
#     print("key not found")
# else:
#     print("key found")

# 7. Write a program to count the total number of key-value pair

# a = {1:"dhruv",2:"yash",3:"lavish"}

# print ("total number of key-value pair",len(a))

# 8. Write a Python program to create a dictionary from the following two lists.
# keys = ["ID","Name","Age","City"]
# values = [101,"Ankit",20,"Delhi"]
# Expected Output: {'ID':101,'Name':'Ankit','Age':20,'City':'Delhi’}

# a = {"ID":101,"Name":"Ankit","Age":20,"City":"Delhi"}
# print(a)


# 9. Create a nested dictionary to store details of three students. Each student should
# have: Name, Branch, Semester, CGPA
# Print the complete nested dictionary.

# students = {"student1":{"name":"dhruv","branch":"cse","semester":3,"cgpa":7},"student2":{"name":"yash","branch":"cse","semester":3,"cgpa":4}}
# print(students)


# 10. Using the nested dictionary created in Question 11, print only:
# * Name of Student 2 * Branch of Student 3 * CGPA of Student 1

# students = {"Student1": {"Name": "Rahul","Branch": "CSE","CGPA": 8.5},
#             "Student2": {"Name": "Aman","Branch": "ECE","CGPA": 8.2},
#             "Student3": {"Name": "Riya","Branch": "IT","CGPA": 9.0}}

# print("Name of Student 2:", students["Student2"]["Name"])
# print("Branch of Student 3:", students["Student3"]["Branch"])
# print("CGPA of Student 1:", students["Student1"]["CGPA"])

# 11. Create the nested dictionary for each department of RDEC. Department should
# contain: HOD Name, Number of Faculty, Number of Students
# Then write statements to:
# 1. Print the HOD of the ECE department.
# 2. Print the number of students in the CSE department.
# 3. Update the faculty count of the ME department.
# 4. Add a new department named Civil.
# 5. Print all department names.
# 6. Print the complete nested dictionary.

# 11. Nested dictionary for each department of RDEC

# departments = { "CSE": {"HOD Name": "Dr. Amit Sharma","Number of Faculty": 25,"Number of Students": 500},
#     "ECE": {"HOD Name": "Dr. Neha Gupta","Number of Faculty": 20,"Number of Students": 400},
#     "ME": {"HOD Name": "Dr. Rajesh Kumar","Number of Faculty": 15,"Number of Students": 300}}

# print("HOD of ECE:", departments["ECE"]["HOD Name"])

# print("Number of students in CSE:", departments["CSE"]["Number of Students"])

# departments["ME"]["Number of Faculty"] = 18


# departments["Civil"] = {
#     "HOD Name": "Dr. Suresh Verma",
#     "Number of Faculty": 12,
#     "Number of Students": 250
# }


# print("Department Names:")
# for department in departments:
#     print(department)

# print("Complete Nested Dictionary:")
# print(departments)