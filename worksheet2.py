# Worksheet-2
# Q1
# L=[11,12,13,14,24,22,25,27]
# L=[1,2,3,4]
# (i)
# x=[50,60]
# L.extend(x)
# print(L)

# (ii)
# L.remove(11)
# L.remove(13)
# print(L)

# (iii)
# L.sort()
# print(L)

# (iv)
# L.sort(reverse=True)
# print(L)

# (v)
# y= 13 in L
# print(y)

# (vi)
# print(L.count)

# (vii)
# print(sum(L))

# (viii)
# odd_sum=0
# for i in L:
#     if i%2!=0:
#         odd_sum=odd_sum+i
# print(odd_sum)

# (ix)
# even_sum=0
# for i in L:
#     if i%2==0:
#         even_sum=even_sum+i
# print(even_sum)

# (x)
# sum_prime=0
# for i in L:
#     prime=True
# for j in range (2,i):
#     if i%j==0:
#         prime=False
#         break
#     if prime:
#         sum_prime=sum_prime+i
#         print(sum_prime)

# (xi)
# print(L.clear())

# (xii)
# del L

# Q2
# sum=0
# for i in L:
#     sum= sum+i
# print(sum)
    
# Q3
# pdt=1
# for i in L:
#     pdt=pdt*i
# print(pdt)

# Q4
# array = [[['*' for k in range(6)] for j in range(3)] for i in range(4)]
# for i in array:
#     print(i)

# Q5
# D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# (i)
# D.update({8:8.8})
# print(D)

# (ii)
# D.pop(2)
# print(D)

# (iii)
# print(D.get(6))

# (iv)
# print(len(D))

# (v)
# print(sum(D.values()))

# (vi)
# D.update({3:7.1})
# print(D)

# (vii)
# D.clear()
# print(D)

#Q6
# S1 = {10, 20, 30, 40, 50, 60}
# S2 = {40, 50, 60, 70, 80, 90}

# (i) 
# S1.update([55, 66])
# print(S1)

# (ii) 
# S1.discard(10)
# S1.discard(30)
# print(S1)

# (iii) 
# print("Is 40 present?", 40 in S1)

# (iv)
# print("Union:", S1 | S2)

# (v) 
# print("Intersection:", S1 & S2)

# (vi)
# print(S1 - S2)

# Q7
# (i)

# import random

# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# for i in range(100):
#     length = random.randint(6, 8)
#     s = ''.join(letters[random.randint(0, len(letters)-1)] for _ in range(length))
#     print(s)

# q7 
# (ii)

# def prime(N):
#     a=0
#     if N<=1:
#         print("the number is not prime")
#     else:
#         for i in range (2,N):
#             if N%i==0:
#              a=1
#     return a

# for num in range(600, 801):
#     if prime(num)==0:
#         print(num)

# Q7
# (iii)

# for i in range(100,1000):
#     if i%7==0 and i%9==0:
#         print(i)

# Q8 

# exam_dates = (
#     (11, 12, 2025),
#     (13, 12, 2025),
#     (15, 12, 2025),
#     (17, 12, 2025),
#     (19, 12, 2025)
# )

# subjects = ["Python", "DS", "EDP", "Mechanincs", "TOM"]

# for i in range(5):
#     d, m, y = exam_dates[i]
#     print(f"{subjects[i]} exam will start from: {d} / {m} / {y}")


# Q9

# l= [10, 23, 45, 66, 75, 90, 101, 120]

# for i in l:
#     if i % 5 == 0:
#         print(i)

# Q10

# num = int(input("Enter a number: "))
# is_even = (num % 2 == 0)
# if is_even:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is Odd")

# Q11

# text = "Emma is a good developer. Emma also loves Python. Emma is learning AI."
# count = text.count("Emma")
# print(f"The substring 'Emma' appears {count} times.")

# Q12

# list1 = [10, 21, 33, 40, 55, 60, 77]
# list2 = [12, 25, 36, 49, 50, 63, 72]
# new_list = []
# for i in list1:
#     if i % 2 != 0:
#         new_list.append(i)

# for i in list2:
#     if i % 2 == 0:
#         new_list.append(i)

# print("New list:", new_list)

# Q13

# positions = [(2,3), (4,5), (6,7), (7,8)]
# even_positions = []

# for i in positions:
#     if i[0] % 2 == 0:   # check x-coordinate (first element)
#         even_positions.append(i)

# print("Positions with even x-coordinate:", even_positions)

# Q14

# sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
# high_readings = []
# for sensor_id, reading in sensor_data.items():
#     if reading > 3.0:
#         high_readings.append(sensor_id)
# print("Sensor IDs with readings above 3.0:", high_readings)

# Q15

# commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
# commands_executed = {"MOVE", "TURN_LEFT", "STOP"}
# not_executed = commands_received - commands_executed

# print("Commands not executed:", not_executed)


