def textgame():
    tracker = [] #Used to track rooms visited
    
    room = input("""Start: You are in a dark room. There is a door to your right and left, as well as in front and behind you...
             Use w a s d to move around.""") #Start of game

    if room == "d": #If player moves to the right
        print("You see many faces of the past on the walls. You start to hallucinate...")
        tracker.append("horror") #Adds room to tracker list
        print(tracker)
        input("Where will you go?")
        if input == "w":
            print("You enter a room with a table and a chair. You see a book on the table.")
            input("Do you pick up the book or leave it?")
            if input == "yes":
                print("The book is empty. You leave it alone.")
            else:
                pass        
    elif room == "a":  # If player moves to the left
        print("You enter a room with bright white light, and one one chair in the middle of the room.")
        tracker.append("white")
        print(tracker)
        input("Do you check out the chair?")
        if input == "yes":
            print("It is an electrical chair. You have died from electrocution.")
        elif input == "no":
            pass
            tracker.append("bright")
            input("Where will you go?")  # If player moves to the left
    elif room == "w": #If player moves forward
        input("You enter a room, and there is a door with a white light outlining the door. Continue?")
        if input == "yes":
            print("You made it out!")
        else: 
            print("You died from starvation.")


    
    
textgame()