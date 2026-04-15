def get_prize(rank, prize_table):
    for max_rank, prize in prize_table:
        if rank <= max_rank:
            return prize
    return 0

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    # Define prize tables
    festival1 = [
        (1, 5000000),
        (3, 3000000),
        (6, 2000000),
        (10, 500000),
        (15, 300000),
        (21, 100000)
    ]
    festival2 = [
        (1, 5120000),
        (3, 2560000),
        (7, 1280000),
        (15, 640000),
        (31, 320000)
    ]
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        index +=2
        prize1 = get_prize(a, festival1) if a >0 else 0
        prize2 = get_prize(b, festival2) if b >0 else 0
        total = prize1 + prize2
        print(total)

if __name__ == "__main__":
    main()