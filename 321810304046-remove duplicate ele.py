l=[]
n=int(input('Enter no of elements: '))
print('Enter elememts: ')
for i in range(0,n):
	ele=input()
	l.append(ele)
for i in range(1,n-1):
	if(l[i-1]==l[i]):
		del l[i-1]
print('list after removing duplicate elements:',l)