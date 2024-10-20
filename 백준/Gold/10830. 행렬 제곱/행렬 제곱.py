from sys import stdin
from collections import deque

input = stdin.readline

n, b = map(int, input().rstrip().split())

matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]


def mul_matrix(matrix1, matrix2):
    n = len(matrix1)
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return new_matrix


def divide_element(matrix, divider):
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix[i][j] % divider
    return new_matrix


def dnc(matrix, b):
    if b == 1:
        return divide_element(matrix, 1000)
    multiplied = mul_matrix(matrix, matrix)
    if b % 2 == 0:
        return dnc(divide_element(multiplied, 1000), b // 2)
    else:
        return divide_element(mul_matrix(dnc(multiplied, b // 2), matrix), 1000)


result = dnc(matrix, b)
for row in result:
    print(" ".join(map(str, row)))
