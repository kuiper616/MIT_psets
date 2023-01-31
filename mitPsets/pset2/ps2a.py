#hours spent = 0:20
#name: dominic denti

"""this solves all diophantine equations assuming ai + bj + ck = n
"""
def diophantineEquations(x,arr):
    for i in range(int(x/arr[0]) + 1):
        for j in range(int(x/arr[1]) + 1):
            for k in range(int(x/arr[2]) + 1):
                if(i*arr[0] + j*arr[1] + k*arr[2] == x):
                    return [k,j,i], True, x
    return False, x

n = int(input("enter a number: "))
arr = []
for x in range(1, n+1):
    result = diophantineEquations(x,[20,9,6])
    if(result[0] == False):
        arr.append(x)
print(f"Largest number of McNuggets that cannot be bought in exact quantity: {arr[-1]}")