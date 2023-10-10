text="CHICKEN"
out="HEN"
wc={}
is_kangaroo=True
for ch in text:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1
# print(wc)
for ch in out:
    if ch in wc:
        current=wc[ch]
        if current>0:
            wc[ch]-=1
            is_kangaroo=True
        else:
            is_kangaroo=False
print(is_kangaroo)