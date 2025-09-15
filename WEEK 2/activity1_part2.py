# ALEX FHERMAYE
# Python version 3.11.4
# Grade Conversion

#### PART TWO ####

score = int(input("Enter assignment score: "))

if score >= 95:
    grade = "A+"
elif score >= 90:
    grade = "A"
elif score >= 85:
    grade = "B+"
elif score >= 80:
    grade = "B"
elif score >= 75:
    grade = "C"
elif score >= 70:
    grade = "D"
else:
    grade = "F"

print ("You earned a " + grade + " for this assignment.")