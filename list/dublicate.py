lst=[1,2,3,3,1,5,4,9]
dup=[]
lst.sort()
for n in range(0,len(lst)-1):
    n1=lst[n+1]
    n2=lst[n]
    if n1==n2:
        if n1 not in dup:
            dup.append(n1)
print(dup)