lst=[1,2,3,5,6,7,8,4]
odd=[]
even=[]
for i in range(1,len(lst)):
    if lst[i]%2==0:
        even.append(lst[i])
    else:
        odd.append(lst[i])
print("even",even)
print("odd",odd)