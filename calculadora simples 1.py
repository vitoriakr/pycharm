def Adicao(n1,n2):
    add = n1 + n2
    return add
def Subtracao(n1,n2):
    sub = n1 - n2
    return sub
def Multiplicacao(n1,n2):
    mult = n1 * n2
    return mult
def Divisao(n1,n2):
    div = n1 / n2
    return div
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print('A soma dos números é igual a: ', Adicao(n1,n2))
print('A subtração dos números é igual a: ', Subtracao(n1,n2))
print('A multiplicação dos números é igual a: ',Multiplicacao(n1,n2))
print('A divisão dos números é igual a: ',Divisao(n1,n2))