from colorama import Fore,Back,Style

class Account:
    def __init__(self ,bal,acc):
        self.balance = bal
        self.account_no = acc
    
    # debit function
    def debit(self,amount):
        self.balance -= amount
        # change text color using colorama 
        print(f"{Fore.RED}{Back.WHITE}you debited ,",amount,"your current balance is ,",self.balance)
        return

    # credit function
    def credit(self, amount):
        self.balance += amount
        print(f"{Fore.BLACK}{Back.GREEN}you credited ,", amount,"your current balance is ,",self.balance)
        return
    
amount = int(input("Enter your back amount :"))
account_no = int(input("Enter your account no :"))

acc1 = Account(amount,account_no)

word = True

while word :
    if word == True:
        user = input(f"{Fore.WHITE}{Back.BLACK}Enter Debit or Credit or check balance or account_no and exit :")
        data = user.lower()

        if data == "debit":
            debit = int(input("which amount you debited :"))
            text = acc1.debit(debit)

        elif data == "credit":
            credit = int(input("which amount you credited :"))
            text = acc1.credit(credit)

        elif data == "balance":
            print(f"{Fore.WHITE}{Back.RED}",acc1.balance)

        elif data == "account_no":
            print(f"{Fore.WHITE}{Back.BLUE}",acc1.account_no)

        elif data == "exit":
            word = False

        else :
            print("Try Restart.......")

    else :
        break