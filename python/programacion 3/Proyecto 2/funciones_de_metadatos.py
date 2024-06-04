from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, USLT
import os


def extraer_imagen(ruta_archivo):
    try:
        audio = MP3(ruta_archivo, ID3=ID3)
        tags = audio.tags
        for tag in tags.values():
            if isinstance(tag, APIC):
                imagen_data = tag.data
                # Aquí puedes guardar la imagen o convertirla a un formato usable
                return bytes(imagen_data)  # Convertir a bytes antes de devolverlos
    except Exception as e:
        print("Error al extraer la imagen de los metadatos:", e)
        
    return None

def extraer_info_cancion(ruta_archivo):
    #Eliminar la extension del archivo
    nombre_archivo = os.path.splitext(os.path.basename(ruta_archivo))[0]

    #separar el nombre y el artista
    partes = nombre_archivo.split(",")
    if len(partes) == 2:
        titulo = partes[0].strip()
        artista = partes[1].strip()
    else:
        #Caso para el guion
        partes = nombre_archivo.split("-")
        if len(partes) == 2:
            titulo = partes[0].strip()
            artista = partes[1].strip()
        else:
            titulo = partes[0].strip()
            artista = "Desconocido"

    return titulo, artista

def extraer_letra_y_tiempo(ruta_archivo):
    try:
        audio = ID3(ruta_archivo)
        # Verificar si hay letras y marcas de tiempo en los metadatos
        if 'USLT' in audio:
            letra = audio['USLT'].text[0]
            # Supongamos que las marcas de tiempo están en el formato [mm:ss.xx]
            marcas_tiempo = [(float(linea.split(']')[0][1:].replace(':', '.')), linea.split(']')[1]) for linea in letra.split('\n')]
            return marcas_tiempo
        else:
            print("No se encontraron letras y marcas de tiempo en los metadatos.")
    except Exception as e:
        print("Error al extraer la letra y marcas de tiempo de los metadatos:", e)
    
    return None