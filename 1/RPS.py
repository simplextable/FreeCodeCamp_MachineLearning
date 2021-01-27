# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random


def player(prev_play, history=[], my_history=[]):
    
    #print("len(history): ", len(history))
    #print()
    options = ["R", "S", "P"]


    if my_history:
      if((my_history[-1] == "R" and prev_play == "S")or(my_history[-1] == "S" and   prev_play == "P")or(my_history[-1] == "P" and prev_play == "R")):
        history.append([my_history[-1],prev_play,1])
      
      if((my_history[-1] == "R" and prev_play == "P")or(my_history[-1] == "S" and   prev_play == "R")or(my_history[-1] == "P" and prev_play == "S")):
        history.append([my_history[-1],prev_play,-1])  

      if((my_history[-1] == "R" and prev_play == "R")or(my_history[-1] == "S" and   prev_play == "S")or(my_history[-1] == "P" and prev_play == "P")):
        history.append([my_history[-1],prev_play,0])

     
    if (len(history) <= 100) : 
       guess = random.choice(options) 
      
    if(len(history) > 100):

       a =  [i for i, e in enumerate(history) if e == history[-1]]
       #print("ilk a: ",a)
      
       a = a[-2]
       #print("ikinci a: ", a)
       #a = history.index(history[-1]) 
       his_move = history[a+1]
       
       #print("önceki el: ", history[-1],"///" ,"bu önceki el daha önce neredeydi: ", a-1,"///", "beklenen hamle: ", his_move, "///", "history-1 nedir: ", history[-1])
       
       
       #print("a: ", a) 
       
       
       #print("which time: ", len(my_history),"    " ,"his_move_tuple: ",his_move, "     ", "his_move: ",  his_move[1])
       
       #print("which time: ", len(my_history), "   ", "his_move: ", his_move[1])
       if(his_move[1] == "R"):
         guess = "P"
       if(his_move[1] =="S"):
         guess = "R"
       if(his_move[1] == "P"):
         guess = "S"  
       #print("yeni guess: ", guess) 
    
    
    my_history.append(guess)

    #print(history[-1])
    return guess


    