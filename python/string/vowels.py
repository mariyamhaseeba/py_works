text="eight five four Out"
vowels=["a","e","i","o","u"]
word=text.split(" ")
for w in word:
    if w[0].casefold() in vowels:
        print(w)