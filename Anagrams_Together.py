n = int(input())
l = [] ; arr =[]
for i in range(n):
	s = str(input())
	l.append(s)
for w in l:
	s = ''.join(sorted(w))
	arr.append(s)

for p in  range(len(arr)):
	for q in range(p+1,len(arr)):
		print(cmp(arr[p],arr[q]))

