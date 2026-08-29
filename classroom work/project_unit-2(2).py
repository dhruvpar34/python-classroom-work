# 1. To calculate average of first n natural numbers. Where n is to be entered by the user.

# n = int(input("Enter the value of n: "))

# average = (n + 1) / 2

# print("Average of first", n, "natural numbers is:", average)

# 2. To print the multiplication table of n. where n is to be entered by the user.

# a = int (input("enter the number for the table"))
# for i in range(11):
#     print(a,"x",i,"=",a*i)
# print ("complete")

# 3. To calculate the factorial of n.

# a = int (input("enter the number for the factorial"))
# b = 1

# for i in range(1,a+1):
#     b = b*i
# print ("the factorial is",b)

# 4. To calculate the power(x,n).

# x = int(input("Enter the value of x: "))
# n = int(input("Enter the value of n: "))

# power = x ** n

# print(x, "raised to the power", n, "is:", power)

# 5. To sum the series ---- 1+1/2+1/3+1/4+……..+1/n

# a = int(input("Enter the value of n: "))

# sum = 0

# for i in range(1, a + 1):
#     sum = sum + 1 / i

# print("Sum of the series is:", sum)

# 6. To generate the calendar of a month given the start day and no of days in the month.

# start_day = int(input("Enter the starting day (1=Monday, 7=Sunday): "))
# days = int(input("Enter the number of days in the month: "))

# print("\nMon Tue Wed Thu Fri Sat Sun")

# # Print spaces before the first day
# for i in range(1, start_day):
#     print("    ", end="")

# # Print the days of the month
# for day in range(1, days + 1):
#     print(f"{day:3}", end=" ")

#     if (day + start_day - 1) % 7 == 0:
#         print()

## Q-7

# #(i)
# for i in range(6):
#     for j in range(i):
#         print("*",end=" ")
#     print( )

#(ii)

# for i in range(6):
#     for j in range(i):
#         print(j+1,end=" ")
#     print( )

#(iii)

# for i in range(1, 6):
#     print(str(i) * i)

#(iv)

# print("0\n12\n345\n6789")

#(v)

# # Loop from 1 to 4
# for i in range(1,6):
#     # Calculate spaces (5 - i)
#     spaces = " " * (6 - i)
    
#     # Generate numbers from 1 up to i, separated by spaces
#     numbers = " ".join(str(num) for num in range(1, i + 1))
    
#     # Print the combination
#     print(spaces + numbers)

