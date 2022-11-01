n=int(input())
m=int(input())
for i in range(n,m+1):
    rev=0
    tem=i
    while i>0:
        r=i%10
        rev=rev*10+r
        i=i//10
    if tem == rev:
        print(tem,end=' ')