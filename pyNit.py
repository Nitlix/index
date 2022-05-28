emailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
import re
import random






def valueCheck(e,param):
    for x,y in param.items():
        x = x.lower()
        if isinstance(y, str):
            y = y.lower()
        if x == "max-length":
            if len(e) > y:
                return True
        if x == "type":
            if not isinstance(e,y):
                return True
        if x == "email":
            if y == True:
                if(not re.fullmatch(emailregex, e)):
                    return True
            else:
                if(re.fullmatch(emailregex, e)):
                    return True
        if x == "colour":
            if y == "hex":
                if not re.search(r'^(?:[0-9a-fA-F]{3}){1,2}$', e):
                    return True






    return False

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

