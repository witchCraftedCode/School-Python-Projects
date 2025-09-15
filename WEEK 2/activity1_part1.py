# ALEX FHERMAYE
# Python version 3.11.4
# Congress Age Checker

#### PART ONE ####

# 1: Variables
age = int(input("Enter Age: "))

# 2. Variables
# Using the above as a guide, complete the following line so that
# "Enter Number of years as a US Citizen: " will appear when the script is executed
citizen = int(input("Enter Number of years as a US Citizen "))

# 3. Conditional Statement
# Using the variables 'age' & 'citizen', construct a conditional statement that will check to see is the user is eligible for the Senate, House of Representatives, both or neither. To help you get started the first condition has been provided for you

if age >= 30 and citizen >= 9:
    print ("You are eligible for the Senate and the House ")
elif age >= 25 and citizen >= 7:
    print ("You are eligible for the House of Representatives.")
else:
    print ("You are ineligible to serve.")
