R = lambda :list(map(int,input().split()))
for _ in range(int(input())):
    n=R()[0];a=R();a.sort();z=a[0]&1;yes=False
    for i in range(1,n):z+=a[i]&1;yes|=(a[i]-a[i-1])==1
    print("NYOE S"[yes|z&1^1::2])
