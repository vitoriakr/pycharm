def contar_vogais(string):
    vogais = "aeiouAEIOU"
    return sum(1 for char in string if char in vogais)

texto = input('Digite um texto: ')
print(f'O número de vogais na string é: {contar_vogais(texto)}')
