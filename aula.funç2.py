def calcmededia(a,b,c):
    return (a + b + c)/3


nota1 = float(input('Digite a primeira nota?'))
nota2 = float(input('Digite a segunda nota?'))
nota3 = float(input('Digite a terceira nota?'))

print(f'A media é: {calcmededia(nota1,nota2,nota3):.2f}')





# Definindo a função para calcular a área do retângulo
def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura

# Solicitando ao usuário o comprimento e a largura
comprimento = float(input("Digite o comprimento do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))

# Calculando a área
area = calcular_area_retangulo(comprimento, largura)

# Exibindo o resultado
print(f"A área do retângulo é: {area}")
