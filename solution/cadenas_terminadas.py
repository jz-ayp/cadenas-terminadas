"""
Biblioteca de funciones para cadenas "terminadas" (el final de la cadena
se identifica mediante un carácter terminador).
"""

def str_print(cadena, terminador="$"):
    "Imprimir una cadena carácter por carácter"
    for caracter in cadena:
        if caracter != terminador:
            print(caracter, end="")
        else:
            break
    print()


def str_print_plus(*cadenas, terminador="$", separador=" ", fin="\n"):
    "Imprimir una (en realidad, cero) o más cadenas carácter por carácter"
    for i, cadena in enumerate(cadenas):
        cadena = str(cadena)
        for caracter in cadena:
            if caracter != terminador:
                print(caracter, end="")
            else:
                break
        if i != len(cadenas) - 1:
            print(separador, end="")
    print(fin, end="")


def str_print2(cadena, terminador="$"):
    "Imprimir cadena carácter por carácter (versión con while)"
    posicion = 0
    while posicion < len(cadena) and (caracter := cadena[posicion]) != terminador:
        print(caracter, end="")
        posicion += 1
    print()


def str_copy(cadena, terminador="$"):
    "Copia una cadena carácter por carácter"
    copia = ""
    for caracter in cadena:
        if caracter != terminador:
            copia += caracter
        else:
            break
    copia += terminador
    return copia


def str_concat(cadena1, cadena2, terminador="$"):
    "Concatenar dos cadenas"
    final = ""
    for s in [cadena1, cadena2]:
        for c in s:
            if c != terminador:
                final += c
            else:
                break
    final += terminador
    return final


def str_concat_plus(*strings, terminador="$"):
    "Concatenar varias cadenas"
    final = ""
    for s in strings:
        for c in s:
            if c != terminador:
                final += c
            else:
                break
    final += terminador
    return final


def str_has_prefix(cadena, prefijo, terminador="$"):
    "¿La cadena comienza con el prefijo?"
    tiene_prefijo = True
    posicion = 0
    while posicion < len(prefijo):
        if prefijo[posicion] == terminador:
            break
        elif cadena[posicion] != prefijo[posicion]:
            tiene_prefijo = False
            break
        posicion += 1
    return tiene_prefijo


def str_is_substring(cadena, subcadena, terminador="$"):
    "Verifica si subcadena está presente en cadena"
    # "Limpiar las cadenas"
    cadena = str_copy(cadena, terminador)
    subcadena = str_copy(subcadena, terminador)
    # Obtener subcadenas de cadena y compararlas con cadena
    es_sub = False
    for i in range(len(cadena) - len(subcadena) + 1):
        sub = cadena[i:i+len(subcadena)-1]
        if sub == subcadena[:-1]:
            es_sub = True
            break
    return es_sub


def str_split(cadena, separador=" ", terminador="$"):
    "Divide una cadena en una lista de cadenas separadas por el carácter separador"
    cadenas = []
    temp = ""
    posicion = 0
    while posicion < len(cadena):
        caracter = cadena[posicion]
        if caracter in [separador, terminador]:
            temp += terminador
            cadenas.append(temp)
            temp = ""
        else:
            temp += caracter
        posicion += 1
    return cadenas        


if __name__ == "__main__":
    terminador = "$"

    str_print("-" * 50 + terminador)
    str_print("Probar str_print:$")
    casos = [
        "Hola$",
        "Hola#%jlafaj$",
        "Hola#$jlafaj",
    ]
    for caso in casos:
        str_print(caso, terminador)
        #str_print2(caso, terminador)
    str_print("$")

    str_print("-" * 50 + terminador)
    str_print("Probar str_copy:$")
    casos = [
        "Prueba 1$",
        "Prueba 2$",
        "Abracadabra patas de cabra$extra",
    ]
    for caso in casos:
        str_print_plus(caso, " --> $", str_copy(caso, terminador), terminador)
    str_print("$")

    str_print("-" * 50 + terminador)
    str_print("Probar str_concat:$")
    casos = [
        ("uno$", "dos$"),
        ("uno $", "dos $"),
    ]
    for caso in casos:
        str_print(str_concat(*caso, terminador), terminador)
    str_print("$")

    str_print("-" * 50 + terminador)
    str_print("Probar str_concat_plus:$")
    casos = [
        ("uno$", "dos$", "tres$"),
        ("uno $", "dos $", "tres $"),
        ("una sola$"),
        ("dos$", "cadenas$"),
    ]
    for caso in casos:
        str_print(str_concat_plus(*caso, terminador=terminador), terminador)
    str_print("$")

    str_print("-" * 50 + terminador)
    str_print("Probar str_has_prefix:$")
    casos = [
        ("unicornio$", "uni$"),
        ("dobletear$", "doble$"),
        ("exalumno$", "ex$"),
        ("doscientos$", "treinta$"),
        ("doscientos$", "dos$"),
        ("dos$", "doscientos$"),
    ]
    for caso in casos:
        str_print_plus(*caso, " --> $", str_has_prefix(*caso, terminador=terminador), terminador)
    str_print("$")

    str_print("-" * 50 + terminador)
    str_print("Probar str_is_substring:$")
    casos = [
        ("unicornio$", "uni$"),
        ("manicomio$", "ico$"),
        ("ramiro$", "miro$"),
        ("exalumno$", "rata$"),
        ("doscientos$", "sien$"),
    ]
    for caso in casos:
        str_print_plus(*caso, " --> $", str_is_substring(*caso, terminador=terminador), terminador)
    str_print("$")

    str_print("-" * 50 + terminador)
    str_print("Probar str_split:$")
    casos = [
        ("unicornio rana manicomio dormitorio$", " "),
        ("manicomio/cárcel/siempre/victoriosos/changos$", "/"),
        ("ramiro.fernando.ana.cristina.julia.sofía$", "."),
        ("exalumno%directivo%maestro%coordinador%azafata$", "%"),
    ]
    for caso, sep in casos:
        str_print_plus(caso, " --> $", *str_split(caso, separador=sep, terminador=terminador), terminador)
    str_print("$")


