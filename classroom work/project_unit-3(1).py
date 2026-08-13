# Q-1 
# a = ["spiderman","iron man","joker","king kong","lion king"]

# print (a)
# print (type(a))

# Q-2

# a = [1,2,3,4,5,6,7,8,9]

# print (a[0],a[8],a[1],a[2],a[3],a[4],a[5],a[6],a[7])

# Q-3

# a = ["america","iceland","korea","japan","south_korea","india"]
# print(a[::-1])

# Q-4

# a = [0,1,2,3,4]
# b=[5,6,7,8,9]

# c = a+b
# print(c)

# Q-5

# a = [1,2,3,4,5,6]

# print(a,a,a,sep="\n")

# Q-6

# a = ["apple","grapes","orange","liche","mango"]

# a.append('banana')
# a[1]="red"
# print(a)

# Q-7

# a = [0,1,2,3,4]
# b=[5,6,7,8,9]

# a.extend(b)
# print (a)
# a.remove(a[9])
# print(a)

# Q-8

# a = [0,1,2,3,4,5,6,7,8,9]

# del(a[2])
# print (a)

# del(a)
# print(a)

# Q-9 

# a = [0,1,8,9,5,6,7,2,3,4]

# a.sort()
# print(a)
# a.sort(reverse=True)
# print (a)

# Q-10

# a = [0,1,2,3,4,5,6,7,8,9]
# a.reverse()

# print(a)

# Q-11

# a = [0,1,2,3,4,5,6,7,8,9]
# b=a.copy()

# print (a,b,sep="\n")

# Q-12

# a = [0,1,2,3,9,4,5,9,6,7,9]

# print(a.count(9))

# Q-13

# a = [0,1,2,3,8,4,5,6,7,9]

# # finding the 8 which is at index 4
# print(a.index(8))

# Q-14

# a = [
#     [0,1,2] 
#     ,[3,4,5]
#     ,[6,7,8] 
#     ]
# for row in a:
#     print(*row) 