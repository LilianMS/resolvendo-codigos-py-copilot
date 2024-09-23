
# Desenvolva um programa que leia um número inteiro e verifique se ele é par ou ímpar.

#number = int(input("Digite um número inteiro: "))

def verificar_paridade(number):
    if number % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

if __name__ == "__main__":
    numero = int(input("Digite um número inteiro: "))
    resultado = verificar_paridade(numero)
    print(f"O número {numero} é {resultado}.")

