# Proyecto Recetas

Este proyecto es una aplicación interactiva que permite al usuario gestionar recetas de cocina almacenadas en archivos de texto dentro de una estructura de carpetas específica.

**Estructura del Proyecto:**

El proyecto asume la siguiente estructura de carpetas en el directorio base del usuario:

Recetas/
├── Carnes/
│   ├── receta1_carnes.txt
│   └── receta2_carnes.txt
├── Ensaladas/
│   ├── receta1_ensaladas.txt
│   └── receta2_ensaladas.txt
├── Pasta/
│   ├── receta1_pasta.txt
│   └── receta2_pasta.txt
└── Postres/
├── receta1_postres.txt
└── receta2_postres.txt

Dentro de cada una de estas cuatro carpetas (Carnes, Ensaladas, Pasta, Postres), se encuentran dos archivos de texto que representan recetas individuales. El usuario puede escribir el contenido de estas recetas directamente en los archivos o, si lo prefiere, puede descargar y descomprimir un archivo adjunto con esta estructura.

**Funcionalidades del Programa:**

Al ejecutar el programa, el usuario será recibido con un mensaje de bienvenida y se le informará sobre la ruta de acceso al directorio "Recetas" y la cantidad de recetas existentes dentro de él. A continuación, se le presentará un menú con las siguientes opciones:

1.  **Leer una receta:** El programa preguntará al usuario qué categoría de receta desea leer (carnes, ensaladas, etc.). Una vez que elija una categoría, se le preguntará qué receta específica desea leer y, finalmente, se mostrará el contenido de esa receta.
2.  **Crear una nueva receta:** El programa preguntará al usuario en qué categoría desea crear la nueva receta. Luego, le pedirá que escriba el nombre y el contenido de la nueva receta, y el programa creará un nuevo archivo de texto con esa información en la carpeta correspondiente.
3.  **Crear una nueva categoría:** El programa preguntará al usuario el nombre de la nueva categoría que desea crear y generará una nueva carpeta con ese nombre dentro del directorio "Recetas".
4.  **Eliminar una receta:** Similar a la opción 1, el programa preguntará al usuario qué categoría y qué receta desea eliminar, y procederá a borrar el archivo correspondiente.
5.  **Eliminar una categoría:** El programa preguntará al usuario qué categoría desea eliminar y borrará la carpeta completa con todas las recetas que contenga.
6.  **Finalizar la ejecución:** Esta opción cerrará el programa.

**Consideraciones Adicionales:**

* Después de que el usuario complete exitosamente cualquiera de las opciones (excepto la opción 6), el programa le pedirá que presione cualquier tecla para volver al menú principal y realizar otra acción.

En resumen, este proyecto proporciona una interfaz sencilla para organizar, leer, crear y eliminar recetas de cocina utilizando una estructura de archivos y carpetas en el sistema local del usuario.
