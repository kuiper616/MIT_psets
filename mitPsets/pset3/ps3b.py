# hours spent = 0:10
# name = dominic denti

def subStringMatchExact(target, key):
    x = 0
    j = []
    for i in range(len(key)):
        if(x == len(target)):
            j.append(i - len(target))
            x = 0
        if(key[i] != target[x]):
            x = 0
        if(key[i] == target[x]):
            x += 1
    return tuple(j)
