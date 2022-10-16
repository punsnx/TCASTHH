list = [29,72,98,13,87,66,52,51,36]
n= 0
def sm(l) :
    global n
    if n < len(l)-1 :
        pm = l.index(min(l[n:len(l)]))
        l[n], l[pm] = l[pm], l[n]
        print(l, n, len(l)-1, len(l), pm)
        n+=1 
        sm(l)
    return l

print(str(sm(list)) + "Finished")