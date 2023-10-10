# num=324
# sum=0
# while(num!=0):
#     last_digit=num%10
#     sum=sum+last_digit
#     num=num//10
# print(sum)

num=153
orginal=num
sum=0
while(num!=0):
    last_digit=num%10
    cube=last_digit**3
    sum=sum+cube
    num=num//10
if sum==orginal:
    print("arm")
else:
    print("non")