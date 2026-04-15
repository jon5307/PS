while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == 0 and a2 == 0 and a3 == 0:
        break

    if a2 - a1 == a3 - a2:
        d = a2 - a1
        print(f"AP {a3 + d}")
    else:
        r = a2 // a1
        print(f"GP {a3 * r}")
