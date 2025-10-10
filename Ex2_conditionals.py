# -------------------------------------------
# Exercise 2: Conditional Statements
# -------------------------------------------
# Learning Objective:
# Learn to use conditional statements in Python, practise pair programming,
# and apply basic Git commands in a team workflow.

# Pair Programming Roles:
# - One person is the "Driver" (types), the other(s) is the "Navigator" (guides).
# - Switch roles and computers after each step.
# - Before switching, commit and push your code.
# - After switching, the new Driver must pull the latest version.

# Key Python Terms:
# - if    : begins a condition block
# - elif  : checks another condition if the previous ones are false
# - else  : runs only if all previous conditions are false

# -------------------------------------------
# Step 1: Using a Simple if Statement
# -------------------------------------------
# Task 1:
# - Create a variable called `number` and assign it a value.
#   Try several examples: a positive number, a negative number, and zero.

# Task 2:
# - Write an if statement that checks if the number is greater than 0.
#   If it is, print: "The number is positive."

# Task 3:
# - Add a second if statement to check if the number is even.
#   If it is, print: "The number is even."

# Task 4:
# - Test with different values. What messages appear for each?

# Write your Step 1 code below:

# Dominic I hope you don't mind but I've just tidied up the code a bit
# I added the Steps each part of the code refers to and put some spacing
# in as well. I hope this is ok? Cheers Darren

#1
number = 6888546
#2
print()
print("Step 1")
if number > 0: 
    print("The number is positive.")
else:
    print("The number is zero or negative.")
print()
#3
if number %2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
print()



# ---- GIT STEP ----
# 1. Save your work.
# 2. In the terminal, run:
#    git add Ex2_conditionals.py
#    git commit -m "Step 1 complete"
#    git push origin main
# 3. SWITCH computers and roles.
# 4. On the new computer, run:
#    git pull origin main

# -------------------------------------------
# Step 2: Adding else and Practising Boolean Logic
# -------------------------------------------
# Task 1:
# - Add an else block to the "greater than 0" check.
#   If false, print: "The number is zero or negative."

# Task 2:
# - Add an else to the even/odd check.
#   If it's not even, print: "The number is odd."

# Task 3:
# - Add a new condition using `and`:
#     - If the number is divisible by both 2 and 3, print: "Divisible by 2 and 3."
#     - Otherwise, print: "Not divisible by both."

# Task 4:
# - Try using the `or` operator to check if divisible by either 2 or 3.

# Write your Step 2 code below:

#3
print("Step 2")
if number %2 ==0 and number %3 ==0:
    print("Divisible by 2 and 3.")
else:
    print("Not divisible by both")

print()
#Code added by Darren
#4
if number %2 ==0 or number %3 ==0:
    print("Divisible by 2 and 3.")
else:
    print("Not divisible by both")
print()

# ---- GIT STEP ----
# 1. Save your work.
# 2. Run:
#    git add Ex2_conditionals.py
#    git commit -m "Step 2 complete"
#    git push origin main
# 3. SWITCH computers and roles.
# 4. On the new computer, run:
#    git pull origin main

# -------------------------------------------
# Step 3: Using if - elif - else
# -------------------------------------------
# Task 1:
# - Replace your previous if-else structure with if - elif - else.
# - Check three cases:
#     1. Number is positive
#     2. Number is zero
#     3. Number is negative

# Task 2:
# - Add another elif condition:
#     - If the number is greater than 100, print: "That's a large number!"

# Task 3:
# - If the number is between 1 and 10 (inclusive), print: "A small positive number."
# This condition cannot be met without changing the first if statement!
# As soon as you put 1 or above it satisfies the condition and ignores
# the rest of the elif conditions.

# Task 4:
# - Test with different values. Try to hit every condition.

# Darrens Code
# Write your Step 3 code below:
print("Step 3")
print()
if number > 0 and number > 10 and number < 100:
    print("The number is positive.")
elif number ==0:
    print("The number is 0")
