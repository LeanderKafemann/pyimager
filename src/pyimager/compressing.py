"""
pyimager.compressing
Submodule for compressing lkims

compress -- compresses image file
decompress -- decompresses image file
compressor -- compresses whole file anew
temp_uncompress -- estimates uncompressed color code with given args
listComb -- returns a list with all combinations of two elements of two lists
addComb6 -- add comb6 list to combList

comb6included - var saves if comb6 has been included in combList
"""
from .utils import listComb

comb6included = False #initialize boolean value if comb6 list has been added
                
comb1 = list("abcdefghijklmnopqr")
comb2 = listComb(comb1, comb1); comb2_ = listComb(comb1, comb1, True)
comb3 = listComb(comb2_, comb1); comb3_ = listComb(comb2_, comb1, True)
comb4 = listComb(comb2_, comb2_)
comb5 = listComb(comb2_, comb3_)
"""
comb6 = listComb(comb3, comb3)
print("6")
comb7 = listComb(comb4, comb3)
print("7")
comb8 = listComb(comb4, comb4)
print("8")
comb9 = listComb(comb5, comb4)
"""
combList = comb5+comb4+comb3+comb2+comb1 #initialize list of possible combinations of lkim code elements
"""
the long-term limit list is 9 because at 10 signs the normal, 1-sign compression is more efficient in most of the cases
 (noone would create an image with a abcdefghij sequence repeating itself at least 5 times)   
currently, the limit is 5 for efficiency reasons
 however, you can still activate the includeComb6 statemente while compressing
 but be aware that this will cost some time for making the comb6 list
the combX_ lists are lists with also elements like aaa
 which must not be in the combX lists but must be part of the list1/2 elements for new combX lists
"""

def addComb6(overrideC6I: bool = False):
    """
    Adds comb6 permanently to combList.
    This saves time if you want to compress multiple images with comb6,
    but costs time, if the images don't contain lkim element combs of length 6.
    overrideC6I -- adds comb6 list even if it was already added
    """
    global combList, comb6included
    if not comb6included or overrideC6I:
        combList = listComb(comb3_, comb3_)+combList
        comb6included = True

def temp_uncompress(data: str, sgn: str, sgn_codec: int):
    """
    Uncompresses content of data, but only uncompresses codecs with given sign.
    Replaces it with sgn_codec times the content of the compression element.
    """
    sgn_found = []
    for i in range(len(data)):
        if data[i] == sgn:
            sgn_found.append(i)
    sgn_found_tpl = []
    for i in range(int(len(sgn_found)/2)):
        sgn_found_tpl += [(sgn_found[2*i], sgn_found[2*i+1])]
    if len(sgn_found_tpl) == 0:
        return data
    betw = data[sgn_found_tpl[0][0]+1:sgn_found_tpl[0][1]]
    data_new = data[:sgn_found_tpl[0][0]] + sgn_codec*betw
    sgn_found_tpl.pop(0)
    for i in sgn_found_tpl:
        betw = data[i[0]+1:i[1]]
        idx = sgn_found.index(i[0]) - 1
        data_new += data[sgn_found[idx]+1:i[0]] + sgn_codec*betw
    data_new += data[sgn_found[-1]+1:]
    return data_new

def compress(path: str, target: str = "", includeComb6: bool = False):
    """
    Compresses LKIM with replacing frequent pixels.
    If target is left empty, the given file gets overwritten.
    includeComb6 -- if this value is set to True, the listComb list
                    is combined with the comb6, but making the comb6 list may cost some time.
                    It will not be added if addComb6 has been executed.
    """
    with open(path, "r", encoding="utf-8") as f:
        im = f.read()
    combList_ = combList.copy()
    if includeComb6 and not comb6included:
        combList_ = listComb(comb3_, comb3_)+combList_
    for i in combList_:
        im = im.replace(i*50, f"§{i}§")
        im = im.replace(i*20, f"&{i}&")
        im = im.replace(i*10, f"%{i}%")
        im = im.replace(i*5, f"${i}$")
    if target == "":
        target = path
    with open(target, "w", encoding="utf-8") as f:
        f.write(im)

def decompress(path: str, target: str = ""):
    """
    Decompresses LKIM with replacing frequent pixels.
    If target is left empty, the given file is overwritten.
    """
    with open(path, "r", encoding="utf-8") as f:
        im = f.read()
    sizes, data = im.split("#**#")
    data = temp_uncompress(data, "$", 5)
    data = temp_uncompress(data, "%", 10)
    data = temp_uncompress(data, "&", 20)
    data = temp_uncompress(data, "§", 50)
    if target == "":
        target = path
    with open(target, "w", encoding="utf-8") as f:
        f.write(sizes+"#**#"+data)

def compressor(path: str, target: str = "", includeComb6: bool = False):
    """
    Decompresses and then compresses LKIM anew.
    If target is left empty, the given file is overwritten.
    Read more about (de-/)compressing in the functions documentation.
    """
    if target == "":
        target = path
    decompress(path, target)
    compress(target, target, includeComb6)
