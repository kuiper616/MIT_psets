#hours spent = 1:00
#name = dominic denti

from math import *

def Prime(prime): 
    primeArr = [2]
    it = 2 #it is short for iterator
    for n in range(prime * 100):
        if(len(primeArr) == prime):
            #when arr is of length == to prime then you have found the primeth prime
            return primeArr
        for m in range(len(primeArr)+1):
            if(m >= len(primeArr)):
                #if m > length of array then it must be prime
                primeArr.append(it)
                it += 1
                break
            if(it%primeArr[m] == 0):
                #if it%primeArr[m] == 0 then it is compesite
                it += 1
                break

def logPrimes(ttr): #ttr = times to run
    PrimeArr = Prime(ttr)
    ratioArr = []
    for n in range(ttr):
        PrimeArr[n] = log(PrimeArr[n])
        if(n >= 1):
            ratioArr.append(PrimeArr[n-1]/PrimeArr[n])
    return ratioArr
x = 10
print(logPrimes(x))