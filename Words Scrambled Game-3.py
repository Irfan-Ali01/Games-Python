import random
def game():
    if startup==1:
        words =["iron man","thor","wanda","vision","hulk","captain america","thanos","black panther","dr strange","ant man","spider man"]
        word=random.choice(words)
        #print(word)
        jumble=''.join(random.sample(word,len(word)))
        #print(jumble)
        chances=5
        print()
        print()
        print('~'*30)
        print('~~~ Avengers Jumble Bumble ~~~')
        print('~'*30)
        print()
        while chances!=0:
            print('The Word is ',jumble)
            print()
            guess=input('Enter Your Guessed Word: ').lower()
            if guess==word:
                print('Correct Guess !!!')
                print('You Won !!!')
                break
            if guess!=word:
                chances-=1
                print()
                print('Incorrect Guess !!!')
                print('You Have ',chances,'Chances Remaining !!')
                print()
                if chances==0:
                    print('All Chances Are Excausted (You Lose...) !!!')
                    print('The Word is ', word.capitalize())
    elif startup==2:
        print()
while True:
    startup=eval(input('''
                1. Start The Game.
                2. Exit
                            '''))
    if startup==1:
        game()
    elif startup==2:
        break
    else:
        print("Invalid Operation")