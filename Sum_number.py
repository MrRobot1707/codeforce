x= input()
nE = ''.join(filter(lambda i: i.isdigit(),x))
l = list(nE)
test_list = [int(i) for i in l] 
print(sum(test_list))