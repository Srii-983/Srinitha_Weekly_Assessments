def wordcounter():
    string=input("enter string")
    wds=string.lower().split()
    wd_cnt = {}
    for word in wds:
        if word in wd_cnt:
            wd_cnt[word] += 1
        else:
            wd_cnt[word] = 1
    for word, cnt in wd_cnt.items():
        print(f"{word}: {cnt}")
wordcounter()
