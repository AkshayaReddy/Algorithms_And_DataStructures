#Create Permutations
def Perm(str,start,end):  
    current = 0;  
    global p
    if(start == end-1):  
        p.append(str);  
    else:   
        for current in range(start,end):  
            x = list(str);  
            temp = x[start];  
            x[start] = x[current];  
            x[current] = temp;  
            Perm("".join(x),start+1,end);  
            temp = x[start];  
            x[start] = x[current];  
            x[current] = temp;  
		
#Check divisibility for 8 and print results.		
n=int(input())
l=list(map(str,input().rstrip().split()))[:n]
nl,p=[],[]
for i in range(len(l)):
    Perm(l[i],0,len(l[i]))
    cnt=0
    for i in range(len(p)):
        if int(p[i])%8==0:
            cnt=cnt+1
        else:
            cnt=cnt+0
    if cnt>0:
        nl.append('YES')
    else:
        nl.append('NO')
    p=[]
print(nl)
