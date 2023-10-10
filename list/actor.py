all=["mammotty","mohanlal","nivin","fahad","unni"]
nivin=["fahad","unni"]
req=[]
for n in all:
    if n not in nivin:
        req.append(n)
req.pop(req.index("nivin"))
print(req)