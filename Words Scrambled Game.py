def game():
    import random
    words =["ironman","thor","wanda","vision","hulk","captainamerica"]
    word=random.choice(words)
    #print(word)
    jumble=''.join(random.sample(word,len(word)))
    #print(jumble)
    chances=3
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
        else:
            chances-=1
            print('Incorrect Guess !')
            print('You Have ',chances,'Chances Remaining !!')
            print()
    else:
        print('You Loss !!!')
        print('Correct Word is ',word)
a=10000000
while a!=0:
    game()
    a-=1