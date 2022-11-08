n=int(input())
sq=n*n
digit=pow(10,len(str(n)))
if sq % digit== n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")