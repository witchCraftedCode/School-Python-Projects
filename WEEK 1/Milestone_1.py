# [ALEX FHERMAYE]
# Python Version 3.11.4
# Milestone 1

#### List of variables Used ####

name_of_creator = "Alex"
red = "red"
blue = "blue"
yellow = "yellow"
brown = "brown"
green = "green"
black = "black"
orange = "orange"
toyota_camry = "toyota camry"
supra = "supra"
camry = "camry"
toyota = "toyota"
italian_food = "italian food"
mexican_food = "mexican food"
yes = "Yes"
no = "No"
dog = "dog"
cat = "cat"

# Here I stored all variables that I will be using when I create my program

#### Program Start ####

print(f"Hello! My name is {name_of_creator.title()} and it is a great pleasure to meet you!")

# This is my greeting where my name will be included

user_name = input("What is your name? ")
print("That is a cool name!")

# This will be where the program collects the first piece of data which will be the user's input followed by a print display telling the user how cool their name is.

favorite_color = input("What is your favorite color? ")
if favorite_color == red:
    print("You are a weird person!")
elif favorite_color == blue:
    print("That is not ok!")
elif favorite_color == brown:
    print("I guess you like dirt...")
elif favorite_color == green:
    print("Nice! You are one with nature!")
elif favorite_color == black:
    print("One can say that your soul is the same color...")
elif favorite_color == yellow:
    print("I believe that you are not creative!")
elif favorite_color == orange:
    print("My wife LOVES that color!")
else:
    print("I dont think that is a color, bucko.")

# This is the first input question where the program collects the user's favorite color choice and replies with a unique sentence to add feed back to the user. 
# Here we used the input() function followed by an if statement, 6 elif statements and a closing else statement

car_choice = input(f"Ok, {user_name.title()}, let's continue... if you had to pick between a toyota camry or a supra, what would you pick? ")
if car_choice == toyota_camry:
    print(f"Wow {user_name.title()}, you like SLOW CARS!")
elif car_choice == supra:
    print("Great choice!")
elif car_choice == camry:
    print("You forgot to include TOYOTA, buddy.")
elif car_choice == toyota:
    print("You forgot to include CAMRY, buddy.")
else: 
    print("That was NOT an option but ok, everyone has different tastes!")

# The second input question where the program collects the user's response on a unique question which accepts 5 answers and gives feedback accordingly. 
# Here we used the input() function followed by an if statement, 3 elif statements and a closing else statement

favorite_food = input(f"I find it hard to believe that you chose {favorite_color} earlier but let's move on... what is your favorite food? ")
if favorite_food == mexican_food:
    print("I love mexican food!")
elif favorite_food == italian_food:
    print("Mamma mia!")
else:
    print("I don't think I have ever tried that but it sounds great!")

# The third input question which collects the user's favorite food and replies accordinlgy.
# Here we used the input() function followed by an if statement, an elif statement and a closing else statement

favorite_animal = input(f"What is your favorite animal? ")
if favorite_animal == cat:
    print("Cats are mean")
elif favorite_animal == dog:
    print("They are our best friends!")
else: 
    print("That sounds like a dangerous choice...")

# The last input question where the program collects the user's favorite animal answer and proceeds to the final question before presenting the user to the class
# Here we used the input() function followed by an if statement, an elif statement and a closing else statement

end_phase = input("Are you ready to be introduced? ")
# I added this question so that there was a pause between the favorite_animal question and the introducction so that the viewer was not overwhelmed by a paragraph suddently after answering what their favorite animal was and they could clearly see the feedback from the previous question. 

if end_phase.capitalize() == "Yes":
    print(f"Hello classmates, I want you to meet {user_name.title()}! {user_name.title()}'s favorite color is {favorite_color} and {user_name.title()} absolutely loves the {car_choice}. {user_name.title()}'s favorite food is {favorite_food} so please make sure to remember that next time we have a pot luck. {user_name.title()} probably has a {favorite_animal}.")
else:
    print(f"Hello classmates, eventhough {user_name.title()} was not ready for this, we are still doing it! {user_name.title()}'s favorite color is {favorite_color} and {user_name.title()} absolutely loves the {car_choice}. {user_name.title()}'s favorite food is {favorite_food} so please make sure to remember that next time we have a pot luck. {user_name.title()} probably has a {favorite_animal}.")

# I was having too much fun and decided to include two sepparate answers to "yes" or anything other than yes and this also gave me a solution to the question that was used as a pause before. 
# Here is where all data is collected and presented in an F-String to the class introducing the user. 