s = "bad is good"
sl = s.split()
l = []
for word in sl:
	l.append(word[0])

print(''.join(l))
