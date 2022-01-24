"""
Name(s): Penelope Chew
Name of Project: CS9 Spring Project - Choose Your Adventure (School Edtion)
"""

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

import os

choice = input("Today is yet another day of school, a Tuesday. After crawling out of bed, shoving breakfast into your mouth, and waiting for the delayed train to arrive, you arrive at the main entrance of Hunter nearly late - it is 8:06. You are struggling to find your ID. Yesterday you stuffed it somewhere in your bag and you forgot where. You're at the front of the line. Do you try to sneak past without scanning your ID or attempt to find it, potentially becoming late as a result of this? Type sneak if you try and sneak past and type look to look for you ID: ")
while choice not in ['sneak', 'look']:
  os.system('clear')
  print("That's not a valid input.")
  choice = input("Today is yet another day of school, a Tuesday. After crawling out of bed, shoving breakfast into your mouth, and waiting for the delayed train to arrive, you arrive at the main entrance of Hunter nearly late - it is 8:06. You are struggling to find your ID. Yesterday you stuffed it somewhere in your bag and you forgot where. You're at the front of the line. Do you try to sneak past without scanning your ID or attempt to find it, potentially becoming late as a result of this? Type sneak if you try and sneak past and type look to look for you ID: ")
if choice == "sneak":
  choice = input ("You don't have time to look for your ID. You walk through the door and hold up your metrocard to the scanning machine briefly, hoping the guard doesn't notice. They don't. After reaching staircase A, you breathe a sigh of relief. You run up the stairs and arrive just in time for math class. Afterwards, you go to your second class, global studies, where you are greeted with a pop quiz on last night's reading. That's a problem. You read it, but don't remember anything from it. There's only one question, and it's multiple choice. Easy, right? Not really. You decide it's not A or D. That leaves just C or D. Type in C if you choose C and type in D if you choose D: ")
  while choice not in ['C', 'D']:
    os.system('clear')
    print("That's not a valid input.")
    choice = input("You don't have time to look for your ID. You walk through the door and hold up your metrocard to the scanning machine briefly, hoping the guard doesn't notice. They don't. After reaching staircase A, you breathe a sigh of relief. You run up the stairs and arrive just in time for math class. Afterwards, you go to your second class, global studies, where you are greeted with a pop quiz on last night's reading. That's a problem. You read it, but don't remember anything from it. There's only one question, and it's multiple choice. Easy, right? Not really. You decide it's not A or D. That leaves just C or D. Type in C if you choose C and type in D if you choose D: ")
  if choice == "C":
   choice = input ("You choose C on the test. After handing it in, you ask the people around you what they got. They all answer C. Yes! Nothing better then guessing the right answer. It's lunch now, and you are with your friends deciding where to eat. You could eat outside, but it's cold. You could eat in the eating rooms but you'd be seperated by class. Where do you choose to eat? Type outside if you want to eat outside and type inside if you want to eat inside: ")
   while choice not in ['outside', 'inside']:
    os.system('clear')
    print("That's not a valid input.")
    choice = input("You choose C on the test. After handing it in, you ask the people around you what they got. They all answer C. Yes! Nothing better then guessing the right answer. It's lunch now, and you are with your friends deciding where to eat. You could eat outside, but it's cold. You could eat in the eating rooms but you'd be seperated by class. Where do you choose to eat? Type outside if you want to eat outside and type inside if you want to eat inside: ")
  if choice == "outside":
      print("You decide to eat outside so you can be with your friends. It isn't even that cold and you guys have fun. You have a pretty uneventful day and you when you get home, you find you only have one homework. All in all, a pretty good day.")
  elif choice == "inside":
        print("It's cold outside and you never liked the cold. Besides, you can meet up with your friends after eating fast in the foyer. You go to your eating room and eat quickly. Then, you go to foyer. You play cards with your friends and win. You finish the day with a smile and bragging rights.")
  elif choice == "D":
    choice = input ("You put down D. After consulting your classmates, you find you put the wrong answer. You sigh. Nothing like getting a 0. Official feels glum and when you exit the room, you trip and fall. Someone's hand appears, and you grab it. They pull you up. You say thanks and are about to go, but they stop you. They ask you if you want to eat with them today. You don't know them that well, and were planning to meet up with your friends. You don't want to disappoint them though. Do you say yes or no? Type yes for yes and no for no: ")
    while choice not in ['yes', 'no']:
     os.system('clear')
     print("That's not a valid input.")
     choice = input("You put down D. After consulting your classmates, you find you put the wrong answer. You sigh. Nothing like getting a 0. Official feels glum and when you exit the room, you trip and fall. Someone's hand appears, and you grab it. They pull you up. You say thanks and are about to go, but they stop you. They ask you if you want to eat with them today. You don't know them that well, and were planning to meet up with your friends. You don't want to disappoint them though. Do you say yes or no? Type yes for yes and no for no: ")
    if choice == "yes": 
     print("You don't really want to disappoint them, and you meet with your friends everyday. You decide to eat lunch with them and turns out they were a cool person! You made a new friend today.")
    elif choice == "no":
      print("You don't really know them that well. You politely decline and say you're busy. They laugh and say it's okay. When you walk away though, you feel a bit gulity. Later in the day, you regret not saying yes, even though you had a good time with your friends during lunch.")
    
