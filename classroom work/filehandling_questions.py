# 1. Read the first 10 characters, display the pointer position, then reset the pointer to 0 and read again.

# file = open("students.txt","w")
# a = "hello world"
# b = "I am dhruv prasad student of rd engineering college"
# file.write(a)
# file.write(b)
# file.close()

# file = open("students.txt","r")
# a = file.read(10)
# print(a)
# print(file.tell())
# file.seek(0)
# b = file.read(10)
# print(a)

# 2. Read 5 characters, skip to another position using seek(), and read the next 10 characters.

# file = open("students.txt","r")

# a = file.read(5)
# print(a)
# file.seek(8)
# b = file.read(10)
# print(b)
# file.close()


# 3. Demonstrate what happens when read() is called twice without using seek().

# file = open("students.txt","r")

# print(file.read())
# print(file.read())#blank space in the after words are finished. 
# file.close()


# 4. Display the pointer position after every readline() operation.

# file = open("students.txt","r")

# print(file.readline())
# print(file.tell())
# print(file.readline())
# print(file.tell())

# file.close()

# 5. Read the complete file, reset the pointer using seek(0), and read only the first line.

# file = open("students.txt","r")

# print(file.read())
# print(file.seek(0))
# print(file.readline())
# file.close()

# 6. Create a program that uses tell() to report the pointer position before and after reading.

# file = open("students.txt","r")
# print(file.tell())
# print(file.read())
# print(file.tell())
# file.close()

# 7. Read a text file and create another file containing only lines that contain the word Python.

# with open("students.txt","r+") as f :
#     print(f.read())
#     new = open("new.txt","w")
#     new.write("Python")
#     new.close()


# 8. Read a file and create a second file with all lines converted to uppercase.

# with open("students.txt", "r") as file:
#     a = file.read()
#     print(a)

# with open("STUDENTS.txt", "w+") as F:
#     a = a.upper()
#     F.write(a)

#     F.seek(0)
#     print(F.read())

# 9. Read a file and write its lines in reverse order to another file.


# with open("students.txt", "w") as f:
#     f.write("Hello\n")
#     f.write("I am Dhruv\n")
#     f.write("I am learning Python")

# with open("students.txt", "r") as f:
#     a = f.readlines()

# with open("new1.txt", "w") as r:
#     for line in a[::-1]:
#         r.write(line)


# 10. Count the frequency of each word in a tex

# with open("students.txt", "r") as f:
#     text = f.read()

# words = text.lower().split()

# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# for word, count in frequency.items():
#     print(word, ":", count)

    

# 11. Find the longest line in a file.

# with open("students.txt","r")as f :
#     a = f.readlines()

# longest = ""

# for i in a:
#     if len(i)>len(longest):
#         longest = i 

# print("longest line :",longest)


# 12. Find the shortest line in a file.

# with open("students.txt","r")as f:
#     a = f.readlines()
#     print(a)

# shortest = None

# for i in a :

#     a = i.rstrip("\n")

#     if shortest is None or len(i) < len(shortest):
#         shortest = i

# print("shortest line :",shortest)

# 13. Remove blank lines from a file and save the result to a new file.


# with open("students.txt", "r") as f:
#     a = f.readlines()

# with open("newfile.txt", "w") as f:
#     for line in a:
#         if line.strip():
#             f.write(line)

# print("Blank lines removed successfully!")

# 14. Merge two text files into a third file.

# with open("students.txt","r") as f:
#     a = f.read()

# with open("new.txt","r")as F:
#     b = F.read()

# with open("new1.txt","w+")as file:
#     file.write(a)
#     file.write("\n")
#     file.write(b)

# 15. Separate even and odd numbers stored in a file into two different files.

# with open("number.txt","w")as file:
#     file.write("1")
#     file.write("\n")
#     file.write("2")
#     file.write("\n")
#     file.write("52")
#     file.write("\n")
#     file.write("36")
#     file.write("\n")    
#     file.write("58")
#     file.write("\n")
#     file.write("88")

# with open("number.txt", "r") as f:
#     number = f.read().split()

# with open("even.txt", "w") as e, open("odd.txt", "w") as o:
#     for num in number:
#         num = int(num)

#         if num % 2 == 0:
#             e.write(str(num) + "\n")
#         else:
#             o.write(str(num) + "\n")

# print("Even and odd numbers separated successfully!")


# 16. Read a student marks file and calculate average marks.

# with open("marks.txt","w")as f :
#     f.write("85")
#     f.write("\n")
#     f.write("95")
#     f.write("\n")
#     f.write("25")
#     f.write("\n")
#     f.write("23")
#     f.write("\n")
#     f.write("66")
#     f.write("\n")
#     f.write("45")
#     f.write("\n")
#     f.write("40")


# with open("marks.txt", "r") as f:
#     marks = f.read().split()

# total = 0

# for mark in marks:
#     total += int(mark)

# average = total / len(marks)

# print("Average marks:", average)
