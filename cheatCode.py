'''
    Author : Shivam Chauhan
    Date   : Januaray 18 , 2019
    About :
    This project generates words that are actually present in the English Dictionary.
    This can be used to break / or use as a hint for playing a game present on the
    play store namely " Words Connect " .
'''
from itertools import permutations
s = input()
while True :
    n = int(input("Enter the length of words to be found "))
    wordPermutations = set(["".join(p) for p in permutations(s,n)])
    fpath = 'words.txt'
    with open(fpath) as fobj:
        content = fobj.read()
    wordsList = content.strip().split("\n")
    wordsList = [i.lower() for i in wordsList]
    count = 0
    for word in wordPermutations:
        if word.lower() in wordsList:
            print("Word Found buddy!!!",word)
            count += 1
    print("Hey there!!! , you will have to look up ",count,"words")
    if input("Enter -1 to quit || 0 to continue") == "-1":
        break

