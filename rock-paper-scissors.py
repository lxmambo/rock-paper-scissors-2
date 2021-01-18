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

rps = [rock, paper, scissors]
computer_nb = random.randint(0,2)
human_nb = int(input("what do you choose? 0 for Rock, 1 for Paper, 2 for Scissor. "))

computer = rps[computer_nb]
human = rps[human_nb]

print(f"You chose:\nf{human}")
print(f"\ncomputer chose:\nf{computer}")

result = [[0,-1,1],[1,0,-1],[-1,1,0]]

if result[computer_nb][human_nb] == 1:
  print("computer won!")
elif result[computer_nb][human_nb] == -1:
  print("you won!")
else:
  print("drawn!")