a = input('enter your time')
seconds = 0
seconds +=  ((3600 *(int(a[0]) + int(a[1]))) +(60 * (int(a[3]) + int(a[4]))) + int(a[6]) + int(a[7]))
print(seconds)