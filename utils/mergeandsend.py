from commands.mergedata import mergedata
from utils.logmanager import *
from commands.uploadtoappwrite import uploadtoappwrite

def mergeandsend():
    mergedata()

    response = user_input("Chcesz wysлаć dane do appwrite? (y/N): ")
    if response.lower() == "y" or response.lower() == "tak":
        success("Wybrano tak")
        uploadtoappwrite()
    else:
        error("Abort")