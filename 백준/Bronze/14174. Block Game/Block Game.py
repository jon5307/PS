import sys

def count_max_letters(boards, n):
    max_letter_count = [0] * 26
    
    for i in range(26):
        letter = chr(i + ord('a'))
        max_count = 0
        
        for board in boards:
            count1 = board[0].count(letter)
            count2 = board[1].count(letter)
            max_count += max(count1, count2)
        
        max_letter_count[i] = max_count
    
    return max_letter_count

def main():
    n = int(sys.stdin.readline().strip())
    boards = [tuple(sys.stdin.readline().strip().split()) for _ in range(n)]
    
    max_letter_count = count_max_letters(boards, n)
    
    for count in max_letter_count:
        print(count)

if __name__ == "__main__":
    main()
