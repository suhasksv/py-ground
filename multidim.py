# from array import *
# matrix = [[1,2,3], [4,5,6], [44,55,66],[14,15,16]]
matrix = [[1, 2], [4, 5]]
matrix1 = [[11, 22], [44, 55]]

oneda = [3, 4, 5, 6, 7, 8]

# matrix = matrix+matrix1

for i, k in zip(matrix, matrix1):
    for j, l in zip(i, k):
        print((j + l), end="\t")
    print(end="\n")
