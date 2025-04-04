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
    
    if opcion == "5":  # Eliminar categoría
        print("\nCategorías disponibles:")
        categorias = [c.name for c in ruta_base.iterdir() if c.is_dir()]
        for i, cat in enumerate(categorias, 1):
            print(f"{i}. {cat}")
        
        try:
            cat_idx = int(input("\nElige categoría a eliminar (número): ")) - 1
            categoria = categorias[cat_idx]
            ruta_cat = ruta_base / categoria
            
            if len(list(ruta_cat.glob('*'))) == 0:
                ruta_cat.rmdir()
                print("\n¡Categoría eliminada con éxito!")
            else:
                print("\n¡La categoría no está vacía!")
        
        except:
            print("\n¡Error al eliminar categoría!")
    elif opcion == "6":  # Salir
        print("\n¡Hasta pronto!")
        break
    
    else:
        print("\nOpción no válida")
    
    input("\nPresiona Enter para continuar...")
