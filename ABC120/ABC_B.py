A,B,K = map(int,input().split())

cnt  = 0
for i in range(max(A,B)+1,0,-1):
    if (A%i==0) and (B%i==0):
        cnt+=1
        if cnt==K:
            print(i)
