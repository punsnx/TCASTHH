def swap(l,pos1,pos2) :
    l[pos1], l[pos2] = l[pos2], l[pos1]
    return l
def compare(l) :
    print(l)
    for n in range(len(l)-1) :
        if n == 0 and l[n+1] > l[n] :
            print(l)
        elif n == 1 and l[n+1] < l[n] :
            print(swap(l,n,n+1))
        elif n == 2 and l[n+1] > l[n] :   
            print(l)
        elif n == 3 and l[n+1] == 10 and l[n] == 35 : 
            print(swap(l,n,n+1))
    return l
                
while True :
    list=[14,33,27,35,10]
    compare(list)