
path1="C:\\Users\\LENOVO\\Desktop\\pythoncourse\\python\\token\\new.txt"
path2="C:\\Users\\LENOVO\\Desktop\\pythoncourse\\python\\token\\stopword.txt"
f_news=open(path1,"r")
f_word=open(path2,"r")
stop_word_set={wline.rstrip("\n") for wline in f_word }
news_set=set()
for nline in f_news:
    word=nline.split()
    for w in word:
        news_set.add(w)
print(news_set.difference(stop_word_set))


