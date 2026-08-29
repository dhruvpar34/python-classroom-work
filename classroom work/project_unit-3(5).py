# 1. Write program to add following elements to an existing set: 25,35,45. Print new set.

# a = {25,35,45}

# a.add(12)

# print (a)

# 2. Write a Python program to remove elements from a set using:
# `remove()`, `discard()`, `pop()` Display the set after each operation

# a = {12,25,32,55}

# a.remove(12)
# print(a)
# a.pop()
# print(a)

# a.discard(22)
# print(a)

# 3. Write a Python program to create two sets and perform the following operations:
# Union, Intersection, Difference, Symmetric Difference. Display result of each operation.

# a = {12,22,25,44,35}
# b = {23,34,55,56,76,22,55}

# c = a.union(b)
# print("The union of the two set are:")
# print(c)

# d = a.intersection(b)
# print("the intersect of the two set are:")
# print(d)

# e = a.difference(b)
# print ("the difference of the two sets are:")
# print(e)

# f = a.symmetric_difference(b)
# print ("the symmertric difference of the two sets are :")
# print (f)



# 4. Write a Python program to determine whether two sets are disjoint.

# a = {12,34,35,55,76}
# b = {33,45,38,98,89}

# if a.isdisjoint(b):
#     print ("the sets are disjoint")
# else:
#     print ("the sets are not disjoint")

# 5. Write a Python program to remove duplicate values from the list using a set.

# a = {12,34,55,56,78,12}
# print(a)

# 6. Write a Python program to find the common subjects chosen by two students.
# Example: Student1 = {"Python","Java","SQL","Excel"}
# Student2 = {"Python","C","Excel","Power BI"} Display common subjects.

# Student1 = {"Python","Java","SQL","Excel"}
# Student2 = {"Python","C","Excel","Power BI"}

# a = Student1.intersection(Student2)
# print("the common subject between two student are:")
# print(a)

# 15. A college has two clubs:
Science_Club = {"Aman","Riya","Rahul","Priya","Ankit"}
Coding_Club = {"Rahul","Ankit","Simran","Rohit","Riya"}

# 1. Display all students enrolled in either club.

# a = Science_Club.union(Coding_Club)
# print(a)

# 2. Display students enrolled in both clubs.

# b = Science_Club.intersection(Coding_Club)
# print(b)

# 3. Display students only in the Science Club.

# c = Science_Club.difference(Coding_Club)
# print(c)

# 4. Display students only in the Coding Club.

# d = Coding_Club.difference(Science_Club)
# print(d)

# 5. Check whether the two clubs have any common members.

# e = Science_Club.intersection(Coding_Club)
# print(e)

# 6. Add a new student to the Coding Club.
# Coding_Club.add("Dhruv")
# print("coding club")
# print(Coding_Club)

# 7. Remove one student from the Science Club.

# g = Science_Club.remove("Rahul")
# print(g)

# 8. Print the updated sets.

# print(Science_Club)
# print(Coding_Club)