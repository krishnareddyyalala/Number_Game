import random
import os

if os.path.exists("source.txt"):
   with open("source.txt", "r")as file:
     prev=file.read().strip()
   print(f"can you beat the previous score {prev}")
else:
    print("no previous score found")
a=random.randint(1,100)
score = [100, 80, 60, 40, 20]
for i in range(5):
  b=int(input("enter the number between 1 to 100: "))
  if a==b:
    print("correct you won")
    print(f"the score is {score[i]}")
    with open("source.txt", "w") as file:
        file.write(str(score[i]))
    break
  else :
    hint= "too low" if a>b  else "too high"
    print(f"the no is {hint}")
    if i<4:
     print(f"wrong: you have {4-i} chances left")
    else:
     print("wrong. try again")
     with open("source.txt", "w") as file:
        file.write("0")