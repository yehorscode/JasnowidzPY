from utils.dependencies import checkDependency
from utils.logmanager import get_date, error, warn, success, info, user_input
import os
from colorama import Fore, Back, Style
from commands.wybierz_strone import wybierzStrone

def chooseAction():
    print(f"{Back.GREEN}Wybierz akcję:{Style.RESET_ALL}")
    print(f"{Back.GREEN} 1 {Style.RESET_ALL} - Wyszukaj wydarzenia")
    print(f"{Back.GREEN} 2 {Style.RESET_ALL} - Wyslij do appwrite")
    print(f"{Back.GREEN} 3 {Style.RESET_ALL} - Sprawdź status stron")
    response = user_input("Podaj numer akcji: ")
    if response == "1":
        info("Wybrano 1")
        print()
        wybierzStrone()
    if response == "2":
        info("Wybrano 2")
        print()
    if response == "3":
        info("Wybrano 3")
        print()


def start():
    info("Start Programu")
    info("Zaczęto sprawdzanie dependencies...")
    checkDependency()
    success(f"Zakończono szukanie dependencies")
    print()
    chooseAction()


start()
