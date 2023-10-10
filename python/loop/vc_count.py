text="coffeeee"
c_count=0
v_count=0
vowels={"a","e","i","o","u"}
for ch in text:
    if ch in vowels:
        v_count=v_count+1
    else:
        c_count=c_count+1
print(v_count,"vowels")
print(c_count,"consonants")