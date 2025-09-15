# Alex Fhermaye
# Python Version 3.11.4
# Functions
###################################################################################################
import time

# Custom Functions
# 2. DESCRIBE HOW THE INCLUDED countdown() FUNCTION WORKS
# A: This function does a countdown from n down to 0 by using a loop with a 1 second delay between counts 
def countdown(n):
    while n >= 0:
        print (n)
        time.sleep(1)
        n -= 1

##################################################################################################
# Self Destruct Sequencer
# This is the custom function created to handle all of the Self Destruct
# features needed. There are a few steps involved in the process, so take a few
# moments to study how this function works and think about ways to make it better.
def self_destruct(x):

    # Set Destruct Codes
    authorized_test = "000-Destruct-0"
    authorized_final = "000-Destruct-1"

    # 3. CREATE VARIABLES (SIMILAR TO ABOVE) FOR THE COMMANDING OFFICER'S CODE (co_code)
    # EXECUTIVE OFFICER'S CODE (xo_code) & CHIEF ENGINEER'S CODE (ce_code)
    # Write your code here
    co_code = "111A-Destruct"
    xo_code = "21A2B-Destruct"
    ce_code = "31B2B-Destruct"
    

##################################################################################################
    # Consider the following print statements. Could they be combined into a single print
    # statement and get the same result? (Answer: Yes) There are many ways to resolve
    # issues in scripting. You get to decide what works best for your script.
    #  Display Self Destruct Warning
    print (" --------------------- WARNING! ---------------------- \n You have initiated the USR ARES Self Destruct Program \n _____________________________________________________ \n You must provide Authorized Initiate Code to Proceed.")

##################################################################################################
    # Request Authorized Rank
    # 4. EXPLAIN THE SIGNIFICANCE OF THE int() FUNCTION IN THE FOLLOWING LINE:
    rank = int(input("Select Correct Rank:\n [1] Commanding Officer\n [2] Executive Officer\n [3] Chief Engineer\n RANK: "))
    # A. The int() function is very important because it lets the user choose their rank which determines what conditional statement is activated in the next step

##################################################################################################
    # Because we're expecting the user to enter a number above, the conditional statement
    # below is needed to convert those numbers into something more useful. Doing this helps
    # reduce the risk of the user introducing bad data into the script.
##################################################################################################
    # Retrieve Rank Initiate Code
##################################################################################################
    # Commanding Officer
    if rank == 1:
        code = "111A-Destruct"
        print ("Commanding Officer Confirmed.")
    # Executive Officer
    elif rank == 2:
        code = "21A2B-Destruct"
        print ("Executive Officer Confirmed.")
    # Chief Engineer
    elif rank == 3:
        code = "31B2B-Destruct"
        print ("Chief Engineer Confirmed.")
    else:
        print ("You are not authorized to initial Self Destruct.")


##################################################################################################
    # Enter Self Destruct Code: 000-Destruct-0 or 000-Destruct-1
##################################################################################################
    # Set Supplied Rank Code
    initiate = input("Enter Self Destruct Confirmation Code: ")

    # Compare Rank Codes
    if initiate == code:
        print ("Self Destruct Initiate Code: ACCEPTED")
        final_code = input("Enter Activation Code: ")
        if final_code == authorized_final:
            print ("Destruct Sequence Confirmed.")
            # 5. EXPLAIN THE SIGNIFICANCE OF X
            print (x, " seconds to Self Destruct.")
            # A. When we run the program, x shows the countdown function in effect counting from the number stored earlier to 0
            print ("ALL HANDS ABANDON SHIP - THIS IS NOT A DRILL")
            countdown(x)
            print ("Have a nice day!")
            print ("BOOM!")
        elif final_code == authorized_test:
            print ("Destruct Sequence Test Order Confirmed.")
            print ("THIS IS A DRILL - THIS IS A DRILL")
            print ("Timer Set to: " + x + " seconds.")
        else:
            print ("Destruct Sequence Aborted.")


##################################################################################################
    # Program Ends
##################################################################################################
# Self Destruct
timer = int(input("Enter Countdown Length (in seconds): "))
self_destruct(timer)



# 6. LIST THE LOCAL VARIABLES AND GLOBAL VARIABLES USED THROUGHOUT THIS SCRIPT
# A. 
'''
- authorized_test = "000-Destruct-0"
- authorized_final = "000-Destruct-1"
- co_code = "111A-Destruct"
- xo_code = "21A2B-Destruct"
- ce_code = "31B2B-Destruct"
- rank = int(input("Select Correct Rank: [1] Commanding Officer [2] Executive Officer [3] Chief Engineer RANK: "))
- initiate = input("Enter Self Destruct Confirmation Code: ")
- timer = int(input("Enter Countdown Length (in seconds): "))
self_destruct(timer)
'''


# 7. LIST THE BUILT IN FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A.
'''
print()
input()
'''


# 8. LIST THE MODULE FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. import time 


# 9. LIST THE CUSTOM FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. def countdown(n) and def self_destruct(x)


### CHECKLIST ###
# (X) Complete header comments at the top of the script.
# (X) Describe how the included countdown(n) script works
# (X) Within the self_destruct() function, create variables for the Commanding Officer's Code (co_code), the Executive Officer's Code (xo_code), and Chief Engineer's Code (ce_code).
# (X) Explain the significance of the int() function.
# (X) Explain the significance of x.
# (X) List the Local Variables and the Global Variables used in the script.
# (X) List the Built-in Functions used in the script.
# (X) List the imported Module Functions (if any) used in the script
# (X) List the custom functions used in the script.