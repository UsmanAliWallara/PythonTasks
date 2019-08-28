import random as rd
win = 1
print('---scissor','paper','rock---')

for x in range(3):
    lis = ['scissor','paper','rock']
    word = input('Enter a word from above list:')
    cho = rd.choice(lis)
    
    if word == cho:
        print('Tie..!')
    elif cho == lis[1] and word == lis[0]:
        print('You Won..!','Computer Word',cho)
    elif cho == lis[2] and word == lis[0]:
        print('You Lose..!','Computer Word',cho,'Remaining Life',-x+2)
    elif cho == lis[1] and word == lis[2]:
        print('You Lose..!','Computer Word',cho,'Remaining Life',-x+2)
    elif cho == lis[0] and word == lis[1]:
        print('You Lose..!','Computer Word',cho,'Remaining Life',-x+2)
    elif cho == lis[0] and word == lis[2]:
        print('You Won..!','Computer Word',cho)
    elif cho == lis[2] and word == lis[1]:
        print('You Won..!','Computer Word',cho)
        break
    elif word not in lis:
        print('Wrong!!! word')
        
if win == 0:
    print('Game Over..!')

        