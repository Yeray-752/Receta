import os 
from os import system
from pathlib import Path
import shutil

# Ruta base donde ya existen las recetas
ruta_base = Path('C:\\Recetas')

# WARNING Para que el codigo funcione perfectamente deberias extraer el ZIP en el dico C:, para que la ruta sea la misma.

# Función para contar recetas
def contar_recetas():
    total = 0
    for categoria in ruta_base.iterdir():
        if categoria.is_dir():
            total += len(list(categoria.glob('*.txt')))
    return total

def MostrarCategoria():
    print('Categorias: \n')
    contenido = os.listdir('C:\\Recetas\\')

    for elemento in contenido:
        print(elemento)

    Categoria = input ('Elige la Categoria que quieres leer: ')

    system('cls')
    return Categoria

        

# Menú principal
while True:
    system('cls')
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

    system('cls')

    if opcion == '1':
        
        categoria = MostrarCategoria()

        system('cls')

        contenido2 = os.listdir('C:\\Recetas\\' + categoria)
        print(f"Contenido de '{categoria}':\n")
        for elemento in contenido2:
            print(elemento)

        Leer = input('\nCopie el nombre del archivo que quiere abrir: ')

        system('cls')

        archivo = open('C:\\Recetas\\' + categoria +'\\' + Leer)

        print(archivo.read() + '\n')

        salir = input('Pulse 6 para salir: ')

        if salir == 6:
            
            break

    

    elif opcion == '2':

        categoria =  MostrarCategoria()

        system('cls')

        contenido2 = os.listdir('C:\\Recetas\\' + categoria)
        print(f"Contenido de '{categoria}':\n")
        for elemento in contenido2:
            print(elemento)



        Crear = input('\nIndique el nombre del archivo que quiere crear: ')

        system('cls')

        ruta2 = 'C:\\Recetas\\' + categoria + '\\' + Crear
        with open(ruta2, "w") as archivo:
         texto = input('Escriba la Receta...: ')
         archivo.write(texto)

    elif opcion == '3':

        NombreCategoria = input('\n Dime el nombre de la Categorias que quieres  crear: ')
        os.mkdir('C:\\Recetas\\' + NombreCategoria)
        print('Se ha creado la carpeta')

    elif opcion == '4':
        
        categoria = MostrarCategoria()

        contenido = os.listdir('C:\\Recetas\\' + categoria)
        
        print(f"Contenido de '{categoria}':")
        for elemento in contenido:
            print(elemento)

        RecetaEliminar = input('Ahora que recetas es la que quieres eliminar?: ')
        os.remove('C:\\Recetas\\' + categoria +'\\' + RecetaEliminar)

    elif opcion == '5':

        categoria = MostrarCategoria()

        contenido = os.listdir('C:\\Recetas\\' + categoria)
        
        print(f"Contenido de '{categoria}':")
        for elemento in contenido:
            print(elemento)

        
        shutil.rmtree('C:\\Recetas\\' + categoria)

    elif opcion == '6':
        break

    else:
        print('Numero no valido')
