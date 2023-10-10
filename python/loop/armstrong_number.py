
num=153
orginal=num
sum=0
while(num!=0):
    last_digit=num%10
    cube=last_digit**3
    sum=sum+cube
    num=num//10
if sum==orginal:
    print("armstrong")
else:
    print("not armstrong")