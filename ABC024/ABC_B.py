N,T = map(int,input().split())
A = [int(input()) for _ in range(N)]
ans = 0
for i in range(1,N):
    ans += min(A[i]-A[i-1],T)

print(ans+T)

