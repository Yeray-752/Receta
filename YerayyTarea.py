import os
from pathlib import Path

# Ruta base donde ya existen las recetas
ruta_base = Path('C:\\Users\\chago\\Desktop\\Clases\\sistemas informaticos\\Phyton\\Recetas (1)\\Recetas')


# Función para contar recetas
def contar_recetas():
    total = 0
    for categoria in ruta_base.iterdir():
        if categoria.is_dir():
            total += len(list(categoria.glob('*.txt')))
    return total

# Menú principal
while True:
    print("\n=== RECETARIO ===")
    print(f"Ubicación: {ruta_base}")
    print(f"Total recetas: {contar_recetas()}")
    
    print("\nOpciones:")
    print("1. Leer receta")
    print("2. Crear receta")
    print("3. Crear categoría")
    print("4. Eliminar receta")
    print("5. Eliminar categoría")
    print("6. Salir")
    
    opcion = input("\nElige una opción (1-6): ")
    
    if opcion == '3':
        NombreCategoria = input('\n Dime el nombre de la Categorias que quieres  crear: ')
        os.mkdir('C:\\Users\\chago\\Desktop\\Clases\\sistemas informaticos\\Phyton\\Recetas (1)\\Recetas\\' + NombreCategoria)
        print('Se ha creado la carpeta')

    elif opcion == '4':
        contenido = os.listdir('C:\\Users\\chago\\Desktop\\Clases\\sistemas informaticos\\Phyton\\Recetas (1)\\Recetas\\')
        print(f"Contenido de Recetas:")
        for elemento in contenido:
            print(elemento)
        CarpetaReceta = input('De que categorias es la receta que quieres eliminar?: ')
        contenido2 = os.listdir('C:\\Users\\chago\\Desktop\\Clases\\sistemas informaticos\\Phyton\\Recetas (1)\\Recetas\\' + CarpetaReceta)
        print(f"Contenido de '{CarpetaReceta}':")
        for elemento in contenido2:
            print(elemento)
        RecetaEliminar = input('Ahora que recetas es la que quieres eliminar?: ')
        os.remove('C:\\Users\\chago\\Desktop\\Clases\\sistemas informaticos\\Phyton\\Recetas (1)\\Recetas\\' + CarpetaReceta +'\\' + RecetaEliminar)
    elif opcion == '6':
        break