N = input()
d = [int(x) for x in N]
print(d)
index = int(len(d)/2)
p1 = sum(d[:index]); p2 = sum(d[index+1:]);
if p1 == p2:
	print(1)
else:
	print(0)