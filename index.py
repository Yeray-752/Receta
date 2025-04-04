import os
from pathlib import Path

# Ruta base donde ya existen las recetas
ruta_base = Path('D:\\ssf\\Recetas')

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
    
