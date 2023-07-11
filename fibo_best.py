def fibo(a):
    
    if a==1 or a==0:
        return a
    else:
        return fibo(a-1)+fibo(a-2)

for i in range(15):
    if fibo(i)<15:
        print(fibo(i))
    else:
        break