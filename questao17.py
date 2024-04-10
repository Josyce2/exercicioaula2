# 1l para cada 6m quadrados
# 18l custa 80
# gl 3.6l custa 25

import math

cobertura_por_lata = 108 # 18*6
cobertura_gl = 21.6 #3.6*6
lata_tinta = 18
preco_por_lata = 80
preco_por_gl = 25
cobertura_litro = 6

# calcula a quantidade de latas e galões necessários

def calcular_latas_gl(area):
  quantidade_latas = math.ceil(area_cliente / cobertura_por_lata)
  quantidade_gl = math.ceil(area_cliente / cobertura_gl)

# Calcula o preço total para comprar apenas latas ou apenas galões

  preco_latas = quantidade_latas * 80
  preco_gl = quantidade_gl * 25

# Calcula a quantidade mínima de latas e galões considerando o desperdício

  area_com_folga = area * 1.1  # Acrescenta 10% de folga
  latas_minimas = math.ceil(area_com_folga / cobertura_por_lata)
  galoes_minimos = math.ceil(area_com_folga / cobertura_por_gl)

# Calcula o preço total para misturar latas e galões
  latas_mistura = latas_minimas
  galoes_mistura = math.ceil((area_com_folga - latas_minimas * cobertura_por_lata) / cobertura_gl)
  preco_mistura = latas_mistura * 80 + galoes_mistura * 25

  return quantidade_latas, preco_latas, quantidade_gl, preco_gl, latas_mistura, galoes_mistura, preco_mistura

def main():
    try:
        area_cliente = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))
        quantidade_latas, preco_latas, quantidade_gl, preco_gl, latas_mistura, galoes_mistura, preco_mistura = calcular_latas_gl(area_cliente)

        print(f"Quantidade de latas necessárias: {latas}, Preço: R${preco_latas:.2f}")
        print(f"Quantidade de galões necessários: {galoes}, Preço: R${preco_galoes:.2f}")
        print(f"Quantidade de latas para mistura: {latas_mistura}, Quantidade de galões para mistura: {galoes_mistura}, Preço: R${preco_mistura:.2f}")

    except ValueError:
        print("Por favor, insira um valor numérico para a área.")

if __name__ == "__main__":
    main()