#!/usr/bin/python

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



	exit = "3"
