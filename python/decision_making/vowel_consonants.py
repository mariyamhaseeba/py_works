# word=input("enter the word = ").casefold()
# if word[0]=="a":
#     is_a=True
# else:
#     is_a=False
# print(is_a)

# word=input("enter the word = ").casefold()
# if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
#     print("vowels")
# else:
#     print("consonants")


word=input("enter the word = ").casefold()
vowel={"a","e","i","o","u"}
if word[0] in vowel:
    print("vowels")
else:
    print("consonants")


