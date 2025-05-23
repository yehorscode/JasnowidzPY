from utils.dependencies import checkDependency
from utils.logmanager import get_date, error, warn, success, info, user_input
import os
from colorama import Fore, Back, Style
from commands.wybierz_strone import wybierzStrone
from utils.checkstatus import checkStatus
from utils.mergeandsend import mergeandsend
from commands.mergedata import mergedata
from commands.uploadtoappwrite import deletealldocuments

def chooseAction():
    print(f"{Back.GREEN}Wybierz akcję:{Style.RESET_ALL}")
    print(f"{Back.GREEN} 1 {Style.RESET_ALL} - Wyszukaj wydarzenia")
    print(f"{Back.GREEN} 2 {Style.RESET_ALL} - Wyslij do appwrite (i złącz dane)")
    print(f"{Back.GREEN} 3 {Style.RESET_ALL} - Sprawdź status stron")
    print(f"{Back.GREEN} 4 {Style.RESET_ALL} - Wyczyść dane, i roboty")
    print(f"{Back.GREEN} 5 {Style.RESET_ALL} - Złącz dane (bez wysyłania)")
    print(f"{Back.GREEN} 6 {Style.RESET_ALL} - Usuń wszystkie dokumenty (z appwrite)")
    response = user_input("Podaj numer akcji: ")
    if response == "1":
        info("Wybrano 1")
        print()
        wybierzStrone()
    if response == "2":
        info("Wybrano 2")
        print()
        mergeandsend()
    if response == "3":
        info("Wybrano 3")
        print()
        checkStatus("https://lublin.eu/kultura/wydarzenia/")
        checkStatus("https://zoom.lublin.pl/wydarzenia/")
    if response == "4":
        info("Wybrano 4")
        print()
        if os.name == 'nt':  # Windows
            os.system("del /Q .\\data\\*")
            os.system("rmdir /S /Q .\\robots\\*")
        else:  # Linux and macOS
            os.system("rm -rf ./data/*")
            os.system("rm -rf ./robots/*")
        success("Dane zostały wyczyszczone")
    if response == "5":
        mergedata()
    if response == "6":
        warn("Usuwanie wszystkich dokumentów...")
        action = user_input("Czy na pewno chcesz to zrobic? (y/N): ")
        if action.lower() == "y" or action.lower() == "tak":
            success("Wybrano tak")
        else:
            error("Abort")
            return
        deletealldocuments()


def start():
    info("Start Programu")
    checkFolders()
    info("Zaczęto sprawdzanie dependencies...")
    checkDependency()
    success(f"Zakończono szukanie dependencies")
    print()
    chooseAction()

def checkFolders():
    if not os.path.exists("./robots"):
        error("Folder `robots` nie istnieje")
        os.makedirs("./robots")
        success("Folder `robots` został utworzony")
    if not os.path.exists("./data"):
        error("Folder `data` nie istnieje")
        os.makedirs("./data")
        success("Folder `data` został utworzony")

start()