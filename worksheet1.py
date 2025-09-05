# worksheet-1
# Q1
# print("Twinkle, twinkle, little star, How I wonder what you are!\nUp above the world so high, Like a diamond in the sky.\nTwinkle, twinkle, little star, How I wonder what you are")

# Q2
# first= input("enter the first name: ")
# last= input("enter the last name: ")
# print(last + " " + first)

# Q3
# radius= int(input("the radius of the circle is: "))
# area= 3.14*radius*radius
# print("area of circle is: ", area)

# Q4
# color_list = ["Red","Green","White" ,"Black"]
# print("first color is ",color_list[0])
# print("last color is ",color_list[3])

# Q5
# n=int(input("value of n is: "))
# print(n+(n*n)+(n*n*n))

# Q6
# num=input("enter the number: ")
# num_list=num.split(",")
# num_tuple=tuple(num_list)
# print("list: ",num_list)
# print("tuple: ",num_tuple)

# Q7
# c=int(input("temp in celcius is "))
# f=(((9*c)/5)+32)
# print("temp in farhenheit is ",f)

# Q8
# x=int(input("first number "))
# y=int(input("second number "))
# x,y=y,x
# print("after swapping, fisrt number ",x)
# print("second number ",y)
# x=x+1
# print(x)

# Q9
# num=int(input("enter the number "))
# if num%2==0:
#     print("number is even")
# else:
#     print("number is odd")

# Q10
# year=int(input("enter the year "))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("leap year")
# else:
#     print("not leap year")

# Q11
# x1=int(input("x1= "))
# x2=int(input("x2= "))
# y1=int(input("y1= "))
# y2=int(input("y2= "))
# z1=int(input("z1= "))
# z2=int(input("z2= "))
# E=((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
# print("euclidean distance is ",E)

# Q12
# angle1=int(input("first angle is: "))
# angle2=int(input("second angle is: "))
# angle3=int(input("third angle is: "))
# if angle1+angle2+angle3==180:
#     print("it is a triangle")
# else:
#     print("it is not a triangle")

# Q13
# P=int(input("principal= "))
# r=int(input("rate= "))
# t=int(input("time period= "))
# A=(P*(1+(r/100))**t)-P
# print("compound interest= ",A)

# Q14
# N=int(input("number is "))
# a=0
# if N<=1:
#     print("the number is not prime")
# else:
#     for i in range (2,N):
#         if N%i==0:
#             a=1
#     if a==1:
#      print("not a prime number ")
#     else :
#      print("prime number")

# Q15
# n= int(input("value of n is= "))
# if n>1:
#     x=(n*(n+1)*((2*n)+1))/6
#     print("sum of squares of n numbers is ",x)
# else:
#     print("enter a positive value")
