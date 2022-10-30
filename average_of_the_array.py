n=int(input())
lst=list(map(int,input().split()))
def average(lst):
    avg=sum(lst)/len(lst)
    return avg
print('%.2f'%(average(lst)))