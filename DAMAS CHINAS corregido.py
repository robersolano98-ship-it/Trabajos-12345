# PROYECTO DE ESTRUCTURA DE DATOS
# JUEGO DE DAMAS

# Crear tablero

def crear_tablero():
    tablero = []

    for fila in range(8):
        fila_tablero = []

        for columna in range(8):

            # Casillas negras donde se pueden colocar fichas
            if (fila + columna) % 2 == 1:

                # Fichas oscuras
                if fila < 3:
                    fila_tablero.append("O")

                # Fichas claras
                elif fila > 4:
                    fila_tablero.append("C")

                else:
                    fila_tablero.append(".")

            else:
                fila_tablero.append(" ")

        tablero.append(fila_tablero)

    return tablero

# Mostrar tablero

def mostrar_tablero(tablero):
    print()
    print("    0   1   2   3   4   5   6   7")
    print("  +---+---+---+---+---+---+---+---+")

    for fila in range(8):
        print(fila, end=" | ")

        for columna in range(8):
            print(tablero[fila][columna], end=" | ")

        print()
        print("  +---+---+---+---+---+---+---+---+")

    print()
    print("C = Ficha clara")
    print("O = Ficha oscura")
    print("D = Dama clara")
    print("K = Dama oscura")

# Saber si una posicion pertenece al jugador

def pertenece_al_jugador(ficha, jugador):

    if jugador == "C":
        return ficha == "C" or ficha == "D"

    else:
        return ficha == "O" or ficha == "K"

# Saber si una ficha es dama

def es_dama(ficha):
    return ficha == "D" or ficha == "K"

# Saber si una posicion esta dentro del tablero

def dentro_tablero(fila, columna):
    return fila >= 0 and fila < 8 and columna >= 0 and columna < 8

# Revisar si existe una captura

def puede_comer(tablero, fila, columna, jugador):

    ficha = tablero[fila][columna]

    if not pertenece_al_jugador(ficha, jugador):
        return False

    # Direcciones diagonales
    direcciones = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for df, dc in direcciones:

        # Las fichas normales solo pueden comer hacia delante
        if not es_dama(ficha):

            if jugador == "C" and df > 0:
                continue

            if jugador == "O" and df < 0:
                continue

        fila_enemigo = fila + df
        columna_enemigo = columna + dc

        fila_salto = fila + (df * 2)
        columna_salto = columna + (dc * 2)

        if dentro_tablero(fila_salto, columna_salto):

            enemigo = tablero[fila_enemigo][columna_enemigo]
            destino = tablero[fila_salto][columna_salto]

            if enemigo != " " and enemigo != ".":
                if not pertenece_al_jugador(enemigo, jugador):
                    if destino == ".":
                        return True

    return False

# Revisar si el jugador tiene alguna captura

def jugador_puede_comer(tablero, jugador):

    for fila in range(8):
        for columna in range(8):

            if puede_comer(tablero, fila, columna, jugador):
                return True

    return False

# Mover una ficha

def mover_ficha(tablero, fila1, columna1, fila2, columna2, jugador):

    ficha = tablero[fila1][columna1]

    if not pertenece_al_jugador(ficha, jugador):
        print("Esa ficha no pertenece al jugador.")
        return False

    if not dentro_tablero(fila2, columna2):
        print("La posicion de destino no existe.")
        return False

    if tablero[fila2][columna2] != ".":
        print("La posicion esta ocupada.")
        return False

    diferencia_fila = fila2 - fila1
    diferencia_columna = columna2 - columna1

    # Movimiento normal

    if abs(diferencia_fila) == 1 and abs(diferencia_columna) == 1:

        if not es_dama(ficha):

            # Las claras bajan hacia filas menores
            if jugador == "C" and diferencia_fila != -1:
                print("La ficha clara solo puede avanzar hacia arriba.")
                return False

            # Las oscuras bajan hacia filas mayores
            if jugador == "O" and diferencia_fila != 1:
                print("La ficha oscura solo puede avanzar hacia abajo.")
                return False

        tablero[fila2][columna2] = ficha
        tablero[fila1][columna1] = "."

        coronar(tablero, fila2, columna2)

        return True

    # Movimiento para comer

    if abs(diferencia_fila) == 2 and abs(diferencia_columna) == 2:

        fila_enemigo = (fila1 + fila2) // 2
        columna_enemigo = (columna1 + columna2) // 2

        enemigo = tablero[fila_enemigo][columna_enemigo]

        if enemigo == "." or enemigo == " ":
            print("No hay una ficha enemiga para comer.")
            return False

        if pertenece_al_jugador(enemigo, jugador):
            print("No puedes comer tu propia ficha.")
            return False

        if not es_dama(ficha):

            if jugador == "C" and diferencia_fila > 0:
                print("La ficha clara solo puede comer hacia adelante.")
                return False

            if jugador == "O" and diferencia_fila < 0:
                print("La ficha oscura solo puede comer hacia adelante.")
                return False

        tablero[fila2][columna2] = ficha
        tablero[fila1][columna1] = "."
        tablero[fila_enemigo][columna_enemigo] = "."

        coronar(tablero, fila2, columna2)

        print("¡Ficha comida!")

        return True

    print("Movimiento no valido.")
    return False


