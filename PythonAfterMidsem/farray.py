def parray(arr):
    n=len(arr)
    for i in range(0,n):
        print(arr[i]," ", end="")
    print("")


def sarray(arr):
    arr2=sorted(arr)
    n=len(arr)
    for i in range(0,n):
        print(arr2[i]," ", end="")
    print("")