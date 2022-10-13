y = 0
x = int(input('first number: '))
divisor = int(input('second number: '))
while x >= divisor:
  x -= divisor
  y += 1 
print(f'Quotient: {y} & remainder {x}')