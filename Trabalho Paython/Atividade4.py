a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

delta = ((b * b) - 4 * a * c)
raiz1 = ((-b + delta))
raiz2 = ((b + delta) / (2 * a))
print(f'Os valores de *1 é {raiz1} e *2 é {raiz2}')
