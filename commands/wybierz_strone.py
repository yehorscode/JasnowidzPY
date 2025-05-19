from colorama import Fore, Back, Style
from utils.logmanager import get_date, error, warn, success, info, user_input
from strony.scrape_lublineu import scrape_lublineu

def wybierzStrone():
    print(f"{Back.LIGHTWHITE_EX}Wybierz metodę scrapowania:{Style.RESET_ALL}")
    print(f"{Back.RED} 1 {Style.RESET_ALL} - Wszystko (Długo)")
    print(f"{Back.LIGHTYELLOW_EX} 2 {Style.RESET_ALL} - https://lublin.eu/kultura/wydarzenia/")
    print(f"{Back.LIGHTYELLOW_EX} 3 {Style.RESET_ALL} - Sprawdź status stron")
    info(
        "Pamiętaj: Nie włączaj zbyt często albo cię zablokują! Scrapowanie może być długie lub nieść odpowiedzialność prawną!"
    )
    response = user_input("Wybierz: ")
    if response == "1":
        info("Wybrano 1")
        print()
    if response == "2":
        info("Wybrano 2")
        print()
        scrape_lublineu()
    if response == "3":
        info("Wybrano 3")
        print()
