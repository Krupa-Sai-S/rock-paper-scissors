import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Write your code below this line 👇


images = [rock,paper,scissors]

user_choice = int(input("Entrer a value any of the below\nrock is 0,paper = 1,scissors = 2:\n"))
if user_choice >= 3 or user_choice < 0:
    print("WTF You entered a wrong value!")
else:

    
    print("Your_Honor,you choosen:")
    print(images[user_choice])
    
    computer_choice = random.randint(0, 2)
    print("majesty_choosen:")
    print(images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("you won")
    elif computer_choice > user_choice:
        print("you lose!")
    elif user_choice == 2 and computer_choice == 0:
        print("you lose!")
    elif user_choice == 1 and computer_choice == 0:
        print("you won")
    elif user_choice == computer_choice:
        print("So,it's draw")
    else:
        print("Stupid you enter the wrong value")
