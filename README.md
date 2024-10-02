# Script de Conteo de Líneas, Palabras y Frecuencia de "Python"

**Propietario del repositorio:** Sergio Quesada

## Uso del Script

1. Preparación:
Coloca los archivos de texto (.txt) que deseas analizar dentro de un directorio específico.

2. Ejecución:
-Abre una terminal y navega al directorio donde tienes el script.
-Ejecuta el siguiente comando:
python nombre_del_script.py <directorio>
-Reemplaza <directorio> con la ruta al directorio donde están los archivos .txt que quieres analizar.

3. Resultado:
-El script buscará archivos .txt en el directorio proporcionado y para cada uno mostrará:
-El número de líneas.
-El número total de palabras.
-La cantidad de veces que aparece la palabra "Python".

## Ejemplos de resultados
-Archivo: file1.txt
Líneas: 20, Palabras: 150, 'Python' encontrado: 3 veces

-Archivo: file2.txt
Líneas: 10, Palabras: 80, 'Python' encontrado: 1 vez

## Explicación del Código
Módulos utilizados:
-sys: Para manejar los argumentos de línea de comandos.
-os: Para navegar en el sistema de archivos y verificar la existencia de directorios.

Funciones:
-contar_lineas_y_palabras(archivo): Lee un archivo de texto, cuenta las líneas, palabras, y la frecuencia de la palabra "Python".
-main(): Controla el flujo del programa. Verifica que se haya pasado un directorio, valida si existe, y procesa los archivos .txt que encuentra.

Manejo de Errores:
-Si no se proporciona un directorio como argumento, el programa mostrará un mensaje de error con las instrucciones correctas de uso.
-Si el directorio no existe, se detiene el programa mostrando un mensaje de error.
-Si hay algún problema al leer los archivos (por ejemplo, permisos o archivos corruptos), el script lo indicará con un mensaje de error específico.