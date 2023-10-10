a=int(input("enter your age"))
if a<13:
    print("child")
elif(a>=13 and a<=19):
    print("teenager")
elif(a>=20 and a<=59):
    print("adult")
else:
    print("senior citizen")