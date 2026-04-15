sleep_time = int(input())
wake_time = int(input())

if wake_time < sleep_time:
    wake_time += 24

print(wake_time - sleep_time)