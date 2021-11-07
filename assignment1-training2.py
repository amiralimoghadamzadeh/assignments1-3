import math
operator = input("choose the operator")

if operator == 'sin' or operator == 'cos' or operator == 'tan' or operator == 'factorial' :
    a = float(input('enter your number'))
    if operator == 'sin':
        print(math.sin(a))
    elif operator == 'cos':
        print(math.cos(a))
    elif operator == 'tan':
        print(math.tan(a))
    elif operator == 'factorial':
        print(math.factorial(a))
    
elif operator == "+" or operator == '-' or operator == '*' or operator == '/':
    b = float(input('enter first number'))
    c = float(input('enter second number'))
    if operator == '+':
        print(b + c)
    elif operator == '-':
        print(b - c)
    elif operator == '*':
        print(b * c)
    elif operator == '/':
        print(b / c)
else:
    print('operator not suppported')


