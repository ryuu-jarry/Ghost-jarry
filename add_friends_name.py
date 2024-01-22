user = input("How many friends do you have: ")
num1 = 1
num2 = int(user)
lst = []
while(num1<=num2):
    user2 = input("Enter your friend's name :")
    lst.append(user2)
    num1 +=1
print(lst)
