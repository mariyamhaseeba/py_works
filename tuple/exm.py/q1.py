text="pycharm is an ide"
vowelcount=0
consonantcount=0
c_count=0
t=text.split(" ")
print(t)
for ch in t:
   c_count+=1

for ch in text:
   if ch in['a','e','i','o','u']:
      vowelcount+=1
   else:
      consonantcount+=1


print("c_count:",c_count)
print("vowel_count:",vowelcount)
print("consonant count:",consonantcount)
    


