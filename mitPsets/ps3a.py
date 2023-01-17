# hours spent = 0:45
# name = dominic denti

def countSubStringMatch(target, key):
    x = 0
    j = 0
    for i in range(len(key)):
        if(x == len(target)):
            j += 1
            x = 0
        if(key[i] != target[x]):
            x = 0
        if(key[i] == target[x]):
            x += 1
    return j


def countSubStringMatchRecursive(target, key, matchs=0,stringMatchCounter=0):
    assert len(target) > 0, "must enter a valid target"
    if(key == ""):
        return stringMatchCounter
    if(matchs == len(target)):
        stringMatchCounter += 1
        matchs = 0
    if(key[0] == target[matchs]):
        matchs += 1
    else: 
        matchs = 0
    key = key[1:len(key)]
    return countSubStringMatchRecursive(target, key, matchs, stringMatchCounter)
print(countSubStringMatchRecursive("10","hello, World!"))