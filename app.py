def textgame():
    tracker = [] #Used to track rooms visited
    
    room = input("""Start: You are in a dark room. There is a door to your right and left, as well as in front and behind you...
             Use w a s d to move around.""") #Start of game

    if room == "d": #If player moves to the right
        print("You see many faces of the past on the walls. You start to hallucinate...")
        tracker.append("horror") #Adds room to tracker list
        print(tracker)
        right = input("Where will you go?")
        if right == "w":
            print("You enter a room with a table and a chair. You see a book on the table.")
            contin = input("Do you pick up the book or leave it?")
            if contin == "yes":
                print("The book is a guide to the past. You read the book and start to feel a sense of loss.")
                tracker.append("book")
                print("You feel your soul ascending. you escape the backrooms.")
                tracker.append("end")
                print(tracker)
            else:
                print("death")        
    elif room == "a":  # If player moves to the left
        print("You enter a room with bright white light, and one one chair in the middle of the room.")
        tracker.append("white")
        print(tracker)
        left = input("Do you check out the chair?")
        if left == "yes":
            print("It is an electrical chair. You have died from electrocution.")
        elif left == "no":
            pass
            tracker.append("bright")
            left2 = input("Where will you go?")  # If player moves to the left
            if left2 == "w":
                tracker.append("solemn1")
                print("The room you enter is quiet. Too quiet...")
                print("There are no other doors. No sound, no light. You go insane and slowly return to dust.")
            elif left2 == "a":
                print("You enter a room with a monster the size of the empire state building. You have died.")
            elif left2 == "s":
                print("You enter a room with a lake of sulfuric acid. You have died.")
            elif left2 == "d":
                print("I am too lazy to think of a room name. You die.")
            
    elif room == "w": #If player moves forward
        decision = input("You enter a room, and there is a door with a white light outlining the door. The door behind locks. Continue?")
        tracker.append("holy1")
        if decision == "yes":
            print("You made it out!")
            tracker.append("end")
            print(tracker)
        else: 
            print("You died from starvation.")


    
    
textgame()