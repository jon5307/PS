a = -(int(input())-int(input()))
if a<1:
    print("Congratulations, you are within the speed limit!")
else:
    print("You are speeding and your fine is $",end="")
    if 0<a<21:
        print(100,end="")
    elif 20<a<31:
        print(270,end="")
    else:
        print(500,end="")
    print(".")