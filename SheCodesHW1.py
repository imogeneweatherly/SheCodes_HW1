

# QUESTION 1 

moths_in_house = False
if moths_in_house == True:
    print("Roary Get the moths!")
else:
    print("No threats detected")

# QUESTION 2 
moths_in_house = True
mitch_is_home = True
if moths_in_house and mitch_is_home:
    print("Hooman! Help me get the moths!")
elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooooooow! Hissssss!")
else:
    print("Climb on Mitch.")

# QUESTION 3 
light_colour = "Red"
car_detected = False
if light_colour == "Red" and not car_detected:
  print("Do nothing.")
elif light_colour == "Red" and car_detected:
    print("Flash!")
elif light_colour == "Green" and not car_detected:
    print("Do nothing.")
elif light_colour == "Green" and car_detected:
    print("Do nothing.")
elif light_colour == "Amber" and not car_detected:
    print("Do nothing.")
else:
    print("Do Nothing.")

# QUESTION 4


Height = int(input("Enter height"))

if Height <= 120:
    print("Sorry, not today :(")
else:
    print("Hop On!")
