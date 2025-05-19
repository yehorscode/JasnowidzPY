from utils.logmanager import error, warn, success, info, user_input
import os
def checkDependency():
    hasRequests = None
    hasSoup = None
    hasAppwrite = None
    hasColorama = None
    hasTQDM = None
    try:
        import tqdm
        hasTQDM = True
    except ImportError:
        hasTQDM = False
        error("Brak modulu tqdm")
    try:
        import colorama
        hasColorama = True
    except ImportError:
        hasColorama = False
        error("Brak modulu colorama")
    try:
        import requests
        hasRequests = True
    except ImportError:
        hasRequests = False
        error("Brak modulu requests")

    try:
        from bs4 import BeautifulSoup
        hasSoup = True
    except ImportError:
        hasSoup = False
        error("Brak modulu bs4")

    try:
        from appwrite.client import Client
        hasAppwrite = True
    except ImportError:
        hasAppwrite = False
        error("Brak modulu appwrite")

    if hasRequests and hasSoup and hasAppwrite and hasColorama and hasTQDM:
        success("Wszystkie zaleznosci sa zainstalowane")
    else:
        if user_input("Autorozwiązanie? (y/n)") == "y":
            success("Rozpoczynanie autoinstalacji...")
            os.system("pip install -r requirements.txt")
            warn("Włącz ponownie skrypt")
        else:
            warn("Abort")
    return hasRequests, hasSoup, hasAppwrite, hasColorama, hasTQDM
