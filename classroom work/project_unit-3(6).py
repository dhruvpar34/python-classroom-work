# 1. Write a function greet() that prints "Welcome to Python Programming".

# def greet():
#     print("Welcome to python Programming")
# greet()
# print(greet())

# 2. Write a function square(n) that accepts a number and returns its square.

# def square(n):
#     return n*n

# print(square(3))

# 3. Write a function is_even(n) that returns True if the number is even, otherwise False.

# def is_even(n):
#     if n%2 == 0 :
#         return True
#     else:
#         return False
# print (is_even(3))

# 4. Write a function maximum(a, b) that returns the larger of two numbers.

# def maximum (a,b):
#     if a>b :
#         return a 
#     else:
#         return b 
# print(maximum(2,4))

# 5. Write a function calculate_area(radius) that calculates and returns the area of a circle.

# def calculate_area(radius):
#     a = 3.14 *radius *radius
#     return a 
# print (calculate_area(3))

# 6. Write a function calculate(a, b) that returns the sum, difference, product, and
# division of two numbers.

# def calculate(a,b):
#     sum = a + b 
#     if a>b :
#         difference = a-b
#     else :
#         difference = b-a
#     product = a*b
#     division = a/b
#     return sum,difference,product,division
# print(calculate(3,4))

# 7. Write a function student_result(marks) that accepts a list of marks and returns:
# Total marks, Average marks, Highest marks, Lowest marks

# def student_result(marks):
#     total_marks = sum(marks)
#     average_marks = total_marks / len(marks)
#     highest_marks = max(marks)
#     lowest_marks = min(marks)
#     return total_marks, average_marks, highest_marks, lowest_marks

# user_input = input("Enter the marks separated by spaces: ")
# a = tuple(map(float, user_input.split()))

# print("total marks , average marks , highest marks, lowest marks :",student_result(a))

# 8. Write a function count_vowels(text) that accepts a string and returns the number of
# vowels in it.

# def count_vowels(text):
#     a = 0 
#     for i in text:
#         if (i == "a")or (i == "e")or (i == "i")or (i == "o")or (i == "u"):
#             a += 1
#     return a
# b = input ("enter the string by space:")
# c = b.split()
# print(count_vowels(c))

# 9. Write a function reverse_number(n) that returns the reverse of a number.

# n = int(input("Enter a number: "))
# print("Reverse:", reverse_number(n))

# def reverse_number(n):
#     reverse = 0

#     while n > 0:
#         digit = n % 10
#         reverse = reverse * 10 + digit
#         n = n // 10

#     return reverse

# 10.Write a function factorial(n) that returns the factorial of a number.

# a = int (input("enter the number for the factorial :"))

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial( n - 1)

# print(factorial(a))

# 11.Write a function check_prime(n) that returns whether a number is prime or not.

# a = int(input ("enter the number :"))

# def check_prime(n):   
#     if n <= 1:
#         return False
    
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False       
#     return True  

# print(check_prime(a))

# 12.Write a function print_table(n) that prints the multiplication table of n.

# a = int(input("enter the number :"))

# def print_table(n):
#     for i in range (11):
#         print (n,"X",i,"=",i*n)

# print_table(a)

# 13.Write a function sum_of_digits(n) that returns the sum of digits of a number.

# def sum_of_digits(n):
#     b = 0
#     while n > 0 :
#         a = n%10
#         b = b + a
#         n = n // 10
#     return b   

# num = int (input ("enter the number for the sum of digits :"))
# print(sum_of_digits(num))

# 14.Write a function count_numbers(numbers) that accepts a list and returns the number
# of: Positive numbers, Negative numbers, Zeros


# a = []
# for i in range(0,3):
#     b = int(input("enter the list number :"))
#     a.append(b)


# def count_numbers(num):
#     a = 0 
#     b = 0 
#     c = 0 
#     for i in num:
#         if i > 0:
#             a += 1
#         elif i < 0 :
#             b +=0   
#         elif i == 0 :
#             c +=0
#     return a , b , c


# print("positive number , negative number, zero number = ",count_numbers(a))

# 15.Write a function get_grade(marks) that returns the grade according to:
# 90–100 → A, 80–89 → B, 70–79 → C, 60–69 → D, Below 60 → F

# marks = int(input("enter the marks :")) 

# def get_grade(marks):
#     if marks >= 90 and marks <=100:
#         print("A")
#     elif marks >= 80 and marks < 100 :
#         print("B")
#     elif marks >= 70 and marks < 100:
#         print("C")
#     elif marks >=60 and marks <100:
#         print ("D")
#     elif marks >100 :
#         print("ERROR, the given marks are greater than")
#     else:
#         print("F")

# get_grade(marks)

# 16. Student Marks Program: Create a program using separate functions: input_marks(),
# calculate_total(), calculate_average(), display_result()
# Program should accept marks of 5 subjects & display total, average and result.


# def input_marks():
#     a = []
#     for i in range (6):
#         marks = int(input("enter the marks of the subject (marks should be less than 100)"))
        
#         while marks < 0 or marks > 100:
#             print("Invalid marks! Enter marks between 0 and 100.")
#             marks = int(input("Enter the marks again: "))

#         a.append(marks)
#     display_result(a)
    
# def calculate_average(a):
#     av = 0 
#     for i in a:
#         av += i
#         c = av/ len(a)
#     return c
    
# def calculate_total(a):
#     t = 0 
#     for i in a:
#         t += i 
#     return t
    
# def display_result(a):
#     print ("average of the marks = ",calculate_average(a))
#     print("total marks = ",calculate_total(a))
    
#     if calculate_total(a) >333 :
#         print ("Result = pass")
#     else:
#         print ("Result = Fail")


# input_marks()

# 17. Simple Calculator: Organise a calculator program using separate functions: add(),
# subtract(), multiply(), divide()
# The main program should ask the user for two numbers and an operation.

# a = int (input("enter the number 1 :"))
# b = int (input("enter the number 2 :"))

# print ("1.addition")
# print ("2.subtract")
# print ("3.multiplication")
# print ("4.division")

# ch = int (input("enter the choice :"))

# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a -b 
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b

# if ch == 1:
#     print("addition of two number is :",add(a,b))
# elif ch == 2:
#     print("subtraction of two number is :",subtract(a,b))
# elif ch == 3 :
#     print ("multiplication of two number is :",multiply(a,b))
# elif ch == 4 :
#     print ("a divides b :",divide(a,b))
# else:
#     print("Error , invalid choice")

# Q-18. etricity Bill: Create a program using functions: get_units(), calculate_bill(),
# display_bill()
# Calculate electricity bill based on units consumed.

# def electricity_bill():
#     unit = int (input("enter the unit of used electricity :"))
#     return unit


# def calculate_bill(unit):
#     if units <= 100:
#         bill = units * 5
#     elif units <= 200:
#         bill = (100 * 5) + (units - 100) * 7
#     elif units <= 300:
#         bill = (100 * 5) + (100 * 7) + (units - 200) * 10
#     else:
#         bill = (100 * 5) + (100 * 7) + (100 * 10) + (units - 300) * 12
#     return bill
# def display_bill(bill,unit):
#     print("The total unit used is :",unit)
#     print("The total fee of the bill is :",bill)


# units = get_units()
# bill = calculate_bill(units)
# display_bill(units, bill)
