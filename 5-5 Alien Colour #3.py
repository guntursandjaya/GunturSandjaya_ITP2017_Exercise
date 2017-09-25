alien_colour = input("Choose Red,Green or Yellow : ")
alien_colour = alien_colour.lower()

if alien_colour == "green":
    print("You earn 5 points")
elif alien_colour == "red":
    print("You earn 15 points")
else:
    print("You earn 10 points")
