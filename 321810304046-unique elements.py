ul,l=[],[]
n=int(input('Enter no of elements: '))
print('Enter elememts: ')
for i in range(0,n):
	ele=input()
	l.append(ele)
for e in l:
	if e not in ul:
		ul.append(e)
print('unique list:',ul)