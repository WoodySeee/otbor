f=open('17.txt')
m=[int(x) for x in f]
m1=[]
for i in range (len(m)-2):
    a,b,c=m[i], m[i+1], m[i+2]
    minm=min(a,b,c)
    maxm=max(a,b,c)
    if abs(maxm)%10==(abs(minm)%100)//10:
        if (('0' not in str(a)) + ('0' not in str(b)) + ('0' not in str(c)))>=2:
            m1.append(a*b*c)
print(len(m1), abs(min(m1)))
    
    
