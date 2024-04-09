import random
num = random.randrange(1000,10000)
n = int(input('Guess the 4 digit number ::'))
if (n == num):
    print('Guess!! You guessed the number in just 1 try!! You are a Mastermind!!')
else:
    ctr = 0
    while (n != num):
        ctr += 1
        count = 0
        n = str(n)
        num = str(num)
        correct = ['X']*4
        for i in range(0,4):
            if(n[i] == num[i]):
                count += 1
                correct[i] = n[i]
            else:
                continue
        print('Not quite the number. But you did get',
              count,'digit(s) correct')
        print('\n')
        print('\n')
        n = int(input('Enter your next choice of numbers::'))
        if(count == 0):
            print('None of the number in your input match')
            n = int(input('Enter your next choice of number:'))
    if n == num:
        ctr += 1
        print('You have become a Mastermind!!')
        print('It took you only',ctr,'tries.')
        