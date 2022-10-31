def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
n=int(input())

m=list(map(int,input().split()))
hcf=gcd(m[0],m[1])
for i in range(1,n):
    hcf =gcd(hcf,m[i])
print(hcf)