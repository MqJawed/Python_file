def armstrong(a):
    b=len(a)
    arm=0
    for i in range(0,b): # range (0,b) means 0 to b-1
        arm += (int(a[i]))**b
    if arm == int(a):
        return True
    else: 
        return False

for i in range(1000):
    if armstrong(str(i)):
        print(i)

