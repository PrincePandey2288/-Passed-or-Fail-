d=str(input())
t=tuple(map(int,d.split(',')))
c=0
for i in t:
    if i<=35:
        c+=1
if c>=2:
    print("failed")
else:
    print("passed")