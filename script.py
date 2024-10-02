import sys
import os

def contar_lineas_y_palabras(archivo):
    # Inicializar contadores
    lineas = 0
    palabras = 0
    conteo_python = 0

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                lineas += 1  # Contar líneas
                # Contar palabras en la línea
                palabras_en_linea = linea.split()
                palabras += len(palabras_en_linea)  # Sumar palabras
                # Contar cuántas veces aparece "Python"
                conteo_python += linea.lower().count("python")  # Contar "Python" (case insensitive)

    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")

    return lineas, palabras, conteo_python

def main():
    # Verifica si se proporcionó un argumento
    if len(sys.argv) < 2:
        print("Error: No se proporcionó un directorio.")
        print("Uso: python nombre_del_script.py <directorio>")
        sys.exit(1)

    directorio = sys.argv[1]

    # Verificar si el directorio existe
    if not os.path.isdir(directorio):
        print(f"Error: El directorio {directorio} no existe.")
        sys.exit(1)

    # Buscar archivos .txt en el directorio
    for archivo in os.listdir(directorio):
        if archivo.endswith(".txt"):
            ruta_archivo = os.path.join(directorio, archivo)
            lineas, palabras, conteo_python = contar_lineas_y_palabras(ruta_archivo)

            print(f"Archivo: {archivo}")
            print(f"Líneas: {lineas}, Palabras: {palabras}, 'Python' encontrado: {conteo_python} veces\n")

if __name__ == "__main__":
    main()
