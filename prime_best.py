def isprime(a):
    
    if a==2:
        return True
    elif a>2:
        for i in range(2,a):
            if a%i==0:
                return False
        return True
    else: 
        return False
    
for i in range(50):
    if isprime(i):
        print(i)
        