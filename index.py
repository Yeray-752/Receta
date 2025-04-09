from pathlib import Path
import os

# Ruta base donde ya existen las recetas (esta parte se mantiene según tu indicación)
ruta_base = Path('D:\\ssf\\Recetas')

# Función para contar recetas (esta parte se mantiene según tu indicación)
def contar_recetas():
    total = 0
    if ruta_base.is_dir():
        for categoria in ruta_base.iterdir():
            if categoria.is_dir():
                total += len(list(categoria.glob('*.txt')))
    return total

# Función para leer una receta (modificada para usar las rutas fijas)
def leer_receta():
    print("\n=== LEER RECETA ===")
    print("\nElige una categoría:")
    print("1. Carnes")
    print("2. Ensaladas")
    print("3. Pastas")
    print("4. Postres")

    while True:
        opcion_categoria = input("Selecciona el número de la categoría: ")
        if opcion_categoria in ['1', '2', '3', '4']:
            break
        else:
            print("Opción inválida. Por favor, elige un número del 1 al 4.")

    if opcion_categoria == '1':
        print("\nRecetas de Carnes:")
        print("a. Matambre a la Pizza")
        print("b. Entrecot al Malbec")
        while True:
            opcion_receta = input("Selecciona la letra de la receta: ").lower()
            if opcion_receta == 'a':
                ruta_carnes = Path('C:/Users/mijim/OneDrive/Documentos/DAW/SSF/python/Recetas1/Recetas/Carnes')
                archivo_pizza = ruta_carnes / 'Matambre_a_la_Pizza.txt'
                try:
                    with open(archivo_pizza, 'r', encoding='utf-8') as archivo:
                        print("\n=== Matambre a la Pizza ===")
                        print(archivo.read())
                    break
                except FileNotFoundError:
                    print("Error: Archivo no encontrado.")
                    break
            elif opcion_receta == 'b':
                ruta_carnes = Path('C:/Users/mijim/OneDrive/Documentos/DAW/SSF/python/Recetas1/Recetas/Carnes')
                archivo_Entrecot = ruta_carnes / 'Entrecot al Malbec.txt'
                try:
                    with open(archivo_Entrecot, 'r', encoding='utf-8') as archivo:
                        print("\n=== Entrecot al Malbec ===")
                        print(archivo.read())
                    break
                except FileNotFoundError:
                    print("Error: Archivo no encontrado.")
                    break
            else:
                print("Opción inválida.")

    elif opcion_categoria == '2':
        print("\nRecetas de Ensaladas:")
        print("a. Ensalada Griega")
        print("b. Ensalada Mediterranea")
        while True:
            opcion_receta = input("Selecciona la letra de la receta: ").lower()
            if opcion_receta == 'a':
                ruta_ensaladas = Path('C:/Users/mijim/OneDrive/Documentos/DAW/SSF/python/Recetas1/Recetas/Ensaladas')
                archivo_griega = ruta_ensaladas / 'Ensalada Griega.txt'
                try:
                    with open(archivo_griega, 'r', encoding='utf-8') as archivo:
                        print("\n=== Ensalada Griega ===")
                        print(archivo.read())
                    break
                except FileNotFoundError:
                    print("Error: Archivo no encontrado.")
                    break
            elif opcion_receta == 'b':
                ruta_ensaladas = Path('C:/Users/mijim/OneDrive/Documentos/DAW/SSF/python/Recetas1/Recetas/Ensaladas')
                archivo_mediterraneo = ruta_ensaladas / 'Ensalada Mediterranea.txt'
                try:
                    with open(archivo_mediterraneo, 'r', encoding='utf-8') as archivo:
                        print("\n=== Ensalada Mediterranea ===")
                        print(archivo.read())
                    break
                except FileNotFoundError:
                    print("Error: Archivo no encontrado.")
                    break
            else:
                print("Opción inválida.")

    elif opcion_categoria == '3':
        print("\nRecetas de Pastas:")
        print("a. Canelones de Espinaca")
        print("b. Ravioles de Ricotta")
        while True:
            opcion_receta = input("Selecciona la letra de la receta: ").lower()
            if opcion_receta == 'a':
                ruta_pastas = Path('C:/Users/mijim/OneDrive/Documentos/DAW/SSF/python/Recetas1/Recetas/Pastas')
                archivo_espinaca = ruta_pastas / 'Canelones de Espinaca.txt'
                try:
                    with open(archivo_espinaca, 'r', encoding='utf-8') as archivo:
                        print("\n=== Canelones de Espinaca ===")
                        print(archivo.read())
                    break
                except FileNotFoundError:
                    print("Error: Archivo no encontrado.")
                    break
            elif opcion_receta == 'b':
                ruta_pastas = Path('C:/Users/mijim/OneDrive/Documentos/DAW/SSF/python/Recetas1/Recetas/Pastas')
                archivo_ricotta = ruta_pastas / 'Ravioles de Ricotta.txt'
                try:
                    with open(archivo_ricotta, 'r', encoding='utf-8') as archivo:
                        print("\n=== Ravioles de Ricotta ===")
                        print(archivo.read())
                    break
                except FileNotFoundError:
                    print("Error: Archivo no encontrado.")
                    break
            else:
                print("Opción inválida.")

    elif opcion_categoria == '4':
        print("\nRecetas de Postres:")
        print("a. Compota de Manzana")
        print("b. Tarta de Frambuesa")
        while True:
            opcion_receta = input("Selecciona la letra de la receta: ").lower()
            if opcion_receta == 'a':
                ruta_postres = Path('C:/Users/mijim/OneDrive/Documentos/DAW/SSF/python/Recetas1/Recetas/Postres')
                archivo_manzana = ruta_postres / 'Compota de Manzana.txt'
                try:
                    with open(archivo_manzana, 'r', encoding='utf-8') as archivo:
                        print("\n=== Compota de Manzana ===")
                        print(archivo.read())
                    break
                except FileNotFoundError:
                    print("Error: Archivo no encontrado.")
                    break
            elif opcion_receta == 'b':
                ruta_postres = Path('C:/Users/mijim/OneDrive/Documentos/DAW/SSF/python/Recetas1/Recetas/Postres')
                archivo_frambuesa = ruta_postres / 'Tarta de Frambuesa.txt'
                try:
                    with open(archivo_frambuesa, 'r', encoding='utf-8') as archivo:
                        print("\n=== Tarta de Frambuesa ===")
                        print(archivo.read())
                    break
                except FileNotFoundError:
                    print("Error: Archivo no encontrado.")
                    break
            else:
                print("Opción inválida.")

