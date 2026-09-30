# ==============================================================================
# Proyecto: MisGustos [TuNombre]
# Tema: Series
# Materia: Estructura de Datos
# Lenguaje: Python 3
# ==============================================================================

# ------------------------------------------------------------------------------
# Paso 1: Declaración del arreglo (lista) inicial con 6 series predefinidas
# ------------------------------------------------------------------------------
series_iniciales = [
    "Breaking Bad",
    "Stranger Things",
    "Dark",
    "The Office",
    "Game of Thrones",
    "Loki"
]


# ------------------------------------------------------------------------------
# Paso 3: Función para transformar la lista unidimensional en una matriz (2x3)
# ------------------------------------------------------------------------------
def crear_matriz(arreglo):
    """
    Toma una lista de 6 elementos y los organiza en una estructura bidimensional
    (matriz de 2 filas x 3 columnas) usando ciclos for con control de índices.
    """
    matriz = []
    filas = 2
    columnas = 3
    indice = 0

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(arreglo[indice])
            indice += 1
        matriz.append(fila)
    
    return matriz


# ------------------------------------------------------------------------------
# Paso 4: Función para simular una Pila (LIFO) e ingresar elementos (.append)
# ------------------------------------------------------------------------------
def crear_pila(arreglo):
    """
    Construye una pila a partir del arreglo inicial e inserta 2 elementos
    adicionales en el tope mediante la operación .append().
    """
    pila = []
    
    # Se copian los elementos iniciales a la pila usando un ciclo while
    idx = 0
    while idx < len(arreglo):
        pila.append(arreglo[idx])
        idx += 1
    
    # Inserción de 2 series adicionales en el tope de la pila
    pila.append("Better Call Saul")
    pila.append("The Mandalorian")
    
    return pila


# ------------------------------------------------------------------------------
# Paso 6: Función específica para imprimir de forma ordenada la matriz y la pila
# ------------------------------------------------------------------------------
def imprimir_resultados(matriz, pila):
    """
    Imprime de forma clara y estructurada el contenido de la matriz (2x3)
    y de la pila utilizando ciclos for y while explícitos.
    """
    print("\n" + "="*50)
    print("         VISUALIZACIÓN DE ESTRUCTURAS DE DATOS")
    print("="*50)

    # Impresión de la Matriz (2x3) mediante un ciclo for anidado
    print("\n[+] MATRIZ DE SERIES (2 filas x 3 columnas):")
    print("-" * 45)
    for i in range(len(matriz)):
        print(f"Fila {i + 1}: ", end="")
        for j in range(len(matriz[i])):
            # Formato tabulado para alinear la matriz
            print(f"[{matriz[i][j]:^16}]", end=" ")
        print()

    # Impresión de la Pila utilizando un ciclo while
    print("\n[+] PILA DE SERIES (Estructura LIFO con elementos agregados):")
    print("-" * 45)
    
    # Recorremos la pila desde el tope (último agregado) hasta la base (primer elemento)
    posicion = len(pila) - 1
    while posicion >= 0:
        etiqueta = "<- TOPE" if posicion == len(pila) - 1 else ""
        print(f" Posición [{posicion}]: {pila[posicion]:<20} {etiqueta}")
        posicion -= 1
        
    print("="*50 + "\n")


# ------------------------------------------------------------------------------
# Paso 2: Menú interactivo con ciclo while y condicionales if-elif-else
# ------------------------------------------------------------------------------
def menu_principal():
    """
    Controla el flujo de ejecución del programa interactivo.
    """
    # Variables de estado para almacenar las estructuras generadas
    matriz_series = []
    pila_series = []

    opcion = ""
    while opcion != "4":
        print("\n" + "*"*40)
        print("    MENÚ PRINCIPAL - MisGustos [Series]")
        print("*"*40)
        print("1. Generar Matriz (2x3)")
        print("2. Generar Pila (con series extra)")
        print("3. Imprimir Estructuras")
        print("4. Salir")
        print("*"*40)
        
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            matriz_series = crear_matriz(series_iniciales)
            print("\n[✓] Matriz de 2x3 generada correctamente.")
            
        elif opcion == "2":
            pila_series = crear_pila(series_iniciales)
            print("\n[✓] Pila generada y 2 series adicionales agregadas correctamente.")
            
        elif opcion == "3":
            if not matriz_series or not pila_series:
                print("\n[!] Aviso: Por favor genera primero la Matriz (Opción 1) y la Pila (Opción 2) antes de imprimir.")
            else:
                imprimir_resultados(matriz_series, pila_series)
                
        elif opcion == "4":
            print("\n[✓] Saliendo del programa... ¡Éxito en tu examen!")
            
        else:
            print("\n[✗] Opción no válida. Por favor, ingresa un número del 1 al 4.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()
