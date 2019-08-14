tmp=(pow(3,4)+5*pow(6,7))/8
print(tmp)
i=0
while True:
    n1=i*i
    i=i+0.001
    n2=i*i
    if n1<=tmp and n2>tmp:
        res=(i-0.001)
        print("%5.3f"%(res))
        break
    