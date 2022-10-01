import random


p1 = input('pick your choice: rock, paper or scissor?') 
moves = ('rock', 'paper', 'scissor')
p2 = random.choice(moves)


def get_winner(p1,p2):

    if p1 == p2:
        return ("It's a tie")      
    elif p1 == 'rock':
        if p2 == 'scissors':
            return "First player wins!"
    else:
        return "Computer Player wins!"
    
    if p1 == 'scissors':
        if p2 == 'paper':
            return "First player wins" 
        else:
          return" Computer player wins!"
    elif p1 == 'paper':
      if p2 == 'rock':
        return "First player wins!"
    else:
       return "Computer player win!"
    

print (get_winner(p1,p2))

  
       
