from collections import deque


def main():
    N, M = map(int, input().split())

    a = tuple(map(int, input().split()))

    know_truth = [False for _ in range(N + 1)]

    queue = deque()

    for i in a[1:]:
        know_truth[i] = True
        queue.append(i)

    party = []

    for _ in range(M):
        party.append(list(tuple(map(int, input().split()))[1:]))

    if a[0] == 0:
        print(M)
        return

    while queue:
        p = queue.popleft()
        for i in range(M):
            if p in party[i]:
                for j in party[i]:
                    if not know_truth[j]:
                        queue.append(j)
                        know_truth[j] = True

    fake_parties = 0

    for p in party:
        fake_party = True
        for i in p:
            if know_truth[i]:
                fake_party = False
                continue
        if fake_party:
            fake_parties += 1

    print(fake_parties)


if __name__ == "__main__":
    main()
