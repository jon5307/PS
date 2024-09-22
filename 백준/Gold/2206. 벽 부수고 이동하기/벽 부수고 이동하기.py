from sys import stdin
from collections import deque

input = stdin.readline


def main():
    n, m = map(int, input().rstrip().split())
    ma = [input().rstrip() for _ in range(n)]

    q = deque()
    q.append((0, 0, 1, False))
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    visited = [[(0, 0) for _ in range(m)] for _ in range(n)]
    visited[0][0] = (1, 0)

    while q:
        x, y, distance, breaked = q.popleft()
        if x == n - 1 and y == m - 1:
            print(distance)
            return
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < m:
                if ma[nx][ny] == "0":
                    v, bv = visited[nx][ny]
                    # 안 부수고 갔던 경우에서 안부수고 갈 수 있는 경우
                    if not breaked and v == 0:
                        visited[nx][ny] = (1, bv)
                        q.append((nx, ny, distance + 1, False))
                    # 부수고 갔던 경우
                    elif breaked and v == 0 and bv == 0:
                        visited[nx][ny] = (0, 1)
                        q.append((nx, ny, distance + 1, True))
                else:
                    # 막혀있으므로 한번도 안뚫은 경우만 지나갈 수 있다.
                    if not breaked:
                        visited[nx][ny] = (0, 1)
                        q.append((nx, ny, distance + 1, True))
    print(-1)
    return


main()
