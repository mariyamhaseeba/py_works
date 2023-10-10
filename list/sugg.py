all=["sachin","dhoni","kohli","rohit","sanju","padikkal"]
sanju=["padikkal","sachin"]
sugg=[]
for a in all:
    if a not in sanju:
        sugg.append(a)
sugg.pop(sugg.index("sanju"))
print(sugg)