matriz = []
filas = 0
columnas = 0

def pedirTamaño():
    global filas, columnas
    filas = leerValor("tamaño de filas")
    columnas = leerValor("tamaño de columnas")
    

def leerValor(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error. verifique que el Valor sea entero")

def agregarElementos():
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(int(input(f"Valor: ({i}, {j}): ")))


def menu():
    print("""
1. Asignar tamaño
2. Agregar elemento
3. Salir """)
    op = leerValor("Opcion: ")
    return op

def main():
    while True:
        op = menu()
        if op == 1:
            pedirTamaño()
        elif op == 2:
            agregarElementos()
        elif op == 3:
            break 

main()