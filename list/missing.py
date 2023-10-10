num=[1,2,4,6,7,8]
num.sort()
# print(num)
for i in range(1,len(num)):
    if i not in num:
        print(i,"is missing")