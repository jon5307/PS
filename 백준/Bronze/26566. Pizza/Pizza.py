import math

n = int(input())
for _ in range(n):
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())
    
    slice_value = A1 / P1
    whole_value = (math.pi * R1 * R1) / P2
    
    if whole_value > slice_value:
        print("Whole pizza")
    else:
        print("Slice of pizza")