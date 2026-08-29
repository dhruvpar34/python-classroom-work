# Q1. Write a Python program to input a number and determine whether it is
# positive, negative or zero.

# a = int (input("enter the number"))

# if a>0:
#     print("positive")
# elif a<0:
#     print("negative")
# else:
#     print("zero")

# Q2. Write a program to check whether a given integer is even or odd.

# a = int(input("enter the nuber"))

# if a%2==0:
#     print("even")
# else:
#     print("odd")

# Q3. WAP to input 3 numbers and print largest among them using if-elif-else.

# a = int (input("enter the number"))
# b = int (input("enter the number"))
# c = int (input("enter the number"))

# if (a>b)and(a>c):
#     print("the largest number is :",a)
# elif (b>a)and(b>c):
#     print("the largest number is:",b)
# else:
#     print("the largest number is:",c)

# Q4. Write a program to input marks (0–100) and display the grade:
# A (90–100), B (75–89), C (60–74), D (40–59), Fail (<40)

# a = int (input("enter the marks (0-100)"))

# if (a<100)and(a>=90):
#     print("A")
# elif (a>=75)and(a<=89):
#     print("B")
# elif (a>=60)and(a<=74):
#     print("C")
# elif (a>=40)and(a<=59):
#     print("D")
# else:
#     print("Fail")

# Q5. Write a program to determine whether a given year is a leap year.

# a = int (input("enter the year"))

# if ((a%4 ==0 )and(a%100 != 0))or (a%400 == 0 ):
#     print("the entered year is a leap year")
# else:
#     print("the entered year is not a leap year")

# Q6. Write a program that allows withdrawal from ATM only if: PIN is correct,
# Account balance is sufficient. Otherwise, display the appropriate message.

# pin = 2007
# balance = 20000
# a = int(input("enter the pin"))

# if a == pin :
#     b = int (input("enter the amount you want to withdrawle :"))
#     if (b>balance):
#         print("the amount in the account is not sufficient")
#     elif (b==0):
#         print ("you can't enter withdrawle amount zero")
#     else :
#         print("The withdrawl is succesfull ")
# else:
#     print("the entered pin is wrong")


# Q7. A student is eligible for a scholarship only if: Marks ≥ 85, Attendance ≥
# 75%. Write a program to check eligibility.

# a = int (input ("enter the marks"))
# b = int (input("enter the attendance percentage"))
# if (a>=85) and (b>=75):
#     print ("you are eligible for the scholarship")
# else:
#     print("you are not eligible for the scholarship")

# Q8. Calculate electricity bill using following slabs: Up to 100 units: ₹5/unit,
# 101–300 units: ₹7/unit, Above 300 units: ₹10/unit

# a = int (input ("enter the electricity unit"))

# if (a>0)and(a<=100):
#     b = a*5
# elif (a>=101)and(a<=300):
#     b = a*7
# else:
#     b = a*10

# print ("The amount you need to pay is : ₹",b)

# Q9. WAP that performs Addition, Subtraction, Multiplication, or Division based
# on the user's choice using if-elif-else.

# a = int (input("enter the first number"))
# b = int (input("enter the second number"))

# c = input ("enter '+' for the addition , '-' for the subtraction ,'*' for the multiplication ,'/' for the division ")

# if c== "+":
#     print("The addition is :",a+b)
# elif c == "-":
#     print("The subtraction is :",a-b)
# elif c == "*":
#     print("The multiplication is :",a*b)
# elif c == "/" :
#     print ("The division is :", a/b)
# else:
#     print("[ERROR]")



# Q10. WAP to validate a user's username and password. If both are correct,
# display "Login Successful"; otherwise, display "Invalid Username or
# Password."

# username = "Dhruv@2007"
# password = 2344

# a = input("enter the username")
# if (a == username):
#     b = int (input("enter the password"))
#     if (b == password):
#         print ("login successful")
#     else:
#         print("password is worng")
# else:
#     print ("the username is worng")