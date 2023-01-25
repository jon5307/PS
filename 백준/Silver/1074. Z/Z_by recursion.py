def z(n,r,c,start):
    while n != 1:
        if 2**(n-1) > c: # left side 
            if 2**(n-1) <= r: # down side
                r -= 2**(n-1)
                start += 2**(n*2-1)
        else: # right side
            if 2**(n-1) > r: # up side
                c -= 2**(n-1)
                start += 2**((n-1)*2)
            else: # down side
                r -= 2**(n-1)
                c -= 2**(n-1)
                start += 3*2**((n-1)*2)
        n -= 1
    return start+2*r+c

n,r,c = map(int,input().split())
print(z(n,r,c,0))
