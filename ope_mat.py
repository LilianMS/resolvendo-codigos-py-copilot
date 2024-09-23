# Vamos receber dois numeros inteiros m e n e realizar operações matemáticas com eles
# Vamos retornar o resultado de cada operação em uma linha

m = int(input('Digite o primeiro número inteiro: '))
n = int(input('Digite o segundo número inteiro: '))

# Vamos receber a operação a ser realizada
operacao = input('Digite a operação (+, -, *, /, //, %, **): ')

# Realiza a operação escolhida
if operacao == '+':
    print(m + n)
elif operacao == '-':
    print(m - n)
elif operacao == '*':
    print(m * n)
elif operacao == '/':
    print(m / n)
elif operacao == '//':
    print(m // n)
elif operacao == '%':
    print(m % n)
elif operacao == '**':
    print(m ** n)
else:
    print('Operação inválida')