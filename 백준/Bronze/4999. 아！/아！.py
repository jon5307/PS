# 첫째 줄에서 재환이가 낼 수 있는 "aaah"의 길이를 입력받는다.
jaehwan = input()

# 둘째 줄에서 의사가 듣기를 원하는 "aah"의 길이를 입력받는다.
doctor = input()

# 재환이가 낼 수 있는 "aah"의 길이와 의사가 요구하는 길이를 비교하여 출력한다.
if len(jaehwan) >= len(doctor):
    print("go")
else:
    print("no")
    