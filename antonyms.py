a=dict()
# a={'hot':'cold'}
while True:
    find = False
    word=input("please enter a word:")
    if len(a)>0:
        for x in a:
            if x==word:
                print(a.get(x))
                find=True
                break
        for x in a:
            if a.get(x)==word:
                find = x
                break
        if find!=0:
            print(find)
        else:
            ant = input("what's its antonym?")
            a[word] = ant
    else:
        ant = input("what's its antonym?")
        a[word] = ant