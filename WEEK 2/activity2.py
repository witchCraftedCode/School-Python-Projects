# ALEX FHERMAYE
# Python version 3.11.4
# Troubleshooting

#### PART ONE #### 
# Troubleshooting

### Fixed Code ###

# zoo = ['Lion', 'Zebra', 'Giraffe', 'Hippo']

# for animal in zoo:
#     if animal == 'Lion':
#         print("Alex the " + animal)
#     elif animal == 'Zebra':
#         print("Marty the " + animal)
#     elif animal == 'Giraffe':
#         print("Melman the " + animal)
#     elif animal == 'Hippo':
#         print("Gloria the " + animal)

## Errors Found ##
# if animal == "Lion': <---- Had different quotation marks
# print "Marty the " + Animal <------ the animal variable was capitalized
# NONE of the strings after print were inside parenthesis

#### PART 2 #### 

# Import the Random Module
import random

# Code Name Lists
alpha = ['Crimson', 'Phantom', 'Zephyr', 'Palisade', 'Skyfall']
omega = ['Whirlwind', 'Gatecrasher', 'Iceberg', 'Zealot', 'Element']

# CREATE FOR LOOP HERE
# HINT: The print function below needs to loop 5 times. In order to receive credit, you must use a FOR Loop. 
for item in range(5):


# Print Random Code Name
# HINT: This line of code can be moved if necessary
    print(f"Operation: {random.choice(alpha)} {random.choice(omega)}")