elif number > 100:
    print("That's a large number!")
elif number >= 1 and number <= 10:
    print("A small positive number.")
else:
    print("The number is negative.")
print()

# ---- GIT STEP ----
# 1. Save your work.
# 2. Run:
#    git add Ex2_conditionals.py
#    git commit -m "Step 3 complete"
#    git push origin main
# 3. SWITCH computers and roles.
# 4. On the new computer, run:
#    git pull origin main

# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# Continue rotating after each activity. Use Git to sync between each.

# Extension 1: Interactive Number Check
# -------------------------------------
# - Ask the user to enter a number.
# - Use if-elif-else to check if it’s positive, negative, or zero.
# - Then, also check if it’s even or odd.
# - Print a message such as: "The number is positive and even."

# Write Extension 1 code below:
# Darrens code
print()
print("Extension 1")
print()
number = int(input ("Choose a whole number "))
if number == 0:
    print("The number is 0!")
elif number < 0:
    print("The number is negative!")
elif number %2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")
print()

# ---- GIT STEP (after completing this extension) ----
# git add Ex2_conditionals.py
# git commit -m "Completed Extension 1"
# git push origin main
# Switch machines and git pull

# Extension 2: Age Group Checker
# ------------------------------
# - Ask the user to input their age.
# - Print a message depending on the age group:
#     - Under 13 → "You are a child."
#     - 13 to 17 → "You are a teenager."
#     - 18 to 64 → "You are an adult."
#     - 65 or older → "You are a senior."

# Write Extension 2 code below:
# Darrens code
print()
print("Extension 2")
print()
age = int(input("What is your age? "))
if age <=12:
    print("You are a child and probably wish you were a teenager!")
elif age >=13 and age <= 17:
    print("You're a teenager and probably wish you were an adult!")
elif age >=18 and age <= 64:
    print("You are an adult and probably wish you were a teenager again!")
else:
    print("You're a senior and probably wish you were a child again!")
print()


# ---- GIT STEP ----
# git add Ex2_conditionals.py
# git commit -m "Completed Extension 2"
# git push origin main
# Switch machines and git pull

# Extension 3 (Challenge): Login System
# -------------------------------------
# - Set two variables for the correct username and password.
# - Ask the user to enter both.
# - Use if-elif-else to:
#     - Check if both are correct → print "Login successful!"
#     - Username correct but password wrong → print "Incorrect password."
#     - Username incorrect → print "Username not found."

# Bonus:
# - Add an attempt limit (max 3 tries).
# - Use nested if statements if you like.

# Write Extension 3 code below:
# Darrens code
print()
print("Extension 3")
print()
attempts = 0
max_attempts = 3
user = 1234
password = "Fido123"
while attempts < max_attempts:
    username =int(input("Enter your username "))
    Pass = input("Enter your password ")
if username == user and Pass == password:
    print("Login successful!")
    break
if username != user:
    print("Username not found.")
elif Pass != password:
    print("Password incorrect")
attempts += 1
print(f"Attempts left: {max_attempts-attempts}")
if attempts==max_attempts:
    print("Too many attempts account locked.")
print()
# Dom I can't figure out how to structure the number of tries! I understand I need to set
# a variable for total tries such as total_tries = 3 and a way to increase the attempt
# count by +1 each time. Its the loop back I'm struggling with for example if you enter
# an incorrect username how do I loop back to the input commands while increasing the tries by 1? 
# I can't figure it out. Maybe you'll have more success.
# 
# ---- GIT STEP ----
# git add Ex2_conditionals.py
# git commit -m "Completed Extension 3"
# git push origin main
# Switch machines and git pull

# -------------------------------------------
# FINAL SUBMISSION
# -------------------------------------------
# Once your team has completed all required sections:
# 1. Make sure your last set of changes has been committed and pushed.
# 2. Check GitHub to confirm the latest code is there.
# 3. Celebrate completing your collaborative conditional statements exercise.
# -------------------------------------------
