import pip
import datetime
import requests
import time
import multiprocessing
import msvcrt
import sys

ci = False
try:
    import termcolor
except Exception:
    ci = True

#Timeout exception
#Internal Functions Below
class TimeoutExpired(Exception):
    pass


def install(package):
    package = str(package)
    if not ci:
        print(f"[{termcolor.colored('N.PY','red')}] Installing module... [{package}]")
    else:
        print(f"[N.PY] Installing module... [{package}]")
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

if ci:
    install("termcolor")
    import termcolor
    ci = False

try:
    import multiprocessing
except Exception:
    install("multiprocessing")
    import multiprocessing


try:
    import msvcrt
except Exception:
    install("msvcrt")
    import msvcrt



def input_with_timeout(prompt, timeout, timer=time.monotonic):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    endtime = timer() + timeout
    result = []
    while timer() < endtime:
        if msvcrt.kbhit():
            result.append(msvcrt.getwche())
            if result[-1] == '\r':
                return ''.join(result[:-1])
        time.sleep(0.04) 
    raise TimeoutExpired






if __name__ != "__main__":
    print(termcolor.colored('''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░███╗░░██╗██╗████████╗██╗░░░░░██╗██╗░░██╗░░░██████╗░██╗░░░██╗░
░░████╗░██║██║╚══██╔══╝██║░░░░░██║╚██╗██╔╝░░░██╔══██╗╚██╗░██╔╝░
░░██╔██╗██║██║░░░██║░░░██║░░░░░██║░╚███╔╝░░░░██████╔╝░╚████╔╝░░
░░██║╚████║██║░░░██║░░░██║░░░░░██║░██╔██╗░░░░██╔═══╝░░░╚██╔╝░░░
░░██║░╚███║██║░░░██║░░░███████╗██║██╔╝╚██╗██╗██║░░░░░░░░██║░░░░
░░╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

                Thank you for using nitlix.py!
                          nitlix.pro
    ''','cyan',
    ))






#Off to some Google Kickstarts? :)
#Use this function to scan multiline inputs
#INPUT: Multiline paste or enter
#OUTPUT: List of input lines



def scanMutliInput():
    d = []
    w = 0
    s = True
    f = True
    while s:
        if len(d) == 1:
            f = False
        try:
            if f:
                a = input_with_timeout('', 100)
            else:
                a = input_with_timeout('', 1)
        except TimeoutExpired:
            if f:
                f = False
            else:
                break
        else:
            d.append(a)
    return d


