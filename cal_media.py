# Crie um programa que calcule a média de um aluno. O programa deve receber 3 notas e calcular a média final.

def calcular_media():
    notas = []
    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    return media

if __name__ == "__main__":
    media = calcular_media()
    print(f"A média das notas é: {media:.2f}")