def polegadas_para_centimetros(pol):
    return pol * 2.54

polegadas = float(input("Digite o valor em polegadas: "))
centimetros = polegadas_para_centimetros(polegadas)
print(f"{polegadas} polegadas é equivalente a {centimetros} centímetros")
