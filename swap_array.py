def swapArr(A, D, N):
    temp = []
    for i in range(D):
        temp.append(A[i])
    for j in range(D):
        del A[0]
    for x in range(D):
        A.append(temp[x])
    
    return A

a = [1, 2, 3, 4, 5]
d = 2
n = 5
output = swapArr(a, d, n)
print(output, end="\n")