# 1l para cada 3m quadrados
# 18l custa 80
# 80/18 = R$ 4.44 aproximadamente por litro


import math

area_cliente = float(input("Informe a área em metros quadrados que deseja pintar:" ))
cobertura_por_lata = 54 # 18*3
lata_tinta = 18
preco_por_lata = 80
cobertura_litro = 3

def calcular_quantidade_latas(area):
  quantidade_latas = math.ceil(area_cliente / cobertura_litro)
  return quantidade_latas

def calcular_preco_total(quantidade_latas):
    preco_por_lata = 80
    preco_total = (quantidade_latas * preco_por_lata)
    return preco_total

quantidade_latas = calcular_quantidade_latas(area_cliente)
preco_total = calcular_preco_total(quantidade_latas)

print("Você deverá comprar", quantidade_latas, "latas. O preço total é R$", preco_total)