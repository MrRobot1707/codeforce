for t in range(int(input())):
	g =int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	min_a = min(a)
	min_b = min(b)
	d1= 0
	d2 =0
	total=0
	for i in range(g):
		d1 = a[i] - min_a
		d2 = b[i] - min_b
		total+= max(d1,d2)
	print(total)


