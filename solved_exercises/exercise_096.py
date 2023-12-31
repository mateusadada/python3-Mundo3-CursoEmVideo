# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def calcular_area_retangulo(largura, comprimento):
    area = largura * comprimento
    return area


print('Bem-vindo ao programa de cálculo da área de um terreno!')

largura = float(input('Digite a largura (m): '))
comprimento = float(input('Digite o comprimento (m): '))

print(f'\nA área de um terreno {largura:.1f} x {comprimento:.1f} é de '
      f'\033[33m{calcular_area_retangulo(largura, comprimento):.1f} m².')
