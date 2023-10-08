import re
def solution(s):
    if len(s) == 4 or len(s) == 6:
        search = bool(re.search("^\d*$", s))
        return search
    else :
        return False