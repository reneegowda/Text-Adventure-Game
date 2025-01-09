import time #Imports a module to add pauses 

#Get the current time to track the elapsed time
start_time = time.time()

#Set the time limit for the game
time_limit = 60

#Flag to indicate if the time limit has expired
time_expired = False

#Intro Messages with the goal of the game
print("Welcome to  Island Odyssey!") 
time.sleep(1) #A tiny pause
print("You are on a mysterious island with lush jungles, ancient ruins, and hidden caves.") 
time.sleep(1) #A tiny pause

print()
print("Legend says that a chalice filled with powerful blood is hidden away in the mysteries of the island.")
time.sleep(1) #A tiny pause

print()
print("But there are others vying for it. Evil people. You have to find the chalice before they do.")
time.sleep(1) #A tiny pause

print()
print("Your goal is to find the rumored hidden magical artifact.")
time.sleep(1)
print("The catch is that you only have 60 seconds.")
time.sleep(1) #A tiny pause

#Get the player's choice for the first location to explore 
print()
first_stop = input("Do you want to explore the 'caves', 'jungle', or 'ruins' first: ") #The three story branches depending on user input

#The code is sequenced in a way that depending on the player's choices in the story's branches, it will move them forward to other stops

print()
def explore_jungle(): #Each story branch is enclosed in a function to organize (defining the function)
  global time_expired 
  while True: #A while loop for iteration so it keeps running until the correct option is chosen to move forward in the game. 
    #Calculate elapsed time for this branch
    explore_jungle_time = time.time() - start_time 
    if explore_jungle_time > time_limit: 
      #Check if the time limit has expired
      print("Time's up! You didn't find the artifact in 60 seconds.")
      time_expired = True
      break 
    print("The brush is thick and green. Everything is the same.")
    time.sleep(1) #A tiny pause
    exploreJungle = input("Would you like to 'explore' or 'follow the hiking trail': ") #Two sub-branches to each story through if-elif-else statements
    #Using conditionals (selection) to get the player's choice on whether or not they want to explore or follow the hiking trail
    if exploreJungle == "explore": 
      time.sleep(1) #A tiny pause
      print("You are going in circles.") 
      explore_jungle()
    elif exploreJungle == "follow the hiking trail": 
      time.sleep(1) #A tiny pause
      print("You made it through to the caves!") 
      explore_caves()
    else: 
      #Acklowedges that the user inputted something but they have not followed the correct format for inputting
     print("Invalid Input. Follow the correct capitalization and please try again: ")


print()
def explore_caves():#Each story branch is enclosed in a function to organize (defining the function)
  global time_expired 
  while True: #A while loop for iteration so it keeps running until the correct option is chosen to move forward in the game. 
    #Calculate elapsed time for this branch
    explore_caves_time = time.time() - start_time
    if explore_caves_time > time_limit: 
      #Check if the time limit has expired
      print("Time's up! You didn't find the artifact in 60 seconds.")
      time_expired = True
      break #Exit the loop 
    print("The caves loom before you. The dark grey walls cave in.")
    time.sleep(1) #A tiny pause
    print("There is pitch darkness in front of you.") 
    time.sleep(1) #A tiny pause
    print("You start walking, but, the path suddenly splits into two.")
    time.sleep(1) #A tiny pause
    exploreCaves = input("Would you like to 'go left' or 'go right': ") #Two sub-branches to each story through if-elif-else statements
     #Using conditionals (selection) to get the player's choice on whether or not they want to go left or go right
    if exploreCaves == "go left": 
      time.sleep(1) #A tiny pause
      print("You found the ruins!")
      explore_ruins()
    elif exploreCaves == "go right":
      time.sleep(1) #A tiny pause
      print("You made it through to the jungle!")
      explore_jungle()
    else: 
       #Acklowedges that the user inputted something but they have not followed the correct format for inputting
      print("Invalid input. Follow the correct capitalization and please try again: ")

print() 
def explore_ruins(): #Each story branch is enclosed in a function to organize (defining the function)
  global time_expired
  while True: #A while loop for iteration so it keeps running until the correct option is chosen to move forward in the game. 
    #Calculate elapsed time for this branch
    explore_ruins_time = time.time() - start_time 
    if explore_ruins_time > time_limit: 
       #Check if the time limit has expired
      print("Time's up! You didn't find the artifact in 60 seconds.")
      time_expired = True
      break #Exit the loop 
    print("The destroyed village of Lylac lays before you.")
    time.sleep(1) #A tiny pause
    print("It's been buried in layers of dust.")
    time.sleep(1) #A tiny pause
    exploreRuins = input("Would you like to 'follow the secret passage' or 'search for treasure': ") #Two sub-branches to each story through if-elif-else statements
     #Using conditionals (selection) to get the player's choice on whether or not they want to follow the secret passage or search for treasure
    time.sleep(1) #A tiny pause
    if exploreRuins == "follow the secret passage":
      if explore_ruins_time < time_limit: 
        #Once again the if statement checks if the time limit has expired or not since they have entered the correct branch to find the artifact. 
        print("You found the artifact in time! Congratulations! You saved the world from evil.")
      exit() #Exit the game 
    elif exploreRuins == "search for treasure":
      time.sleep(1) #A tiny pause
      print("You wasted all your energy for nothing! You are back in the caves!")
      explore_caves()
    else: 
      print("Invalid input. Follow the correct capitalization and please try again: ")
      #Acklowedges that the user inputted something but they have not followed the correct format for inputting

print()
 #Using conditionals (selection) to determine which function should run depending on what the user input was and whether or not the time limit has expired yet

if first_stop == "caves" and not time_expired:
    print("You have chosen to explore the caves!")
    explore_caves() #Calling the function so that it runs
elif first_stop == "jungle" and not time_expired:
    print("You have chosen to explore the jungle!")
    explore_jungle() #Calling the function so that it runs
elif first_stop == "ruins" and not time_expired:
    print("You have chosen to explore the ruins!")
    explore_ruins() #Calling the function so that it runs
else: 
  print("Invalid input. Follow the correct capitalization and please try again: ")
  first_stop = input("Do you want to explore the 'caves', 'jungle', or 'ruins' first: ") 

#Repeating this once more in case of an invalid input, so that the sequence of the program continues properly

if first_stop == "caves" and not time_expired:
  print("You have chosen to explore the caves!")
  explore_caves() #Calling the function so that it runs
elif first_stop == "jungle" and not time_expired:
  print("You have chosen to explore the jungle!")
  explore_jungle() #Calling the function so that it runs
elif first_stop == "ruins" and not time_expired:
  print("You have chosen to explore the ruins!")
  explore_ruins() #Calling the function so that it runs

if time_expired: 
  #The conditional says if the time limit has expired, the game will exit after displaying that it is over. 
  print("Game over!")
  exit()
