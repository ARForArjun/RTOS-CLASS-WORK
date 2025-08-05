1. Write a program to take name and age as input and print a greeting. 

name=input("enter your name:")
age=int(input("enter your age:"))
print(f"Hai, {name}, It's great to know you are {age} years old.")

2. Write a program to print even numbers from 1 to 20.

for number in range(1,21):
  if number%2==0:
    print(number)

3. Write a function to return factorial of a number.

  def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
i=int(input("enter the number:"))
print(factorial_iterative(i))

4. Store and display marks of 5 students.
student={}
for i in range(5):
  name=input(f"Enter the name of the student {i+1} :")
  mark=int(input(f"Enter the mark of {name} :"))
  student[name]=mark
print("mark list of students:")
for name,mark in student.items():
  print (f"{name}:{mark}")

5. Write a program to take 5 student names and marks, store in a dictionary, and print topper’s name
student={}
for i in range(5):
  name=input(f"Enter the name of the student {i+1} :")
  mark=int(input(f"Enter the mark of {name} :"))
  student[name]=mark
print("mark list of students:")
for name,mark in student.items():
  print (f"{name}:{mark}")
topper_name = max(student, key=student.get)
topper_marks = student[topper_name]
print(f"\nTopper: {topper_name} with {topper_marks} marks")
  


  
