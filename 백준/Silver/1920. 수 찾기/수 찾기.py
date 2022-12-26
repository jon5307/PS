# fuction that checks num is in the sorted list
def binarysearch(num, n):
    start = 0
    end = len(n) - 1
    while start <= end:
        mid = (start + end) // 2
        if n[mid] == num:
            return True
        elif n[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return False

    
    
def solve():
    input()
    n = list(map(int,input().split()))
    n.sort()
    input()
    for i in map(int,input().split()):
        if binarysearch(i,n):
            print("1")
        else:
            print("0")

if __name__ == "__main__":
    solve()
