import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    for libro in libros:
        print()
        if libro['cant_ej_pr'] == 0:
            print(f"El libro: {libro['titulo']} no tiene ejemplares prestados.")
        else:
            print(f"Libro: {libro['titulo']}")
            print(f"Ejemplares prestados: {libro['cant_ej_pr']}")
    return libro

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)
    print("Libro registrado con éxito.")
    print()
    print(f"Código: {nuevo_libro['cod']}")
    print(f"Título: {nuevo_libro['titulo']}")
    print(f"Autor: {nuevo_libro['autor']}")
    print(f"Cantidad de ejemplares disponibles: {nuevo_libro['cant_ej_ad']}")
    print(f"Cantidad de ejemplares prestados: {nuevo_libro['cant_ej_pr']}")
    return nuevo_libro

def eliminar_ejemplar_libro():
    codigo = (input("Por favor, ingrese el codigo: "))
    libro_encontrado = False
    for libro in libros:
        if codigo == libro['cod']:
            libro_encontrado = True
            break
    
    if libro_encontrado:
        if libro['cant_ej_ad'] > 0:
            libro['cant_ej_ad'] = libro['cant_ej_ad'] - 1
            print("Se ha eliminado un ejemplar del libro.")
        else:
            print("No hay ejemplares disponibles de este libro.")
    else:
        print("El libro no existe en la biblioteca.")

    return libro_encontrado

def prestar_ejemplar_libro():
    codigo_ingresado = input("Ingrese el código del libro: ")
    libro_encontrado = False
    for libro in libros:
        if libro['cod'] == codigo_ingresado:
            libro_encontrado=True
            break
    
    if libro_encontrado:
        print(f"Libro encontrado:")
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        if libro['cant_ej_ad'] == 0:
            print("No hay más ejemplares disponibles.")
        else:
            print(f"Cantidad de ejemplares disponibles: {libro['cant_ej_ad']}")
            libro['cant_ej_ad'] = libro['cant_ej_ad'] - 1
            libro['cant_ej_pr'] = libro['cant_ej_pr'] + 1
            print(f"Cantidad actual de ejemplares disponibles: {libro['cant_ej_ad']}")
            print(f"Cantidad actual de ejemplares prestados: {libro['cant_ej_pr']}")
            print()
            print("Operación exitosa.")
    else:
        print("Error: El código de libro ingresado no existe.")
    return libro_encontrado


def devolver_ejemplar_libro():
    codigo_ingresado = input("Ingrese el código del libro: ")
    libro_encontrado = False
    for libro in libros:
        if libro['cod'] == codigo_ingresado:
            libro_encontrado=True
            break

    if libro_encontrado:
        if libro['cant_ej_pr'] == 0:
            print("Error. No hay ejemplares prestados de este libro.")
        else:
            print("Libro devuelto con éxito.")
            libro['cant_ej_pr'] = libro['cant_ej_pr'] - 1
            libro['cant_ej_ad'] = libro['cant_ej_ad'] + 1
            print(f"Cantidad actual de ejemplares disponibles: {libro['cant_ej_ad']}")
            print(f"Cantidad actual de ejemplares prestados: {libro['cant_ej_pr']}")
    else:
        print("Error: El libro no existe en la biblioteca.")
    return libro_encontrado


"""def nuevo_libro():
    #COMPLETAR
    return None"""