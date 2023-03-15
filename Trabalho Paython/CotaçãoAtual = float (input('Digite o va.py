CotaçãoAtual = float (input('Digite o valor de cotação atual:'))
ValorDolar = float(input('Digite o valor em dólares:'))
ValorReal = (ValorDolar / CotaçãoAtual)

print(f'o valor de {ValorDolar:.2f} dólares equivale a {ValorReal:.2f} reais')