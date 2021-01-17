def check(arr):
    s=set()
    for i in arr:
        if i not in s:
            s.add(i)
        else:
            if i+1 not in s:
                s.add(i+1)
    print(s)
    return len(s)
            
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    max1=len(set(arr))
    print(check(arr))
    
                
            
            
            
            
           
        
            
