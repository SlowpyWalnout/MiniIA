nombres_sin_repetir_lista = [{1},{0, 1}, {11.8, 12.9, 12.2, 14.6, 11.9, 13.0, 13.5, 14.0, 14.4, 15.3, 12.1, 15.5, 14.7, 15.2, 11.5, 11.4, 11.7, 11.6, 12.5, 12.3, 12.8, 12.7, 12.0, 13.8, 13.7, 13.3, 13.2, 13.9, 14.5, 14.2, 14.1, 14.3, 15.4, 15.1, 15.0, 12.4, 12.6}, {5.5, 5.9, 7.1, 6.8, 5.4, 6.1, 6.3, 6.2, 5.2, 5.8, 6.7, 7.0, 5.1, 5.6, 6.5, 6.0, 6.4, 5.3, 5.7}, {0, 1}, {0, 1}, {0, 1}, {0, 1}]
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

print('Los grupos disponibles son:', gruposX)
nuevoGruposX = []
for lista in gruposX:
    if (len(lista) == 1):
        nuevaLista = lista[0]
        nuevoGruposX.append(nuevaLista)
    else:
        nuevoGruposX.append(lista)
numeroGruposDisponibles = len(nuevoGruposX)
print(f'Los nuevos grupos disponibles son: {numeroGruposDisponibles}')
        