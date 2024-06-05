import os
from pydub import AudioSegment

# Verifica si ffmpeg y ffprobe están en la ruta especificada
ffmpeg_path = r"C:\Users\andre\Downloads\FFMpeg\ffmpeg-2024-06-03-git-77ad449911-full_build\ffmpeg-2024-06-03-git-77ad449911-full_build\bin\ffmpeg.exe"
ffprobe_path = r"C:\Users\andre\Downloads\FFMpeg\ffmpeg-2024-06-03-git-77ad449911-full_build\ffmpeg-2024-06-03-git-77ad449911-full_build\bin\ffprobe.exe"

if not os.path.isfile(ffmpeg_path):
    raise FileNotFoundError(f"ffmpeg no se encuentra en la ruta especificada: {ffmpeg_path}")
if not os.path.isfile(ffprobe_path):
    raise FileNotFoundError(f"ffprobe no se encuentra en la ruta especificada: {ffprobe_path}")

AudioSegment.converter = ffmpeg_path
AudioSegment.ffprobe = ffprobe_path

def reproducir_musica(lista_de_reproduccion, all_songs_list):
    # Aquí debes proporcionar la ruta correcta al archivo de audio
    ruta_archivo = lista_de_reproduccion[0]  # Ejemplo: "C:/ruta/al/archivo.mp3"
    
    # Verifica si el archivo de audio existe
    if not os.path.isfile(ruta_archivo):
        raise FileNotFoundError(f"El archivo de audio no se encuentra en la ruta especificada: {ruta_archivo}")
    
    try:
        # Cargar el archivo de audio
        current_audio_segment = AudioSegment.from_file(ruta_archivo)
        # Aquí iría el código para reproducir la música
        print("Archivo de audio cargado correctamente") 
    except Exception as e:
        print(f"Error al cargar el archivo de audio: {e}")

# Llamar a la función para reproducir música
reproducir_musica([os.path.join(os.path.dirname(__file__), "canciones/Cinco Noches_ Paquito Guzman (letra)(MP3_128K).mp3")], [])