elif choice == "look":
   choice = input ("You don't want to sneak past, so you look for you ID. You find it! 2 minutes later. It is 8:08. You are going to be late for class. You run up the stairs, walk really fast down the hallway, and open the door, red in the face. The teacher is also late. Whew. You get to your seat, take off your coat and bring out your notebook, just like you were always there just in time as the teacher comes in. Nothing like coming in late but the teacher is also late. You are halfway through class when your phone alarm goes off. You want to bring out your phone to properly turn it off but you don't want the teacher to question it. But if you don't do that, the alarm will keeping on going - even if you press the power button it'll go on snooze and go off again in 10 minutes. Do you try and take your phone out or just keep pressing the power button? Type in bring to bring out your phone, and snooze to keep snoozing your phone: ")
   while choice not in ['bring', 'snooze']:
     os.system('clear')
     print("That's not a valid input.")
     choice = input("You don't want to sneak past, so you look for you ID. You find it! 2 minutes later. It is 8:08. You are going to be late for class. You run up the stairs, walk really fast down the hallway, and open the door, red in the face. The teacher is also late. Whew. You get to your seat, take off your coat and bring out your notebook, just like you were always there just in time as the teacher comes in. Nothing like coming in late but the teacher is also late. You are halfway through class when your phone alarm goes off. You want to bring out your phone to properly turn it off but you don't want the teacher to question it. But if you don't do that, the alarm will keeping on going - even if you press the power button it'll go on snooze and go off again in 10 minutes. Do you try and take your phone out or just keep pressing the power button? Type in bring to bring out your phone, and snooze to keep snoozing your phone: ")
   if choice == "snooze":
    choice = input ("You don't want to risk getting caught with a phone in class. You just press the power button. 10 minutes later, the alarm goes off again. People glance at you, and you turn a bit red again. 10 minutes after that, it goes again, but the period has ended. That was kind of embarassing. You exit the classroom, and find the hallway to be packed. You usually cross that hallway to go to staircase A, but it seems unlikely you'll make it through without shoving someone. Staircase E is right there though. However, if you took that route you would have to go around the 2nd floor. Do you try and make your way past the crowd or take staircase E and walk a lot? Type in hallway to try and get through, and E to take staircase E: ")
    while choice not in ['hallway', 'E']:
     os.system('clear')
     print("That's not a valid input.")
     choice = input("You don't want to risk getting caught with a phone in class. You just press the power button. 10 minutes later, the alarm goes off again. People glance at you, and you turn a bit red again. 10 minutes after that, it goes again, but the period has ended. That was kind of embarassing. You exit the classroom, and find the hallway to be packed. You usually cross that hallway to go to staircase A, but it seems unlikely you'll make it through without shoving someone. Staircase E is right there though. However, if you took that route you would have to go around the 2nd floor. Do you try and make your way past the crowd or take staircase E and walk a lot? Type in hallway to try and get through, and E to take staircase E: ")
    if choice == "hallway":
     print("You don't have that much time. You take a deep breath and go into the storm. You say excuse me a lot and have to squeeze in. You get pushed up against the lockers at some point, which isn't fun. How did the hallway get so crowded anyway? But you finally make it through. What a story to tell your friends at lunch.")
    elif choice == "E":
      print("You know you are not making it through that hallway. You take staircase E and walk really fast around the 2nd floor to get to your class. You arrive just in time. You always didn't like staircase E, because it didn't go to the basement or the 4th floor. But then again, Hunter is a weird school, but you still love it. Kind of.")
   elif choice == "bring":
    choice = input ("You decide it would be quick and when the teacher turns around, you quickly take out your phone and turn the alarm off. But, you drop your phone and it falls to the floor. The teacher stares at it. You stare at it. The teacher asks you to put away your phone. You do, red in the face. You hate it when teachers single you out. After lunch, you enter music class kind of early. One of your friends says you should play the piano there. You know how to play piano. Do you say yes or no? Type in yes to play and type in no to decline: ")
    while choice not in ['yes', 'no']:
     os.system('clear')
     print("That's not a valid input.")
     choice = input("You decide it would be quick and when the teacher turns around, you quickly take out your phone and turn the alarm off. But, you drop your phone and it falls to the floor. The teacher stares at it. You stare at it. The teacher asks you to put away your phone. You do, red in the face. You hate it when teachers single you out. After lunch, you enter music class kind of early. One of your friends says you should play the piano there. You know how to play piano. Do you say yes or no? Type in yes to play and type in no to decline: ")
    if choice == "yes":
      print("You decide to play. Not many people are there anyways. You decide to play some simple songs so you don't screw up and at the end feel pretty good about yourself. Some of your classmates now know you're a pretty good musician.")
    elif choice == "no":
      print("You don't want to embarrass yourself. So instead, your friend goes up and plays. They are really good and the room is blown away. You laugh and say they're just showing off. They retort you just don't want to bring attention to yourself after math class. That's friends for you.")
   



