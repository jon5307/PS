from sys import stdin

input = stdin.readline


def lcm(a, b):
    m = a * b
    while b != 0:
        r = a % b
        a = b
        b = r
    return m // a


def ky():
    m, n, x, y = map(int, input().split())
    m_year = x
    n_year = y
    max_year = lcm(m, n)
    while m_year <= max_year and n_year <= max_year:
        if m_year < n_year:
            m_year += m
        elif n_year < m_year:
            n_year += n
        else:
            return m_year
    return -1


for _ in range(int(input())):
    print(ky())
