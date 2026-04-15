import sys

def count_lines():
    count = 0
    for _ in sys.stdin:
        count += 1
    print(count)

if __name__ == "__main__":
    count_lines()