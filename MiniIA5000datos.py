import pandas as pd
#df = pd.read_csv('datos_100.csv')
df = pd.read_csv('datos.csv')
num_columnas = df.shape[1]
# Inicializa la lista para almacenar nombres sin repetir
nombres_sin_repetir_lista = []
# Itera sobre todas las columnas, excepto la última
for i in range(num_columnas - 1):
    nombre_columna = df.columns[i]
    columna = df.iloc[:, i]
    nombres_sin_repetir = set()
    # Itera sobre los elementos de la columna y agrega los nombres al conjunto
    for nombre in columna:
        nombres_sin_repetir.add(nombre)
    nombres_sin_repetir_lista.append(nombres_sin_repetir)
#=====================================#
#asignacion de los grupos
gruposX = []

for casosX in nombres_sin_repetir_lista:
    listaCasosX = list(casosX)
    listaCasosX.sort()

    if len(listaCasosX) > 6:
        num_elementos_por_grupo = len(listaCasosX) // 6
        residuo = len(listaCasosX) % 6
        inicio = 0
        fin = num_elementos_por_grupo + (1 if residuo > 0 else 0)
        grupos_subgrupos = []

        for _ in range(6):
            grupoCasos = listaCasosX[inicio:fin]
            grupos_subgrupos.append(grupoCasos)
            inicio = fin
            fin += num_elementos_por_grupo + (1 if residuo > 0 else 0)
            residuo -= 1

        gruposX.append(grupos_subgrupos)
    else:
        gruposX.append([listaCasosX])

nuevoGruposX = []
for lista in gruposX:
    if (len(lista) == 1):
        nuevaLista = lista[0]
        nuevoGruposX.append(nuevaLista)
    else:
        nuevoGruposX.append(lista)
numeroGruposDisponibles = len(nuevoGruposX)
print(f'Los nuevos grupos disponibles son: {numeroGruposDisponibles}') 
#=====================================#
for i in range(len(nuevoGruposX)):
    print(f'En la columna {i} puedes seleccionar los siguientes grupos {nuevoGruposX[i]}')
#proceso de la "IA"
#para el caso que queremos elegir, tenemos que obtener el valor de la cantidad de veces donde x cumple y entre la cantidad y's cuyo valor es 1
casosX = [1, nuevoGruposX[1][1], nuevoGruposX[2][1], 0, 0, 1, 0]
casosY = ['Male', 'Female']
casosY1 = []
n_casosY = []
#iteración para cada y en el data set
for caso_y in casosY:
    contadorY = 0
    y = caso_y
    casos_y_actual = []
    #Contador para ir cambiando de columna
    i = 0
    #iteración para la lista de condiciones x en el dataset
    for caso_x in casosX:
        x = caso_x
        if isinstance(x, list):
            #print('el elemento es una lista')
            numero_casosY1 = 0
            #iteracion sobre todas las filas de dataframe comparando la condicion X con el caso Y
            for index, fila in df.iterrows():
                #se obtiene 
                valor_columnaX = fila.iloc[i] #columna donde se compara con la condicion x
                valor_columnaY = fila.iloc[-1] #columna donde se compara con el caso y
                for elemento in x:
                    if valor_columnaX == elemento and valor_columnaY == y:
                        numero_casosY1 += 1
            casos_y_actual.append(numero_casosY1) #se agrega el numero de casos donde si se cumple la condicion a la lista de casos.
            print(f'Casos donde x = {x} y y = {y}: {numero_casosY1}')
            numero_casosY1 = 0
            i += 1
        else:
            #print("El elemento no es una lista.")
            numero_casosY1 = 0
            #iteracion sobre todas las filas de dataframe comparando la condicion X con el caso Y
            for index, fila in df.iterrows():
                #se obtiene 
                valor_columnaX = fila.iloc[i] #columna donde se compara con la condicion x
                valor_columnaY = fila.iloc[-1] #columna donde se compara con el caso y
                if valor_columnaX == x and valor_columnaY == y:
                    numero_casosY1 += 1
            casos_y_actual.append(numero_casosY1) #se agrega el numero de casos donde si se cumple la condicion a la lista de casos.
            print(f'Casos donde x = {x} y y = {y}: {numero_casosY1}')
            numero_casosY1 = 0
            i += 1
    i = 0
    casosY1.append(casos_y_actual)
    #print(casosY1)
    #para obtener el numero de casos donde se cumple la Y en interación
    for index, fila in df.iterrows():
        valor_columnaY = fila.iloc[-1]
        if valor_columnaY == y:
            contadorY += 1
    n_casosY.append(contadorY)
print(casosY1) #imprime la cantidad de veces que se cumplió x condicipon con el caso Y con todos valores de Y
print(n_casosY) #imprime las veces que se obtuvo Y con todas las salidas

#se obtiene la probabilidad para los casos con la siguiente formula ProbabilidadY = (multiplicacion de todos los elementos del array) * (CantidadTotalYs)
Probabilidades_Ys = []
for i in range(len(n_casosY)):
    Y_n = n_casosY[i]
    casosYn = casosY1[i]
    ProbabilidadY1 = 1
    for numero_caso in casosYn:
        ProbabilidadY1 = (numero_caso / Y_n) * ProbabilidadY1
        #print(ProbabilidadY1)
    Probabilidades_Ys.append(ProbabilidadY1)
print(Probabilidades_Ys)

#obtenemos probabilidadTotal = ProbabilidadSi + ProbabilidadNo
probabilidadTotal = 0
for probabilidad in Probabilidades_Ys:
    probabilidadTotal += probabilidad
print(f'la probabilidad total es: {probabilidadTotal}')
#obtenemos el procentaje de la probabilidad y1 y y2
porcentajes = []
for i in range(len(Probabilidades_Ys)):
    porcentajeProbabilidad = 0
    porcentajeProbabilidad = Probabilidades_Ys[i] / probabilidadTotal
    porcentajes.append(porcentajeProbabilidad)
    porcentajeProbabilidad = 0
print(f'la probabilidad de que se cumpla el el caso con las condiciones brindadas {casosX} es de...\n {porcentajes[0]*100}% a que sea {casosY[0]} y {porcentajes[1]*100}% a que sea {casosY[1]}')
