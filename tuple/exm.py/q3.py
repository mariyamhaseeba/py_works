
list1 = [10,11,13,15]
list2 = [9,8,11,13,14]
list1.sort()
list2.sort()
p1,p2=0,0

while(p1<len(list1) and p2<len(list2)):
    if list1[p1]==list2[p2]:
        print(list1[p1])
        p1+=1
        p2+=1
    elif list1[p1]<list2[p2]:
        p1+=1
    else:
        p2+=1 
            





