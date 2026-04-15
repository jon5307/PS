n = int(input())
f = int(input())

a = (n//100)*100
for i in range(100):
  if (a+i)%f == 0:
    print('{0:02d}'.format(i))
    break