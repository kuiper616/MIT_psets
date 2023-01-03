#hours spent = 5:00
#name = dominic denti
def Prime(x):
    arr = [2]
    i = 2
    for n in range(x * 100):
        if(len(arr) == x):
            #when arr is of length == to x then you have found the xth prime
            print(arr)
            return arr[-1]
        for k in range(len(arr)+1):
            if(k >= len(arr)):
                #if k > length of array then i must be prime
                arr.append(i)
                i += 1
                break
            if(i%arr[k] == 0):
                #if i%arr[k] == 0 then i is compesite
                i += 1
                break
print(Prime(1000))
