n=int(input())
lst=list(map(int,input().split()))
check=int(input())
if check in lst:
    print('True')
else:
    print('False')