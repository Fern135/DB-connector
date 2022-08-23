import random
import datetime
import string
from this import d
import colorama
import json
import platform
import os
#region validating email
import re
from validate_email_address import validate_email
#endregion
# import time
from os import system, name
from colorama import Fore
# from os.path import exists

# region global variables
colorama.init(autoreset=True)


# for the coloring the console for debugging
success = Fore.GREEN
warning = Fore.YELLOW
error = Fore.RED

GEN_API_KEY_CHOOSE = string.ascii_uppercase + string.digits + \
    string.ascii_lowercase + string.punctuation + string.ascii_letters

COMMANDS = {
    "pip-linux": "python3 -m pip install --upgrade pip",
    "pip-windows": "python -m pip install --upgrade pip",
    # <=======================> this is an external package for updating the packages
    "update-package": "pip-review --auto",
    # <=============================> this is an external package for Decrypting what needs to be updated
    "Decrypt-package": "pip-Decrypt",
    "windows-cls": "cls",
    "linux-cls": "clear",
}


OS_SUPPORTED = {
    "mac": "Darwin",
    "linux": "Linux",
    "windows": "Windows"
}


#region getting basic time, date, month, by day, weekday
def get_time():  # * get full 12 hour time
    return f'{datetime.datetime.now().strftime("%I")} : {datetime.datetime.now().strftime("%M")} {datetime.datetime.now().strftime("%p")}'


def get_Date():  # * get full date
    return datetime.datetime.now().strftime("%x")


def getMonth():  # * full name of month
    return datetime.datetime.now().strftime("%B")


def getMonthDay():  # * get the day of the month
    return datetime.datetime.now().strftime("%d")


def getWeekDay():  # * get fullname of the weekday
    return datetime.datetime.now().strftime("%A")

#endregion


#region basic utilities
def generateAPIKey(Size:int) -> str:  # * generating the random api key and saving it with each user
    return ''.join(random.choice(GEN_API_KEY_CHOOSE) for _ in range(Size))


def openJson(title, json_usage='r'):  # * opening json file
    with open(f'{title}.json', json_usage) as f:
        return json.load(f)


def writeJson(title, data=None, writeType='w', indents=4):
    if data is None:
        data = {}

    # w for write. a whole new file,
    # a for appending to the end of the file
    with open(f'{title}.json', writeType) as f:
        json.dump(data, f, indent=indents)


def rnd(max: int):  # * random number generator default min = 1
    return random.randint(1, max)


def rnd(min: int, max: int):  # * random number generator between min and max
    return random.randint(min, max)


def evenRnd(min: int, max: int, step=2):  # generating random even numbers
    return random.randint(min, max, step)


def oddRnd(min: int, max: int, step=3):  # generating random odd numbers
    return random.randint(min, max, step)


def toInt(data) -> int:  # type casting data to int
    return int(data)


def toFloat(data) -> float:  # type casting data to Float
    return float(data)


def toString(data) -> str:  # type casting data to String
    return str(data)


def cls():  # * clear the console
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#endregion


def getPcDevOs():  # getting the os that the pythong script is runTerminalCommand on
    return platform.system()


def delFile(title: str):  # deleting specific file with title
    if os.path.exists(title):
      os.remove(title)
    else:
        print("The file does not exist")


def runTerminalCommand(command:str):  # runTerminalCommand terminal commands
    os.system(command)


def update_packages():  # auto updater to be used in development
    try:
        if getPcDevOs() == OS_SUPPORTED['linux'] or getPcDevOs() == OS_SUPPORTED['mac']:
            runTerminalCommand(COMMANDS["pip-linux"])
            # runTerminalCommand(COMMANDS["Decrypt-package"]) # Decrypting first what needs to be updated
            # update any packages that need updating
            runTerminalCommand(COMMANDS["update-package"])

        elif getPcDevOs() == OS_SUPPORTED['windows']:
            runTerminalCommand(COMMANDS["pip-windows"])
            # runTerminalCommand(COMMANDS["Decrypt-package"]) # Decrypting first what needs to be updated
            # update any packages that need updating
            runTerminalCommand(COMMANDS["update-package"])

        else:
            print(f" * {error}Unables to get os")

    except Exception as e:
        print(f" * {error}Error: {str(e)}")


#region advanced utilities

# get's how many numbers in the list are above and bellow the compare
def aboveBellow(compare, myList=None):

    if myList is None:
        myList = []

    above = 0
    bellow = 0

    for i in myList:
      if i < compare:
        bellow += 1

      elif i > compare:
        above += 1

      else:
        return ("this else statement should not reach here.\nIn theory\nif it does. sorry")

    # wanted to get fancy. un coment this for it to be written in a file
    # self.write(
    #   {
    #     "above": above,
    #     "bellow": bellow
    #   }
    # )

    return json.dumps(
        {
            "above": above,
            "bellow": bellow
        }
    )


# rotate string char to the right rotateTimes times
def rotateRight(data: str, rotateTimes: int):
    return data[-rotateTimes:] + data[:-rotateTimes]


def addStrings(string_A, string_B, defaultAdd=' + '):  # adding 2 strings and returning it
    return str(string_A + defaultAdd + string_B)


def split(str_A: str, defaultSplit=' + '):  # spliting a string and returning the list
    return str_A.split(defaultSplit)


#endregion

#region basic sorting and searching
def sort(arr=None):  # returns sorted list or aka array
    if arr is None:
        arr = []
    return sorted(arr)


def search(Search, arr=None) -> bool:  # returning true or false if Search is found in arr
    if arr is None:
        arr = []
    return Search in arr


def search(Search, In) -> bool:  # returning true or false if Search is found in In
    return Search in In

#endregion


def valEmail(email):  # validating if the email is valid or not
    # validating email and more
    REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # check if email is in proper format
    checkedEmail = re.fullmatch(REGEX, email)

    if not validate_email(checkedEmail, verify=True):
        return False
    else:
        return True
