fin=open("word.txt")

def lis(fin):
    new=[]
    for i in fin:
        new.append(i.strip())
    listt=sorted(new)
    y=(lambda x, y: len(x) < len(y), listt)
    print(y)


lis(fin)





