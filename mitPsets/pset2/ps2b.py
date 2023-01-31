#hours spent = 0:00
#name: dominic denti

"""this solves all diophantine equations assuming ai + bj + ck = n
"""
def diophantineEquations(x,arr):
    for a in range(2):
        assert arr[a] > 0, "all inputs must be non-zero positive integers line-8"
    for i in range(int(x/arr[0]) + 1):
        for j in range(int(x/arr[1]) + 1):
            for k in range(int(x/arr[2]) + 1):
                if(i*arr[0] + j*arr[1] + k*arr[2] == x):
                    return [k,j,i], True, x
    return False, x

n = int(input("enter a number: "))
assert n > 0, "input int must be >= 1 line-17"
arr = []
x = int(input("enter x: "))
y = int(input("enter y: "))
z = int(input("enter z: "))
tupl = (x,y,z)

for i in range(1, n):
    result = diophantineEquations(i,tupl)
    if(result[0] == False):
        arr.append(i)
print(f"Given package sizes {x}, {y}, and {z}, the largest number of McNuggets that cannot be bought in exact quantity is: {arr[-1]}")