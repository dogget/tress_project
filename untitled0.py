a=int(input())
b=int(input())
q=0
n1=0
n2=0
n3=0
min=min(a,b)
p=abs(a-b)

if p%3==0:
    n1+=int(p/3)
    c=min//3
    n1+=c
    n3+=c
    n2+=min%3
    if a>=b:
        print(n1,n2,n3)
    else:
        print(n3,n2,n1)
    
else:
    q+=-1
    print(q)

    
    

