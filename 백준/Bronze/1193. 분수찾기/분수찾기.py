no = int(input())
line = 1
while (line + 1) * (line / 2) < no:
    line += 1
line -= 1
rest = int(no - (line + 1) * (line / 2))
if line % 2 == 0:
    print(line-rest+2,"/",rest,sep="")
else:
    print(rest,"/",line-rest+2,sep="")