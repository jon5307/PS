from sys import stdin

input = stdin.readline

key_map = list(map(int, input().split()))
message = input().strip()

t9_dict = {
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

real_keypad = {}
for original_key in range(1, 10):
    real_keypad[key_map[original_key - 1]] = str(original_key)

result = []
prev_key = None

for char in message:
    for key, letters in t9_dict.items():
        if char in letters:
            press_count = letters.index(char) + 1
            actual_key = real_keypad[int(key)]
            break

    if prev_key == actual_key:
        result.append("#")

    result.append(actual_key * press_count)
    prev_key = actual_key

print("".join(result))
