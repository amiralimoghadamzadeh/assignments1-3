a = input('enter your list')
b = a[1:len(a)-1]
c = b.split(',')
l = []
for i in range(len(c)):
    l.append(0)


for i in range(len(c)):
    l[i] += int(c[i])

for i in range(len(l) - 1):
    if l[i + 1] < l[i]:
        print('arrays are  not in order')
        break
    else:
        print('arrays are  in order')
        break


