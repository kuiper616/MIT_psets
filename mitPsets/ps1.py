#hours spent = 4:00
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

            if(it >= 1000 and primeArr[m] > sqrt(it)):
                primeArr.append(it)
                it += 1
                break

            if(it%primeArr[m] == 0):
                #if it%primeArr[m] == 0 then it is compesite
                it += 1
                break
idk = input("what prime do you want to find?: ")
print(Prime(int(idk)))
