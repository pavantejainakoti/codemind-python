N=int(input())
lst=list(map(int,input().split()))
def average(lst):
    a=sum(lst)//len(lst)
    return a
avg=average(lst)
if avg in lst:
    print(True)
else:
    print(False)