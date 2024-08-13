def calcular_poligono(num_lados, medida_lado):
    if num_lados == 3:
        perimetro = 3 * medida_lado
        print(f"TRIÂNGULO com perímetro: {perimetro} cm")
    elif num_lados == 4:
        area = medida_lado ** 2
        print(f"QUADRADO com área: {area} cm²")
    elif num_lados == 5:
        print("PENTÁGONO")

num_lados = int(input("Digite o número de lados do polígono (3, 4 ou 5): "))
medida_lado = float(input("Digite a medida do lado (em cm): "))

calcular_poligono(num_lados, medida_lado)
