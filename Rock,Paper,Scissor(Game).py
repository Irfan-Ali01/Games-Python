import random
d=['Rock','Paper','Scissor']
while True:
    mecount=0
    pccount=0
    print('~'*30)
    print('~~~ Rock | Paper | Scissor Game ~~~')
    print('~'*30)
    print()
    uc=int(input('''
Game Start....
1. Yes | Start the Game
2. No | Exit
'''))
    print()
    print()
    if uc==1:
        for i in range(1,6):
            player=int(input('''
1. Rock
2. Paper
3. Scissor
'''))
            if player==1:
                playerchoice='Rock'
            elif player==2:
                playerchoice='Paper'
            elif player==3:
                playerchoice='Scissor'
            pcchoice=random.choice(d)
            if playerchoice==pcchoice:
                print('Game Draw...')
                print('You Choosed', playerchoice)
                print('Computer Choosed', pcchoice)
                mecount+=1
                pccount+=1
            elif playerchoice=='Rock' and pcchoice=='Scissor' or playerchoice=='Paper' and pcchoice=='Rock' or playerchoice=='Scissor' and pcchoice=='Paper':
                print('You Win !!!')
                print('You Choosed',playerchoice)
                print('Computer Choosed',pcchoice)
                mecount+=1
            else:
                print('Computer Win !!!')
                print('You Choosed',playerchoice)
                print('Computer Choosed',pcchoice)
                pccount+=1
            if mecount==pccount:
                print()
                print('Game Draw')
                print('Your Score: ',mecount)
                print('Computer Score: ',pccount)
                print()
            elif mecount>pccount:
                print()
                print('You Won !!!')
                print('Your Score: ',mecount)
                print('Computer Score: ',pccount)
                print()
            elif pccount>mecount:
                print()
                print('You Lose !!!')
                print('Your Score: ',mecount)
                print('Computer Score: ',pccount)
                print()