#Created 25 July 2020 in Python

from datetime import date

print("WELCOME TO THE BAR")
name = input("What is your name: ")
age = int(input("What is your age?: "))

today = date.today()
year = str(today.year - age + 21)

if age < 21:
    print(name + ", You are not old enough to enter this bar. Please come see us again after you turn 18 in the year " +
          year + ".")
elif age == 21:
    print(name + ", You have recently turned 21. Congratulations and come on in!")
else:
    print(name + ", You are over the age of 21. Come on in and have a Budweiser! You turned 21 in the year " + year +
          ".")
