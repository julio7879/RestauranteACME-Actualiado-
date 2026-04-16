import csv, os

def obtener_ruta(archivo):
    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(carpeta, exist_ok=True) 
    return os.path.join(carpeta, archivo.strip("/"))

def guardar_archivo(lista, nombre, campos):
    ruta = obtener_ruta(nombre)
    with open(ruta, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(lista)

def cargar_datos(nombre):
    ruta = obtener_ruta(nombre)
    if not os.path.exists(ruta): return []
    with open(ruta, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))