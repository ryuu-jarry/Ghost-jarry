import random
from colorama import Fore

class Psswd:
    def __init__(self, fullname):
        self.name = fullname

    def generate_passwords(self):
        with open('password.txt', 'a+') as word:
            for pwd in range(1, 1000):
                keyword = '@'  # Change this to your desired keyword
                random_number = random.randint(1000, 99999)  # Generate a random 4-digit number
                password = f"{keyword}{self.name}{random_number}\n"
                word.write(password)
                #print(f'{Fore.CYAN}',password)
            print(f'{Fore.RED}[+] == please wain...')

    def generate_count(self):
        with open('password.txt', 'a+') as word:
            for pwd in range(1, 9999):
                password = f"{pwd}{self.name}\n"
                word.write(password)
                #print(f'{Fore.CYAN}',password)
            print(f'{Fore.YELLOW}[+] == please wait...')

    def generate_count2(self):
        with open('password.txt', 'a+') as word:
            for pwd in range(1, 9999):
                password = f"{self.name}{pwd}\n"
                word.write(password)
                #print(f'{Fore.CYAN}',password)
            print(f'{Fore.YELLOW}[+] == please wait...')

    def sym_generate(self):
        syms = ['!','@','#','$','%','^','&','*']
        with open('password.txt', 'a+') as word:
            for pwd in range(1, 10):
                for sym in syms:
                    password = f"{self.name}{sym}\n"
                    word.write(password)
                    #print(f'{Fore.CYAN}',password)
            print(f'{Fore.RED}[+] == please wait...')

    def sym_generate_f(self):
        syms = ['!','@','#','$','%','^','&','*']
        with open('password.txt', 'a+') as word:
            for pwd in range(1, 10):
                for sym in syms:
                    password = f"{sym}{self.name}\n"
                    word.write(password)
                    #print(f'{Fore.CYAN}',password)
            print(f'{Fore.RED}[+] == please wait...')

    def password1(self):
        syms = ['!','@','#','$','%','^','&','*']
        with open('password.txt', 'a+') as word:
            for pwd in range(1, 9999):
                for sym in syms:
                    password = f"{self.name}{sym}{pwd}\n"
                    word.write(password)
                    #print(f'{Fore.CYAN}',password)
            print(f'{Fore.YELLOW}[+] == please wait...')

    def password2(self):
        syms = ['!','@','#','$','%','^','&','*']
        with open('password.txt', 'a+') as word:
            for pwd in range(1, 9999):
                for sym in syms:
                    password = f"{pwd}{sym}{self.name}\n"
                    word.write(password)
                    #print(f'{Fore.CYAN}',password)
            print(f'{Fore.GREEN}[+] == please wait...')
        print(f'{Fore.BLUE}[+] == password file saved!!!!')




# Example usage:
user = input(f'{Fore.RED}create password file :: ')
ps = Psswd(user)
ps.generate_passwords()
ps.sym_generate()
ps.sym_generate_f()
ps.generate_count()
ps.generate_count2()
ps.password1()
ps.password2()