tedad = int(input('how many students'))
l = []
sum = 0
for i in range(tedad):
    a = float(input("enter your score"))
    l.append(a)
    sum += a

a = max(l)
b = min(l)
avg = float(sum / tedad)

print('max score is', a)
print("least score is", b)
print("avg is ", avg)