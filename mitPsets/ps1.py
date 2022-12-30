#hours spent = 1:00
#name = dominic denti
def thousandthPrime(x, i, arr):
    if(len(arr) == x):
        return arr[-1]
    for n in range(0, len(arr)):
        if(i/arr[n] == 1):
            arr.append(i)
            #print(i)
            return thousandthPrime(x, i, arr)
        n += 1
    i += 1
    return thousandthPrime(x, i, arr)
print(thousandthPrime(1000, 2, [2]))