def f (x):
    B = 60 <= x <= 80
    return ((x%a==0 )or (B <= (not(x%a== 0))))

for a in range (1000,0,-1):
    if all(f (x) == 1 for x in range (1,1000)):
        print (a)
        break