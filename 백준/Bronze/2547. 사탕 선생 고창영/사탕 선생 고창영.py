import sys
input = sys.stdin.read

def solve():
    data = input().strip().split('\n')
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        while data[idx] == '':
            idx += 1  # 빈 줄 스킵
        n = int(data[idx])
        idx += 1
        total = 0
        for _ in range(n):
            total = (total + int(data[idx])) % n
            idx += 1
        results.append("YES" if total == 0 else "NO")
    print('\n'.join(results))

solve()