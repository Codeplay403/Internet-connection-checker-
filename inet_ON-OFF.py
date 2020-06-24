import time
import os
from urllib.request import urlopen
os.system("clear")

banner = """\033[1;92m
_________________
< Internet Status >
 -----------------
"""
print(banner)

print(" Author: EɾrØrC͢͢͢Ø∂e ")
print(" Github: https://github.com/Codeplay403")
time.sleep(1)
print("")
print("")

def google_ok():
    try:
        urlopen('https://www.google.com', timeout=10);
        return True
    except:
        return False


def yahoo_ok():
    try:
        urlopen('https://www.yahoo.com', timeout=10);
        return True
    except:
        return False


if google_ok() or yahoo_ok():
    print ('\033[1;96m    [*] Internet Status:\033[1;94m Online');
    print ();

else:
    print ('\033[1;96m    [*] Internet Status:\033[1;91m Offline')
