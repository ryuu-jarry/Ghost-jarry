import requests
from colorama import Fore
class webvernbility:
    def __init__(self) -> None:
        pass

    def show(self,url,user):
        newurl = self.url = url
        r = requests.get(newurl)
        rootuser = self.user = user
        if rootuser == 'cookies' or rootuser == '1':
            print(f'{Fore.GREEN}This web cookies ===>  ::',r.cookies)
            print()

        elif rootuser == 'elapsed' or rootuser == '2':
            print(f'{Fore.GREEN}This web elapsed ===> ::',r.elapsed)
            print()

        elif rootuser == 'encoding' or rootuser == '3':
            print(f'{Fore.GREEN}This web encoding ===> ::',r.encoding)
            print()

        elif rootuser == 'apparent_encoding' or rootuser == '4':
            print(f'{Fore.GREEN}This web apparent_encoding ===> ::',r.apparent_encoding)
            print()

        elif rootuser == 'headers' or rootuser == '5':
            print(f'{Fore.GREEN}This web headers ===> ::',r.headers)
            print()

        elif rootuser == 'history' or rootuser == '6':
            print(f'{Fore.GREEN}This web history ===> ::',r.history)
            print()

        elif rootuser == 'is_permanent_redirect' or rootuser == '7':
            print(f'{Fore.GREEN}This web is_permanent_redirect ===> ::',r.is_permanent_redirect)
            print()

        elif rootuser == 'raw' or rootuser == '8':
            print(f'{Fore.GREEN},This web raw ===> ::',r.raw)
            print()

        elif rootuser == 'ispermenents' or rootuser == '9':
            ispermenents = r.is_permanent_redirect
            print(f'{Fore.GREEN}This web ispermenents ===> ::',ispermenents)
            print()

        elif rootuser == 'request' or rootuser == '10':
            print(f'{Fore.GREEN}This web request ===> ::',r.request)
            print()

        elif rootuser == 'links' or rootuser == '11':
            print(f'{Fore.GREEN}This web links ===> ::',r.links)
            print()

        elif rootuser == 'json' or rootuser == '12':
            print(f'{Fore.GREEN}This web json ===> ::',r.json)
            print()

        elif rootuser == 'next' or rootuser =='13':
            print(f'{Fore.GREEN}This web next ===> ::',r.next)
            print()

        elif rootuser == 'url' or rootuser == '14':
            print(f'{Fore.GREEN}This web url ===> ::',r.url)
            print()

        elif rootuser == 'status_code' or rootuser == '15':
            print(f'{Fore.GREEN}This web status code ===> ::',r.status_code)
            print()
        elif rootuser == '__class__()' or rootuser == '16':
            print(f'{Fore.GREEN}This web class ===> ::',r.__class__())
            print()

        elif rootuser == 'content' or rootuser == '17':
            print(f'{Fore.GREEN}This web content ===> ::',r.content)
            print()

        elif rootuser == 'text' or rootuser == '18':
            print(f'{Fore.GREEN}This web text ==> ::',r.text)
            print()
        else:
            print(f'{Fore.BLUE}<== Out of range ==>')
        

urlEnter = input(f'{Fore.YELLOW}Enter url :: ')

while True:
    print()
    user = input(f'''{Fore.RED}what can't see you ===> 
                 
(1) ==> cookies,
(2) ==> elapsed,
(3) ==> encoding,
(4) ==> apparent_encoding,
(5) ==> headers,
(6) ==> history,
(7) ==> is_permanent_redirect,
(8) ==> raw,
(9) ==> ispermenents,
(10) ==> request,
(11) ==> links,
(12) ==> json,
(13) ==> next,
(14) ==> url,
(15) ==> status_code,
(16) ==> __class__()
(17) ==> content
(18) ==> text
(19) ==> restart 
           exit
:: Enter your choice :: ==> :''')

    site = webvernbility()
    site.show(urlEnter,user)
    print(site)
    if user == 'exit':
        break
    if user == 'restart' or user == '19':
        urlEnter = input('Enter url :: ')