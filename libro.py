# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    CodGenerado = generar_codigo()
    titulo = str(input("Ingrese el título: ")) 
    autor = str(input("Ingrese el autor: "))
    ej_adquiridos = int(input("Ingrese los ejemplares adquiridos: "))
    while ej_adquiridos < 0:
        print("Error. La cantidad de ejemplares adquiridos no puede ser negativa.")
        ej_adquiridos = int(input("Ingrese los ejemplares adquiridos: "))
        break

    libro_reg = {
        'cod': CodGenerado,
        'titulo': titulo,
        'autor': autor,
        'cant_ej_ad': ej_adquiridos,
        'cant_ej_pr': 0
    }
    return libro_reg

def generar_codigo():
    from cod_generator import generar
    codigo = generar()
    return codigo