# Convertir ficha normal en dama

def coronar(tablero, fila, columna):

    ficha = tablero[fila][columna]

    # Las claras llegan a la fila 0
    if ficha == "C" and fila == 0:
        tablero[fila][columna] = "D"
        print("¡La ficha clara se convirtio en Dama!")

    # Las oscuras llegan a la fila 7
    if ficha == "O" and fila == 7:
        tablero[fila][columna] = "K"
        print("¡La ficha oscura se convirtio en Dama!")


# --------------------------------------------------
# Contar fichas
# --------------------------------------------------

def contar_fichas(tablero, jugador):

    cantidad = 0

    for fila in range(8):
        for columna in range(8):

            if pertenece_al_jugador(tablero[fila][columna], jugador):
                cantidad += 1

    return cantidad


# --------------------------------------------------
# Revisar si el jugador puede hacer algun movimiento
# --------------------------------------------------

def tiene_movimiento(tablero, jugador):

    for fila in range(8):
        for columna in range(8):

            ficha = tablero[fila][columna]

            if pertenece_al_jugador(ficha, jugador):

                direcciones = [
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1)
                ]

                for df, dc in direcciones:

                    # Las fichas normales solo avanzan
                    if not es_dama(ficha):

                        if jugador == "C" and df > 0:
                            continue

                        if jugador == "O" and df < 0:
                            continue

                    nueva_fila = fila + df
                    nueva_columna = columna + dc

                    if dentro_tablero(nueva_fila, nueva_columna):

                        if tablero[nueva_fila][nueva_columna] == ".":
                            return True

                    # Revisar posibilidad de comer
                    if puede_comer(tablero, fila, columna, jugador):
                        return True

    return False


# --------------------------------------------------
# Juego principal
# --------------------------------------------------

def jugar():

    tablero = crear_tablero()

    # Comienzan las fichas claras
    jugador = "C"

    print("===================================")
    print("          JUEGO DE DAMAS")
    print("===================================")
    print()
    print("Las fichas claras comienzan.")
    print("Escribe las coordenadas usando numeros del 0 al 7.")

    while True:

        mostrar_tablero(tablero)

        # Revisar si algun jugador se quedo sin fichas
        if contar_fichas(tablero, "C") == 0:
            print("¡Ganaron las fichas oscuras!")
            break

        if contar_fichas(tablero, "O") == 0:
            print("¡Ganaron las fichas claras!")
            break

        # Revisar si el jugador esta acorralado
        if not tiene_movimiento(tablero, jugador):
            print("El jugador no tiene movimientos disponibles.")

            if jugador == "C":
                print("¡Ganaron las fichas oscuras!")
            else:
                print("¡Ganaron las fichas claras!")

            break

        if jugador == "C":
            print("Turno de las FICHAS CLARAS")
        else:
            print("Turno de las FICHAS OSCURAS")

        # Revisar si es obligatorio comer
        obligatoria = jugador_puede_comer(tablero, jugador)

        if obligatoria:
            print("¡TIENES QUE COMER UNA FICHA!")

        try:
            fila1 = int(input("Fila de la ficha: "))
            columna1 = int(input("Columna de la ficha: "))

            fila2 = int(input("Fila destino: "))
            columna2 = int(input("Columna destino: "))

        except ValueError:
            print("Debes escribir solamente numeros.")
            continue

        # Si hay una captura obligatoria,
        # el movimiento debe ser de 2 casillas
        if obligatoria:

            if abs(fila2 - fila1) != 2:
                print("Debes comer una ficha.")
                continue

            if not puede_comer(tablero, fila1, columna1, jugador):
                print("Esa ficha no puede comer.")
                continue

        movimiento = mover_ficha(
            tablero,
            fila1,
            columna1,
            fila2,
            columna2,
            jugador
        )

        if movimiento:

            # Si se acaba de comer, revisar si puede seguir comiendo
            fila_actual = fila2
            columna_actual = columna2

            while puede_comer(
                tablero,
                fila_actual,
                columna_actual,
                jugador
            ):

                mostrar_tablero(tablero)

                print("¡Puedes seguir comiendo!")
                print("Debes continuar con la misma ficha.")

                try:
                    nueva_fila = int(input("Nueva fila destino: "))
                    nueva_columna = int(input("Nueva columna destino: "))

                except ValueError:
                    print("Debes escribir numeros.")
                    continue

                if abs(nueva_fila - fila_actual) != 2:
                    print("Debes realizar otra captura.")
                    continue

                movimiento2 = mover_ficha(
                    tablero,
                    fila_actual,
                    columna_actual,
                    nueva_fila,
                    nueva_columna,
                    jugador
                )

                if movimiento2:
                    fila_actual = nueva_fila
                    columna_actual = nueva_columna

            # Cambiar turno
            if jugador == "C":
                jugador = "O"
            else:
                jugador = "C"


# --------------------------------------------------
# Iniciar programa
# --------------------------------------------------

jugar()
