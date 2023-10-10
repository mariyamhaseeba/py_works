# for row in range(1,4,1):
#   for cols in range(1,row):
#     print("#",end="\t")
#   print()

for r in range(1,4):
    for c in range(4-r):
        print("#", end="\t")
    print() 

for r in range(1,4):
    for c in range(r):
        print("#", end="\t")
    print() 