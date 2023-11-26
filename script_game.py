# This begins the Text generated User input game 
#By Paul Schulz, project started on 11/16/23

#Module that allows for random number generation maily used in the puzzles found in the game
import random

#Gives the user a list of usable commands in the game 
print("Here are a list of commands for your journey:")
print(" ")
print("fight, run, forward, reverse, left, right, middle, hidden door, solve")
print(" ")
print("And one secret command you must find on your journey!")
print(" ")
print("Remember adventurer, every input counts, one input is the difference between fourture or failure!")
print(" ")
print("Type -begin- your journey to start your adventure ")
print(" ")
#Where the user can input their choice
user = str(input("What are you going to do!" + " "))

#Conditional statement that begins the jouney of the user through the game 
if user == "begin" :
  print(" ")
  print("Your adventure has began, and you stand outside the entrance to the decrepit woods")
  print(" ")


#Conditional statment that givces user the choice to continue to the cave or to go to the castle
if (input("What are you going to do!" + " ")) == "forward" : 
  print(" ")
  print("You Venture out into the woods and find yourself standing at a decrepit gate")
  print(" ")
else:
  print(" ")
  print("You wander off in a random dicrection and find yourself standing outside a cave in the middle of the forest")
  print(" ")


#Begining of the cave choice options 
  if (input("What are you going to do?" + " ")) == "forward" :
    print(" ")
    print("You venture into the cave and find your self in a dark room with two doors one on the left, and one on the right") 
    print(" ")
  else :
    print(" ")
    print("You venture into the cave and find your self in a dark room with two doors one on the left, and one on the right")
    print(" ")
    #Statments concering the door on the right are further down, these begining conditionals concern the door on the left in the cave


  #Begining of door choices 
  if (input("What are you going to do?" + " ")) == "left" :
    print(" ")
    print("You go through the door on the left and find yourself surrounded by skeletons!")
    print(" ")
    
  else:
    print(" ")
    print("You go in the door on the right and find yourself in a long dark hallway")
    print(" ")


  #Begining of what happends upon entering the left door in the cave 
  if (input("What are you going to do?" + " ")) == "fight" :
    print(" ")
    print("You fight valiantly dealing a significant ammound of damage, but not enough to finish off the skeletons")
    print(" ")
  else:
    print(" ")
    print("You quickly turn and make for the door but are unable to escape,l you narrowly dodge a sword and find yourself pinned against the door")
    print(" ")


  if (input("What are you goihng to do?" + " ")) == "reverse" :
    print(" ")
    print("You leave the room and are now back in the first room of the cave with both the door on the left and the door on the right")
    print(" ")
  else:
    print(" ")  
    print("You quickly dart out of the room but in the process nearly lose your life, you once again find yourself in the room with the door on the left and the door on the right")
    print(" ")
        
  #Begining of the user returning to the origional room and continuing through the door on the right 
  if (input("What are you going to do?" + " ")) == "right" :
    print(" ")
    print("You go into the door on the right and find yourself in a dark hallway")
    print(" ")
  else: 
    print(" ")
    print("You go into the door on the right and find yourself in a dark hallway")
    print(" ")
        
    
  if (input("What are you going to do?" + " ")) == "forward" :
    print(" ")
    print("You continue down the hallway and find yourself surrounded in darkness")
    print(" ")
  else:
    print(" ")
    print("You continue down the hallway and find yourself surrounded in darkness")
    print(" ")

  #Secret conditonal statement within the game that allows the player to find the sword if they know the correct phrase 
  if (input("What are you going to do?" + " ")) == "humility" :
    print(" ")
    print("You stumble into a random room within the darkness and find the MAGIC SWORD!")
    print(" ")
  else: 
    print(" ")
    print("You continue wandering in the darkness and eventually arrive at a door, the door leads to the outside and you find yourself once more in the decrepit woods")
    print(" ")

  if (input("What are you going to do" + " ")) == "forward" :
    print(" ")
    print("You venture back through the darkness and eventually find some light at the end fo the tunnel, you quickly find yourself in front of a decrepit gate")
    print(" ")
  else :
    print(" ")
    print("You venture back through the darkness and eventually find some light at the end of the tunnel, you quickly find yourself in front of a decrepit gate")
    print(" ")
#This ends the choices to be made in the cave, and allows the user to venture into the castle
    
    

#The choices leading the user through the castle and eventually battle with a dragon 
if (input("What are you going to do?" + " ")) == "forward" :
  print(" ")
  print("You venture through the decrepit gate and find a ruined castle on the otherside infested with skeletons, however they haven't noticed you")
  print(" ")
else:
  print(" ")
  print("You venture through the decrepit gate and find a ruined castle on the otherside infested with skeletons, however they don't seem to notice you")
  print(" ")

#Begins conditonal statements that lead the user through the middle, or hidden door. 
#There is also a bug in this block of code, the else statment does not execute 
if (input("What are you going to do?" + " ")) == "forward" :
  print(" ")
  print("You sneak past the skeletons at the front gate and make your way into the castle")
  print(" ")
