#!/usr/bin/python

print("Welcome to Zork Concept Plus!")
print("By Sanjay Seshan")
print("Copyright (c) Sanjay Seshan 2013")
print("Loading...")

while exit != "3" :
	invent = "match"
	main = "Which direction would you like to go?"
	count = "1"
	exit == "1"
	while exit != "2" :
		print("You are in the echo room")
		print(main)
		action= input("--")
	 	if action == "forward":
			print("You found a painting")
		elif action == "left":
	            code = input("Code-->")
        	    if code == "15237" :
                	print("You found a key")
                	count = "2"
                	invent = "match,key"
              	    else:
               		print("wrong")
		elif action == "right":
			print("There is a table. A peice of paper says 15237.")
		elif action== "backward" :
			if count== "1" :
				print("You bumped into the wall")
			if count== "2" : 
				print("You found the door")
				main = "What would you like to do with the door?"
		elif action =="use-key" :
			print("The door is open")
			exit = "2"
		elif action == "list" :
			print(invent)
		else:
			print("Command not found")




	main = "It is getting dark, you need to find shelter. Which direction would you like to go?"
	count = "1"
	exit = "1"
	while exit != "2" :
	        print("You are in a forest")
	        print(main)
	        action= input("--")
	        if action == "forward":
	                print("You found a cave")
			main = "What would you like to do with the cave?"
	        elif action == "left":
	                print("You found a sword")
			invent = "match,key,sword"
	        elif action == "right" :
	                print("Nothing")
	        elif action== "backward" :  
	                print("You bumped into a tree")
	        elif action == "go-into-the-cave" :
	                print("good")
        	        exit = "2"
		elif action == "none":
			print("fine")
		elif action == "list" :
	                print(invent)
	        else:
	                print("Command not found")




	main = "A bear is lurking in the cave. What would you like to do?"
	count = "1"
	exit = "1"
	while exit != "2" :
        	print("You are in the cave")
        	print(main)
        	action= input("--")
        	if action == "list":
                	print(invent)
	        elif action == "fight":
        	        print("The bear is killed")
    	                invent = "match,key,sword"
			exit = "2"
  	        elif action == "use-match" :
          	        print("The bear ran away")
	 		invent = "key,sword"
			print("You used up your only match")
			exit = "2"
		elif action == "none":
			print("You have been eaten" , "You died")
			exit="3"
		else :                
                	print("Command not found")







	invent = "sword"
	main = "You were badly injured by the bear. You need to make medicine. You have also lost your key and match."
	count = "1"
	exit = "1"
	while exit != "2" :
        	print("You are in the cave")
        	print(main)
        	action= input("--")
                if invent == "maple leaves,berries,sword,water" :
            	    print("You have made the medicine")
            	    exit = "2"

        	if action == "list":
                	print(invent)
	        elif action == "right":
        	        print("There is an old enscription reading : 2 maple leaves, water, and berries.")
    	               
		
  	        elif action == "forward" :
          	        print("You found the bear's food. The food contains maple leaves and berries.")
                    invent = "maple leaves,berries,sword"
			
		elif action == "backward":
			print("You found a puddle of water.")
			if invent == "maple leaves,berries,sword" :
			   	invent = "maple leaves,berries,sword,water"
			else :
				invent = "sword, water" 
		else :                
                	print("Command not found")

        
        

        
	exit = "3"
