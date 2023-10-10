num=int(input("enter the number = "))
previous=0
current=1
start=1
is_present=False
fibon=0
# print(previous)
# print(current)
while(fibon<=num):
    fibon=previous+current
    if fibon==num:
     is_present=True
     break
    previous=current
    current=fibon
    start=start+1
print(is_present)
    