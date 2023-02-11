#1 What is a variable?
## A Variable is an object that is assigned a value. It can be changed later in the script

#2 What is a constant?
## A constant is an object that has an assigned value that cannot be changed

#3 Can a variable be changed once assigned?
## Yes, vaiables can be changed by reassigning it's value to something else

#4 Write a program that counts for the user.
# Let the user enter the starting number, the ending number, and the amount by which to count..


#start = int(input("Enter number to start at: "))
#end = int(input("Enter the number to end at: "))
#counterAmount = int(input("Enter the amount to count by: "))
#for i in range(start, end, counterAmount):
#   print(i, end=" ")


#5 Create a program that gets a message from the user and then prints it out backwards.


#wordStart = input("Input a word you want reversed: ")
#for i in range(len(wordStart) - 1, - 1, - 1):
#    print(wordStart[i], end="")ffff


#6 ''' Create a game where the computer picks a random word and the player has to guess that word.
# The computer tells the player how many letters are in the word.
# Then the player gets five chances to ask if a letter is in the word.
# The computer can only respond with “yes” or “no”. Then, the player must guess the word.

import random
wordBank = ("Books", "Knowledge", "Exacerbation", "Siri", "Villainous")
print("Your options are: ", wordBank)
guessword = random.choice(wordBank)
correct = guessword
jumble =""
stop_hint = ""
counter = 1
score=len(guessword)*10
print("There are", score /10, "letters in the word")
guess = input("\n Make your guess: ")
if guess != correct:
        print("Wrong")
while guess != correct and guess != "" and counter <=5 and stop_hint !=1:
      letter=input("You can now ask the PC if a letter is in the word: ")
      score-=10
      counter+=1
      if letter.lower() not in correct:
          print("No")
      else:
          print("Yes")
      stop_hint=int(input("Do you want to guess already? Yes; press 1. If you want another hint press 0."))

guess = input("Your guess: ")
if guess != correct:
        print("You lost, better luck next time")
        score=0
if guess == correct:
        print("Good job, you got it!")

input("\n\n Press the enter key to exit.")