import random
from random import randint
p_score=0
c_score=0
g_s="Playing"
i=0
def play():
  global p_score
  global c_score
  global g_s
  global i
  while g_s == "Playing":
    print(f"Choose your move 1 for stone,2 for paper,3 for scissor")
    p_choice=int(input("Enter your choice"))
    c_choice=randint(1,3)
    
    if (p_choice==1 and c_choice==3) or (p_choice==2 and c_choice==1) or (p_choice==3 and c_choice==2):
      p_score+=1
      c_score+=0
      print("Player Score is:",p_score,"Computer Score is:",c_score)
      i+=1
    elif p_choice==c_choice:
      print("DRAW")
      c_score+=0
      p_score+=0
      i+=1
      print("Player Score is:",p_score,"Computer Score is:",c_score)
    else:
      c_score+=1
      p_score+=0
      i+=1
      print("Player Score is:",p_score,"Computer Score is:",c_score)
    m=p_score
    n=c_score
    z=i
    game_over(m,n,z)
def game_over(x,y,z):
  global g_s
  if z>10:
      if x>y:
          print("PLAYER WINS")
          g_s="Game Over"
          print(g_s)
      elif x<y:
          print("COMPUTER WINS")
          g_s="Game Over"
          print(g_s)
      else:
          print("DRAW")
          g_s="Game Over"
          print(g_s)
  else:
      g_s="Playing"
 
play()
