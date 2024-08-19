"""
pyimager.utils
Submodule for pyimagers utils

temp_uncompress -- uncompresses lkim-data temporarily
countDif -- counts different characters in strings
"""
def countDif(str1: str, str2: str):
    """
    Counts how many different characters are in two strings.
    """
    a = []
    for i in str1+str2:
        if i not in a:
            a.append(i)
    return len(a)

def listComb(list1: list, list2: list, skipCheck: bool = False):
    """
    Returns a list with all possible combinations of elements of list1 and list2.
    skipCheck -- skips check of the two elements have the same characters.
    """
    retList = []
    for i in list1:
        for j in list2:
            if countDif(i, j) > 1 or skipCheck:
                retList.append(i+j)
    return retList