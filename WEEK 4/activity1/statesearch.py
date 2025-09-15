# Alex Fhermaye
# 3.11.4
# Working with Dictionaries
# State Capitol Search

# Allow for 5 Searches
# Save Results of search to state_result.txt

#########################################
# IMPORT THE STATES & CAPITOLS
#########################################

# 2. Explain why we start with an empty Dictionary
# A: we have not defined what goes in there yet. As the code runs, that dictionary will have the capitals. 
# Create Blank Dictionary
states = {}

# 3. Explain how the FOR Loop here is used to import the data
#  and separate it into KEY / VALUE pairs.
# A: the for loop imports data from the states.txt file and the states and capitals are already sepparated by a coma in this file. By using line.split it uses both sepparately.
# Import State & Capitol in the blank Dictionary
with open('states.txt', 'r') as f:
    for line in f:
        (key, val) = line.split(',')
        states[key] = val

# User must enter the name of the state to search
print ('STATE SEARCH SCRIPT')
print ('Please enter the name of 5 states to search for.')

# 4. Create a variable called count with an assigned value of 5
count = 5

##########################################
# LOOP THE SEARCH & WRITE TO EXTERNAL FILE
##########################################

# Open Report file
f= open('state_results.txt', 'w+')

# 5. Describe how the WHILE Loop uses the count variable as a control.
# A: everytime the WHILE loop runs, count is subtracted by 1 and when it reaches less than 0, the loop stops. 
# 6. How is the count variable updated?
# A: count is subtracted by 1 (count -= 1) everytime a user runs the loop
# 7. What is the effect?
# A: The count variable stops the while loop, without it, we would have an infinite loop. It also controls the amount of attemps that the user has. 
# 8. Explain how states[search] returns a value.
# A: When the user inputs a state name, the loop reaches into states.txt and pulls out the capital of the state mentioned

# Use a Loop to run search 5 times
while count > 0:
    search = input('Enter Name of State: ').title()

    # Check the Dictionary for the State / Capitol result
    if search in states:
        print ('The Capitol of ' + search + ' is ' + states[search])
        count -= 1
        print ('Remaining number of searches: ', count)
        f.write('State: ' + search + ' Capitol: ' + states[search])
    else:
        print ("You have entered an incorrect value.")

###########################################

# 9. Rewrite the LOOP SEARCH Section above (Lines 22 - 28) to utilize with open()

# 10. Test and confirm your script works before submitting to FSO!

### CHECKLIST ###
# (x) Complete the Header Comments and make sure the script executes without error.
# (x) Explain why we use an empty dictionary
# (x) Explain how the FOR Loop is used to import the external data
# (x) Create a variable called count with an assigned value of 5
# (x) Describe how the WHILE Loop uses the count variable as a control
# (x) Describe how the script updates the count variable.
# (x) What is the effect of the count variable on the script?
# (x) Explain how states[search] returns a value.
# (x) Rewrite the LOOP SEARCH section of code to utilize with open()