def spread (sentence):
    i=0
    r="'"
    while i<len(sentence):
        if " "!=sentence[i]:
            r=r+str(sentence[i])
        else:
            r=r+"','"
        i=i+1
    print(r+"'")
a = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
spread(a)
b=input("enter the sentence")
spread(b)