# Función para crear una nueva receta (manteniendo la lógica original para la ruta base 'D:\\ssf\\Recetas')
def crear_receta():
    print("\n=== CREAR RECETA ===")
    if not ruta_base.is_dir():
        print("No se pueden crear recetas. La ruta base no existe.")
        return

    categorias = [d.name for d in ruta_base.iterdir() if d.is_dir()]
    if not categorias:
        print("No hay categorías disponibles para crear recetas.")
        crear_categoria()
        return

    print("\nCategorías disponibles:")
    for i, categoria in enumerate(categorias):
        print(f"{i+1}. {categoria}")

    while True:
        try:
            seleccion_categoria_index = int(input("Elige el número de la categoría para la nueva receta: ")) - 1
            if 0 <= seleccion_categoria_index < len(categorias):
                categoria_seleccionada = ruta_base / categorias[seleccion_categoria_index]
                break
            else:
                print("Opción inválida. Por favor, elige un número de la lista.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

    nombre_receta = input("Introduce el nombre de la nueva receta (sin extensión .txt): ")
    nombre_archivo = f"{nombre_receta}.txt"
    ruta_nueva_receta = categoria_seleccionada / nombre_archivo

    if ruta_nueva_receta.exists():
        print(f"Advertencia: La receta '{nombre_archivo}' ya existe en esta categoría.")
        confirmacion = input("¿Deseas sobreescribirla? (s/n): ").lower()
        if confirmacion != 's':
            print("Creación de receta cancelada.")
            return

    print("\nEscribe el contenido de la receta (termina con una línea en blanco o presiona Ctrl+D en Linux/macOS o Ctrl+Z luego Enter en Windows):")
    contenido = []
    while True:
        try:
            linea = input()
            contenido.append(linea)
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        if not linea:
            break

    try:
        categoria_seleccionada.mkdir(parents=True, exist_ok=True)
        with open(ruta_nueva_receta, 'w', encoding='utf-8') as archivo:
            archivo.write('\n'.join(contenido))
        print(f"\nReceta '{nombre_archivo}' creada exitosamente en '{categoria_seleccionada.name}'.")
    except Exception as e:
        print(f"Ocurrió un error al crear la receta: {e}")

# Función para crear una nueva categoría (manteniendo la lógica original)
def crear_categoria():
    print("\n=== CREAR CATEGORÍA ===")
    nombre_categoria = input("Introduce el nombre de la nueva categoría: ")
    ruta_nueva_categoria = ruta_base / nombre_categoria

    if ruta_nueva_categoria.exists() and ruta_nueva_categoria.is_dir():
        print(f"Advertencia: La categoría '{nombre_categoria}' ya existe.")
    else:
        try:
            ruta_nueva_categoria.mkdir(parents=True, exist_ok=True)
            print(f"Categoría '{nombre_categoria}' creada exitosamente.")
        except Exception as e:
            print(f"Ocurrió un error al crear la categoría: {e}")

# Menú principal (solo opciones 1 y 2)
while True:
    print("\n=== RECETARIO ===")
    print(f"Ubicación de las nuevas recetas: {ruta_base}")
    print(f"Total recetas en la ubicación de nuevas recetas: {contar_recetas()}")

    print("\nOpciones:")
    print("1. Leer receta")
    print("2. Crear receta")
    print("6. Salir")

    opcion = input("\nElige una opción (1, 2 o 6): ")

    if opcion == '1':
        leer_receta()
    elif opcion == '2':
        crear_receta()
    elif opcion == '6':
        print("Saliendo del recetario. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elige 1, 2 o 6.")