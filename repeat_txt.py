# vamos receber uma string e um número inteiro n e vamos repetir a string n vezes
# vamos retornar a string resultante separada por quebra de linha

string = input('Digite a string: ')
number = int(input('Digite o número inteiro: '))


def repeat_txt(txt, n):
    return (txt + '\n') * n

print(repeat_txt(string, number))
