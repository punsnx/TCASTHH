F = [0,1]
def fibo(n,s) :
    if n == s :
        print("stop")
        return 
    if n <= 1 :
        print(F[n])
        n+=1
        fibo(n,s)
    elif n > 1 :
        fn = F[n-1] + F[n-2]
        F.append(fn)
        print(fn)
        n+=1
        fibo(n,s)
fibo(0,10)