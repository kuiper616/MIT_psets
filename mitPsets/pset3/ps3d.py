# hours spent = 0:50
# name = dominic denti

from string import *

def subStringMatchExact(target,key):
    x = 0
    j = []
    if(key == ""):
        return ()
    for i in range(len(target)-1):
        if(x == len(key)):
            j.append(i - len(key))
            x = 0
        if(target[i] != key[x]):
            x = 0
        if(target[i] == key[x]):
            x += 1
    return tuple(j)

def constrainedMatchPair(firstMatch,secondMatch,exactMatchArray):
    n = []
    for i in range(len(firstMatch)):
        for j in range(len(secondMatch)):
            if(firstMatch[i] in exactMatchArray):
                break
            if(firstMatch[i] == secondMatch[j] + 2):
                n.append(firstMatch[i])
    return tuple(n)

def subStringMatchExactlyOneSub(target,key): 
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print ('breaking key',key,'into',key1,key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        j = subStringMatchExact(target,key)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,j)
        allAnswers = allAnswers + filtered
        print ('match1',match1)
        print ('match2',match2)
        print ('possible matches for',key1,key2,'start at',filtered)
    return allAnswers
print(subStringMatchExactlyOneSub('tcgtatgagcagg','atg'))