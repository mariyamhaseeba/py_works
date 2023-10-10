number=int(input("enter the number = "))
sum=0
org=number
l=len(str(number))
while(number!=0):
    last_digit=number%10
    cube=last_digit**l
    sum=sum+cube
    number=number//10
if sum==org:
    print("armstrong")
else:
    print("not armstrong")
    