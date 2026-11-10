#from pprint import pprint

def suma_maxima(lista, empate=False):
    """
    Encontrar la sublista de elementos contiguos en una lista 
    con los que se obtiene la suma máxima.
    En caso de empate, si el parámetro empate es False, se regresa la lista vacía,
    si es True, se regresan todas las sublistas con las que se obtiene la suma máxima.
    """
    # Caso trivial: Lista vacía
    if not lista:
        return []
    # Registraremos los resultados de las sumas en un diccionario
    sumas = {}
    # Vamos a hacer sublistas de tamaño 1, 2, 3, ... len(lista)
    for tamanho in range(1, len(lista)+1):
        # Las listas inician en las posiciones 0, 1, ... len(lista) - tamaño
        for inicio in range(len(lista)-tamanho+1):
            sublista = lista[inicio:inicio+tamanho]
            suma = sum(sublista)
            if suma not in sumas:
                sumas[suma] = [sublista]
            else:
                sumas[suma].append(sublista)
    #pprint(sumas)
    # Encontrar la suma máxima
    suma_max = max(sumas)
    # Encontrar la sublista relacionada
    sublistas = sumas[suma_max]
    # ¿Hay una sola opción para suma máxima o está repetida
    if len(sublistas) > 1:
        if empate:
            sublista = sublistas
        else:
            sublista = []
    else:
        sublista = sublistas[0]
    return sublista


if __name__ == "__main__":
    casos = [
        [1, -2, 3, 4, -9, 6],
        [-1, -1, -1, -1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, -1],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [1, 2, 3, 4, 5, 6, 7, 8, -8],
        [1, -2, 3, -4, 5, -6, 7, -8, -8],
        [-1, -8, -3, -2, -100, -8, -4],
        [5, -1, 2],
        [4, -5, 4, -1, 2, -1, 2, -3],
        [-1, -2, -3, -4, -5],
    ]
    print("Probar excluyendo los empates")
    for caso in casos:
        print(caso, " --> ", suma_maxima(caso))
    print()
    print("Probar incluyendo los empates")
    for caso in casos:
        print(caso, " --> ", suma_maxima(caso, empate=True))
