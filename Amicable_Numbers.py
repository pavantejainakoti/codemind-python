n=int(input())
m=int(input())
s=a=0
for i in range(1,n):
    if n%i==0:
        s+=i
for j in range(1,m):
    if m%j==0:
        a+=j
if n==a and m==s:
    print('Amicable')
else:
    print('Not Amicable')