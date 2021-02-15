def good(a):
    "Select a good image"

    ls=[]
    with open("good.txt","r") as f:
        words=f.readlines()
        for line in words:
            ls.append(line)
    return ls[a]

def bad(b):
    "Selects a bad image"
    
    ls=[]
    with open("bad.txt","r") as f:
        words=f.readlines()
        for line in words:
            ls.append(line)
    return ls[b]
