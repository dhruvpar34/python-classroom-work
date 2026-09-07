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

