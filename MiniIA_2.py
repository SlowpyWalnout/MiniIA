import pandas as pd

# Leemos el archivo Excel
df = pd.read_csv('DataSet.csv')

# Proceso de la "IA"
casosX = ['lluvia', 'calor', 'A', 'N']
casosY = ['No', 'Si']
casos_Y1 = []

for caso_y in casosY:
    y = caso_y
    casos_Y1_y_actual = []  # Lista para almacenar el número de casos para el valor y actual
    for caso_x in casosX:
        x = caso_x
        numero_casosY1 = 0
        for index, fila in df.iterrows():
            valor_columnaX = fila[caso_x]
            valor_columnaY = fila['Se jugo']
            if valor_columnaX == x and valor_columnaY == y:
                numero_casosY1 += 1
            else:
                print(f'Hubo {valor_columnaX} y {valor_columnaY}, no se jugó.')
        casos_Y1_y_actual.append(numero_casosY1)
        print(f'Número de casos donde hubo {x} y {y} se jugó: {numero_casosY1}')

    casos_Y1.append(casos_Y1_y_actual)
    print(casos_Y1_y_actual)

print("Casos 'No':", casos_Y1[0])
print("Casos 'Si':", casos_Y1[1])

