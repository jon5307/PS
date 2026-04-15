a = input()
b = input()
c = input()
try:
    a_int = int(a)
except:
    a_int = -1
try:
    b_int = int(b)
except:
    b_int = -1
try:
    c_int = int(c)
except:
    c_int = -1

if a_int != -1:
    result = a_int + 3
elif b_int != -1:
    result = b_int + 2
else:
    result = c_int + 1

if result % 15 == 0:
    print("FizzBuzz")
elif result % 3 == 0:
    print("Fizz")
elif result % 5 == 0:
    print("Buzz")
else:
    print(result)
