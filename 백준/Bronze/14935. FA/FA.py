def is_fa_number(x: str) -> str:
    seen = set()
    while x not in seen:
        seen.add(x)
        first_digit = int(x[0])
        num_digits = len(x)
        x = str(first_digit * num_digits)
    return "FA"

# 입력
x = input().strip()
print(is_fa_number(x))
