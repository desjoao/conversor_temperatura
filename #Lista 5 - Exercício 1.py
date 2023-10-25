#Lista 5 - Exercício 1

def conv (c):
    conv = (c-32)*5/9
    return conv
temp = float(input('Insira a temperatura em graus Fahrenheit: '))
print(f'A temperatura em graus Celsius é: {conv(temp)}º')
