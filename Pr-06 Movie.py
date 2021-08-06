# Movie ticket booking system.
"""
The system asks customer for which movie the want to watch then
it asks for age of customer

If the age of customer is eligible to watch the movie and ticket
if the ticket is available for that movie then system book the ticket
for the customer.

"""

cinema={
    "Tanhaji: The Unsung Warrior":[10,15],
    "Angrezi Medium":[16,10],
    " Sonic the Hedgehog ":[10,12],
    "Avengers: Endgame":[18,8],
    "Joker":[18,10],
    "Spider-Man: Far from Home":[18,5]
    }

while True:
    print("*" *117)
    print("Today's Movies List")
    print(list(cinema.keys()))

    choice = input("Which film would you like to watch?:").strip().title()
    if choice in cinema:
        age = int(input(("How old are you?:").strip()))
        
        if age > cinema[choice][0]:
            seat = cinema[choice][1]
            if seat > 0:
                print( "Enjoy the film...")
                cinema[choice][1] = cinema[choice][1] -1
            else:
                print("Sorry, we are sold out!")
        else :
            print("You are too young to see that film.")
    else :
        print("We dont have that film...\n")
    
    
        
