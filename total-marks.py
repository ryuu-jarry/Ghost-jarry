user = int(input("How many subjects are there in which marks have to be added? :"))
zero = 1
lst = []
while(zero<=user):
    user2 = int(input("Enter your marks :"))
    lst.append(user2)
    zero +=1
print(lst)
print("Total sum of this number :",sum(lst))
print("Parsentge this student :",sum(lst)/6)