else:
  print(" ")
  print("You try and sneak past the skeleton's and are seen in the process, the skeletons are coming!")
  print(" ")
#End of bugged block of code 

#Code block for choices after dealing with the skeletons at the entrance to the caslte
if (input("What are you going to do?" + " ")) == "forward" :
  print(" ")
  print("You find yourself standing in the main castle forum. A single door in the middle of the room stands before you")
  print(" ")
else : 
  print(" ")
  print("You turn and run as fast as you can and quickly relaize there are too many of them to fight at once, you quickly dart inside the castle and slam the door behind you")
  print(" ")
  print("You findk yourself standing in the main castle forum. A single door in the middle of the room stands before you")
  print(" ")
#End of choices concering entering the castle

#Choices leading up to the two puzzles found inside the castle both secret and not
if (input("What are you going to do?" + " ")) == "middle" :
  print(" ")
  print("You go through the middle door and find yourself in a well lit hallway that preceivably is a dead end, however you quickly realize there is a secret door!")
  print(" ")
  print("Upon examining the secret door, you realize there is a puzzle that must be solved in order to pass")
  print(" ")
else : 
  print(" ")
  print("You spend a lot of time contemplating your options, and decide going through the middle door is best, upon entering the room you find a dead end")
  print(" ")
  print("However upon examining the wall you quickly realize there is a secret door, you also know you must solve the puzzle in order to open the door")

#Where user really has no choice on whether to solve the puzzle or not
if (input("Enter -solve- to attempt the puzzle" + " ")) == "solve" :
  print(" ")
  print("You click a stone in the wall and activate the puzzle, you must solve it in order to pass.")
  print(" ")
else:
  print(" ")
  print("You realize you have no choice, you must solve the puzzle in order to proceed into the castle further")
  print(" ")

#This code block is the begining of the puzzle to open the secret door in the castle 
while random.randint(1,50) :
  if (input("Guess a Numkber Here" + " ")) == "22":
    print(" ")
    print("You guessed correctly and the door opens, you may now proceed")
    print(" ")
    break
  else :
    print(" ")
    print("Your guess is incorrect, try again")
    print(" ")
#Optional puzzle for user to learn secret word for next adventure 
if (input("What are you going to do?" + " ")) == "hidden door" :
  print(" ")
  print("You continue through the secret door after solving the puzzle to once again find yourself face to face with another puzzle, you must solve it in order to proceed")
  print(" ")
  #Loop for secret puzzle that gives the command needed to find the magic sword

  while random.randint(1,90) :
    if(input("Guess a Number Here" + " ")) == "54" :
      print(" ")
      print("You solve the puzzle and the wall slides open to reveal the SECRET COMMAND!, the command is humility, but where can you use it?")
      print(" ")
      break
    else:
      print(" ")
      print("You guessed incorrectly, try again")
      print(" ")
    #End of puzzle loop

  #begining of choices that lead user to the end game of the castle choices
  if (input("What are you going to do?" + " ")) == "reverse" :
    print(" ")
    print("You continue through the secret door and quickly find yourself in a long hallway with a door on the other end")
    print(" ")
  else:
    print(" ")
    print("You continue through the secret door and quickly find yourself in a long hallway with a door on the other end")
    print(" ")
else : 
  print(" ")
  print("You continue through the secret door and qucikly find yourself in a long hallway with a door on the other end")

#End of secret puzzle in the castle and begining of the end stages of the castle portion of the adventure 
if (input("What are you going to do?" + " ")) == "forward":
  print(" ")
  print("You continue through the door and find yourself in a gigantic room in which you cannot see to the other side of")
  print(" ")
else:
  print(" ")
  print("You continue through the door and find yourself in a gigantic room in which you cannot see to the other side of")
  print(" ")

#Begining of fight with the dragon found in the castle 
if (input("What are you going to do?" + " ")) == "forward" :
  print(" ")
  print("You continue through the large room and find yourself face to face with a dragon that has taken roost in the castle!")
  print(" ")
else :
  print("You wander randomly through the room and awaken the dragon on the far side of the room! It is coming for you and is very very angry!") 
  print(" ")

#Begining of the battle with the dragon 
if (input("What are you going to do!" + " ")) == "fight" :
  print(" ")
  print("You muster all the courage you posses, out of the corner of your eye the dragon lets loose with its flmaing breath and you duck behind a pillar")
  print(" ")
  print("The dragon takes a second to catch its breath after breathing fire and you realize now is your chance, you draw your sword and strike the dragon down!")
  print(" ")
  print("You defeat the dregon and take all its riches, you can return home now knowing your adventure was a sucess.")
else :
  print(" ")
  print("You make a run for the door and narrowly dodge the dragon's flamming breath and quickly make your way out of the castle knowing the dragon is chasing you.")
  print(" ")
  print("You however are not fast enough and are burned to a crisp and die a horrible death of burninating from Trogdor the Burninator!")
  print(" ")
#End of either fighting or running from the dragon







   

