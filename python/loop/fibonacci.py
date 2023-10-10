limit=int(input("enter the limit = "))
start=1
previous=0
current=1
print(previous)
print(current)
while(start<=limit):
    sum=previous+current
    previous=current
    current=sum
    print(sum)
    start=start+1