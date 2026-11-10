# Funciones

## Ejercicios: 
1. **Subarreglo de suma máxima**
2. **Cadenas terminadas**


## Enunciado

Para cada uno de los problemas planteados, realizar el análisis* (entradas, procesos, salidas, pruebas), el algoritmo* (como diagrama de flujo) y el programa en Python.

****Nota***: Incluir análisis y algoritmo únicamente para el ejercicio 1.

### Ejercicio 1. Subarreglo de suma máxima
Dada una lista de números, por ejemplo: `[1, -2, 3, 4, -9, 6]`, el objetivo es encontrar, dentro de la lista, un subconjunto de elementos contiguos con el que se obtenga la máxima suma posible. Por ejemplo, para la lista mencionada anteriormente, la suma máxima posible es `7` y se obtiene sumando los elementos contiguos `[3, 4]`. 

Escribe una función `suma_maxima` que regrese la lista con la que se obtiene la suma máxima, o en el caso de que no haya suma máxima, regrese una lista vacía.

Incluye un bloque `if __name__ == "__main__":` para escribir tus pruebas.

***Nota***: ¿Cómo es que no se podría obtener una suma máxima? Por ejemplo, en la lista `[-1, -1, -1, -1]` no hay suma máxima. Verifícalo.


### Ejercicio 2. Cadenas terminadas. Uso indexado de elementos.
Implementa los siguientes algoritmos en Python, cada uno en una función.

Prueba su funcionamiento dentro de un bloque `if __name__ == "__main__":` en el mismo archivo de código. 

***Nota***: Para estos ejercicios, se considerará como cadena una sucesión de caracteres cuyo fin se denota con un carácter terminador, por ejemplo: `"$"`. Cualquier carácter posterior al terminador, no se considera parte de la cadena. Tampoco el terminador forma parte de la cadena.

1. Impresión de una cadena (`str_print`). Escribe una función que reciba una cadena y el carácter que se usará como terminador, e imprima los caracteres de la cadena uno por uno, hasta encontrar el terminador (que no se enviará a imprimir a la terminal). ***Nota***: Esta función será usada en todo este ejercicio para imprimir las cadenas, ya que todas deberán llevar un carácter terminador.

2. Copia manual de una cadena en otra, letra a letra (`str_copy`). La función recibe una cadena y el carácter que se usará como terminador y, en una cadena interna, realiza la copia carácter por carácter, hasta el carácter terminador. Regresa la cadena copiada, que incluya un único terminador al final de la misma.

3. Concatenación manual de un par de cadenas (`str_concat`). La función recibe dos cadenas (propiamente terminadas) y el carácter que se usará como terminador, y regresa una cadena que contenga ambas cadenas unidas. La cadena regresada debe incluir un solo terminador, al final. ***Nota***: Cuando la tengas, pregúntame cómo hacerle para que concatene cualquier cantidad de cadenas, no solo dos.

4. Función `str_has_prefix`. Recibe una cadena a procesar, una cadena prefijo, y un carácter que se usará como terminador. Regresa un valor lógico `True` en el caso de que la cadena a procesar contenga la cadena prefijo al inicio de la misma; regresa `False` en otro caso. El algoritmo debe considerar que ambas cadenas terminan al encontrar el carácter terminador.

5. Función `str_is_substring`. Recibe una cadena a procesar, una cadena secundaria, y un carácter que se usará como terminador. Regresa un valor lógico `True` en el caso de que la cadena a procesar contenga la cadena secundaria; regresa `False` en otro caso. El algoritmo debe considerar que ambas cadenas terminan al encontrar el carácter terminador.

6. Implementación de `split`. Escribe una funcion `str_split`, que reciba una cadena a procesar, un carácter separador y un carácter terminador. Dentro de la función, analiza letra por letra la cadena a procesar. La función regresa una lista con varias cadenas, correspondientes a las que se encuentran en la cadena original, delimitadas por el carácter separador, que ya no formará parte de las cadenas incluidas en la lista. Todas las cadenas de la lista deben incluir su correspondiente carácter terminador.


## Instrucciones
- Elabora los correspondientes análisis y algoritmos antes de escribir el código de cada una de las funciones. Utiliza diagramas de flujo para representar cada uno de tus algoritmos e ilustrar su lógica. 

- Codifica tus soluciones en los archivos [`sublista_suma_max.py`](/sublista_suma_max.py) y [`cadenas_terminadas.py`](/cadenas_terminadas.py), respectivamente.
     
- Prueba tus funciones en un bloque `if __name__ == "__main__:` con diferentes datos de entrada. Verifica que tus funciones regresen los valores correctos. Identifica y pon atención especial a los casos que pudieran ser problemáticos de manejar (casos límite).

- Añade cadenas de documentación a tu programa y a cada una de tus funciones.

  
## Entrega
Completa estos y el resto de los ejercicios y compila, para cada uno, el enunciado, análisis, diagrama de flujo, código y pruebas de ejecución, en un informe tal como se describe en los requisitos para entrega de tareas en Canvas. No olvides incluir portada y conclusiones.

***Nota***: Recuerda que solo deberás incluir el análisis y el algoritmo para el ejercicio 1.


## Casos de prueba de ejemplo

### `suma_maxima`
| Entradas               | Salidas  |
|:-----------------------|:---------|
| `[1, -2, 3, 4, -9, 6]` | `[3, 4]` |
| `[-1, -1, -1, -1]`     | `[]`     |

### `str_print`
| Entradas            | Salidas |
|:--------------------|:--------|
| `"Hola$"`, `"$"`    | `Hola`  |
| `"Adiós&"`, `"&"`   | `Adiós` |
| `"Salud#os"`, `"#"` | `Salud` |

### `str_copy`

| Entradas            | Salidas      |
|:--------------------|:-------------|
| `"Ejemplo$"`, `"$"` | `"Ejemplo$"` |

### `str_concat`

| Entradas                            | Salidas             |
|:------------------------------------|:--------------------|
| `"Diseño$"`, `"Algoritmo$s"`, `"$"` |`"DiseñoAlgoritmo$"` |

### `str_has_prefix`

| Entradas                          | Salidas |
|:----------------------------------|:--------|
| `"prehistoria$"`, `"pre$"`, `"$"` | `True`  |
| `"castillo$"`, `"xy$"`, `"$"`    | `False` |

### `str_is_substring`

| Entradas                            | Salidas |
|:------------------------------------|:--------|
| `"prehistoria$"`, `"histo$"`, `"$"` | `True`  |
| `"castillo$"`, `"pillo$"`, `"$"`    | `False` |

### `str_split`

| Entradas                          | Salidas |
|:----------------------------------|:--------|
| `"algoritmos/cálculo/historia%"`, `"/%"`, `"%"` | `["algoritmos%", "cálculo%", "historia%"]`  |


## Rúbrica
Verifica tu entrega contra la rúbrica disponible en Canvas para maximizar tu calificación.
