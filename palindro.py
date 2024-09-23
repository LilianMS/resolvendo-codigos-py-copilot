# Vamos testar se uma palavra é um palíndromo.
# Um palíndromo é uma palavra que se lê da mesma forma de trás para frente.

def verificar_palindromo(palavra):
    if palavra == palavra[::-1]:
        return "É um palíndromo"
    else:
        return "Não é um palíndromo"
    
if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    resultado = verificar_palindromo(palavra)
    print(f"A palavra {palavra} {resultado}.") 

