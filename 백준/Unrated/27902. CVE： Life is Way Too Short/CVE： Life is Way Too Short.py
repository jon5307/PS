import sys

sys.set_int_max_str_digits(0)

a = 2 ** int(input())

if len(str(a)) <= 4300:
    print(a)
