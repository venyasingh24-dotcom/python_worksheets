# Worksheet-3
# Q1
# def add_numbers(a):
#     if(a>17):
#         x=(a-17)*(2)
#     else:
#         x=(17-a)
#     return x
# add_numbers(18)
# print(add_numbers(18))

# Q2
# def test_range(n):
#     if n in range(100,1000):
#         return True
#     if n in range(1000,2000):
#         return True
#     else:
#         return False
# print(test_range(200))
# print(test_range(1500))  
# print(test_range(40))
# print(test_range(3000))

# Q3
# def rev_str(s):
#     return s[::-1]
# print(rev_str("robot"))

# Q4
# def count_letters(str):
#     counts = {'uppercase': 0, 'lowercase': 0}
#     for char in str:
#         if char.isupper():
#             counts['uppercase'] += 1
#         elif char.islower():
#             counts['lowercase'] += 1
#     return counts

# name = "Venya Singh"
# count_name = count_letters(name)
# print("string:", name)
# print("Letter Counts:", count_name)

# Q5
# def unique_list(l):
#     return list(set(l))                                 
# print(unique_list([1,2,3,3,2,5,5,3,3,4,5]))

# Q6
# def even(num_list):
#     even_num = []
#     for num in num_list:
#         if num % 2 == 0:
#             even_num.append(num)
#     return even_num
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ans = even(L)
# print("Original List:", L)
# print("Even Numbers:", ans)

# Q7
# def robot():
#     def move():
#         print("Robot is moving")
#     move()
# robot()

# Q8
# def student(name, age, course):
#     return f"Name: {name}, Age: {age}, Course: {course}"
# print(student("Venya", 19, "B.Tech"))

# Q9
# def move_robot(x, y, dir):
#     if dir == "up":
#         y += 1
#     elif dir == "down":
#         y -= 1
#     elif dir == "left":
#         x -= 1
#     elif dir == "right":
#         x += 1
#     return (x, y)
# print(move_robot(0, 0, "up"))     
# print(move_robot(2, 3, "left"))   
# print(move_robot(5, 5, "down"))   
# print(move_robot(1, 1, "right"))  

# Q10
# def temp_check(temp):
#     if temp < 15:
#         return "Cold"
#     elif 15 <= temp <= 30:
#         return "Moderate"
#     else:
#         return "Hot"
# print(temp_check(10))
# print(temp_check(20))
# print(temp_check(30))
# print(temp_check(35))

# Q11
# def goal_reached(path):
#     ( x, y) = (0, 0)
#     for move in path:
#         if move == "up":
#             y += 1
#         elif move == "down":
#             y -= 1
#         elif move == "left":
#             x -= 1
#         elif move == "right":
#             x += 1
#     return (x, y) == (2, 0)
# print(goal_reached(["up", "right", "right", "down"]))

# Q12
# class Student:
#     def __init__(self, student_id, student_name, student_class):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_class = student_class
#     def display(self):
#         print("Student ID:", self.student_id)
#         print("Student Name:", self.student_name)
#         print("Student Class:", self.student_class)
# s1 = Student(1024230004, "Venya", "RAI")
# s2 = Student(102423000, "abcd", "CSE")
# s1.display()
# s2.display()

# Q13
# class Student:
#     def __init__(self, student_id, student_name, student_class):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.student_class = student_class
#     def display(self):
#         print("Student ID:", self.student_id)
#         print("Student Name:", self.student_name)
#         print("Student Class:", self.student_class)
# s1 = Student(1024230004, "Venya", "RAI")
# s2 = Student(102423000, "abcd", "CSE")
# print("Student 1 details:")
# s1.display()
# print("Student 2 details:")
# s2.display()

# Q14
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius ** 2
#     def perimeter(self):
#         return 2 * math.pi * self.radius
# c1 = Circle(5)
# c2=Circle(10)
# print("Radius 1:", c1.radius)
# print("Area 1:", c1.area())
# print("Perimeter 1:", c1.perimeter())
# print("Radius 2:", c2.radius)
# print("Area 2:", c2.area())
# print("Perimeter 2:", c2.perimeter())

# Q15
# class Capital:
#     def __init__(self):
#         self.text = ""
#     def get_String(self):
#         self.text = input("Enter a string: ")
#     def print_String(self):
#         print(self.text.upper())
# s = Capital()
# s.get_String()
# s.print_String()

# Q16
# class Robot:
#     def __init__(self, name, task, battery_level=100):
#         self.name = name
#         self.task = task
#         self.battery_level = battery_level
#     def perform_task(self):
#         if self.battery_level <= 0:
#             print(f"{self.name} has no battery left! Please recharge.")
#             return
#         print(f"{self.name} is performing task: {self.task}")
#         self.battery_level -= 10
#         if self.battery_level < 0:
#             self.battery_level = 0
#     def recharge(self):
#         self.battery_level = 100
#         print(f"{self.name} has been recharged to 100% battery.")
#     def status(self):
#         print(f"Robot Name: {self.name}")
#         print(f"Current Task: {self.task}")
#         print(f"Battery Level: {self.battery_level}%")
#         print("------------------------")
# r1 = Robot("Robot_1", "Cleaning")
# r1.status()
# r1.perform_task()
# r1.status()
# r1.perform_task()
# r1.recharge()
# r1.status()

