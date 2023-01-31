#hours spent = 0:30
#name: dominic denti

"""this solves all diophantine equations assuming a6 + b9 + c20 = n
"""
def diophantineEquations(x,arr):
    for i in range(int(x/arr[0]) + 1):
        for j in range(int(x/arr[1]) + 1):
            for k in range(int(x/arr[2]) + 1):
                if(i*arr[0] + j*arr[1] + k*arr[2] == x):
                    return [k,j,i], True, x
    return False, x

for i in range(1,66):
    print(diophantineEquations(i, [6,9,20]))