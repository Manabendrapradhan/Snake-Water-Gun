import random
def gameWin(comp,you):
    if comp == you:
        return None
    
    elif comp == 'S':
        if you == 'W':
            return False
        elif you == 'G':
            return True
    elif comp == 'w':
        if you == 'G':
            return True
        elif you == 'S':
            return True
    elif comp == ' G':
        if you == 'S':
            return False
        elif you == 'W':
            return True    
        
print ("Comp Trun : Snake(S) Water(W) or Gun (G)?")
randNo = random.randint(1,3) 
if randNo == 1:
    comp ='S'
elif randNo == 2:
     comp ='W'
elif randNo == 3:
    comp= 'G'  

you = input("Your turn: Snake(S) Water(W) or Gun (G)?")
a = gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a Tie! ")
elif a:
    print("You win!") 
else: 
    print("You lose")       