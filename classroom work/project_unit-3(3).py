# 1. Write a Python program to input a string from the user and display:
# Original string, Length of the string, Data type of the variable

# a = input("enter the string")

# print (a)
# print (len(a))
# print (type(a))

# 2. Write a Python program to print the following slices of a string:
# * First 5 characters * Last 5 characters * Characters from index 3 to 10
# * Every second character * Reverse of the string

# a = input("enter the string")

# print(a[0:5:1])
# print (a[6:1:-1])
# print(a[3:10:1])
# print (a[0:10:2])
# print (a[::-1])

# 3. Write a program that counts the number of:
# * Uppercase letters * Lowercase letters * Digits * Spaces
# * Special characters in a given string.

# a = "Awesome is123 Good "

# uppercase = 0 
# Lowercase = 0 
# digits = 0 
# spaces = 0 
# specialcharacter = 0

# for i in a:
#     if (i.isupper()):
#         uppercase += 1
#     elif (i.islower()):
#         Lowercase += 1
#     elif (i.isdigit()):
#         digits += 1
#     elif (i.isspace()):
#         spaces += 1
#     elif (not i.isalpha() and i.isdigit() ):
#          specialcharacter += 1

# print (uppercase,"is the count of uppercase")
# print (Lowercase,"is the count of lowercase")
# print (digits,"is the count of digits")
# print (spaces, "is the count of spaces")
# print (specialcharacter, "is the count of special character")

# 4. Write a Python program to check whether a given string is a palindrome or not

# a = input ("enter the string")

# if (a == a[::-1]):
#     print ("palindrome")
# else:
#     print ("not palindrome")

# 5. Write a Python program to replace every space with a hyphen (`-`) using both:

# a = "awesome is good"
# a = a.replace(" ","-")
# print(a)

# 6. Write a Python program to check whether two strings are anagrams.

# a = input ("enter the fist string")
# b = input ("enter the second string")

# if (len(a)!= len(a)):
#     print ("a and b are not anagrams")

# a = sorted(a)
# b = sorted(b)

# if (a==b):
#     print ("the string is anagrams")

# 7. Write a Python program to find the frequency of each character in a string

# a = "hello dhruv"
# frequency = {}

# for char in a:
#     frequency[char] = frequency.get(char, 0) + 1

# print(frequency)

# 8. Write a Python program to input a sentence and display every word on a new line.

# a = input ("enter a sentence")

# b = a.split()
# for i in b:
#     print (i)

# 9. Write a Python program to reverse the order of words in a sentence.

# sentence = input("Enter a sentence: ")

# words = sentence.split()
# reversed_words = words[::-1]

# print("Reversed sentence:", " ".join(reversed_words))

# 10. Write a Python program to remove duplicate characters from a string.

# a = input("enter the string")
# b = ""
# for i in a:
#     if i not in b:
#         b += i
# print ("after the removing the duplicate letter",b) 

# 11. Write a Python program to find the longest word in a sentence.

# a = input("enter the sentence")

# word = a.split()

# longest_words = word[0]

# for i in word:
#     if len(i)>len(longest_words):
#         longest_words = i
# print (longest_words)

# 12. Write a Python program that performs the following operations on a given string:
# * Convert to uppercase * Convert to lowercase * Swap case
# * Remove leading/trailing spaces * Replace one word with another
# * Split into words * Join the words using a hyphen (`-`)

# a = input ("enter the string")

# b = a.upper()
# c = a.lower()
# d = a.replace(" ","")
# e = a.split()
# f = a.replace(" ","-")

# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
