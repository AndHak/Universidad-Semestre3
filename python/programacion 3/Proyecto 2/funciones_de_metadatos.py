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

