wordstring='''
it was the best of times it was the wprst of times.
it was the age of wisdom it was the age og doolishness.
'''
wordstring=wordstring.replace('.',' ')
wordlist=wordstring.split()
list=[]
for w in wordlist:
    list.append(wordlist.count(w))
d=dict(zip(wordstring,list))
print(d)
