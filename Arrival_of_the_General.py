n  = int(input())
a = [*map(int,input().split())]
i1 = a.index(max(a)) + a[::-1].index(min(a))
print(i1-(i1>=n))
