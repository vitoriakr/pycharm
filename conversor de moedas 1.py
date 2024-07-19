def conversor_de_Moedas_real_yuan(real):
 yuan = real*1.33
 return yuan

def conversor_de_Moedas_real_euro(real):
 euro = real*0.17
 return euro

real = float(input('Digite um valor em real: '))

resultado_yuan = conversor_de_Moedas_real_yuan(real)
resultado_euro = conversor_de_Moedas_real_euro(real)


print('A conversão do real para yuan (moeda chinesa) é igual a: ', resultado_yuan)
print("A conversão do real para euro (moeda europeia) é igual a: ", resultado_euro)