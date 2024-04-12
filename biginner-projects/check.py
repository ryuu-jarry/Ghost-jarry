with open('password.txt','r')as word:
    word = word.read()
    lines = word.split()
    user = input('check password ::: ')
    for line in lines:
        if (line == user):
            print('password is break \nthis password is here for file!!!!')
            break
        print(line)