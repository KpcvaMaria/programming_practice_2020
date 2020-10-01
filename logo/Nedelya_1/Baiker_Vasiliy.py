v=int(input())
t=int(input())
s=abs(v*t)
if v>0:
    print(s%109)
else:
    print(109-(s%109))


