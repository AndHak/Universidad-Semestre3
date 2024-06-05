from pydub import AudioSegment
import imageio_ffmpeg as ffmpeg

# Configurar las rutas de ffmpeg y ffprobe
AudioSegment.converter = ffmpeg.get_ffmpeg_exe()
AudioSegment.ffmpeg = ffmpeg.get_ffmpeg_exe()
AudioSegment.ffprobe = ffmpeg.get_ffprobe_exe()

print("ffmpeg executable: ", AudioSegment.converter)
print("ffprobe executable: ", AudioSegment.ffprobe)

# Intenta cargar un archivo de audio de prueba
try:
    audio = AudioSegment.from_file("C:\Programacion Universidad\Semestre 3\python\programacion 3\Proyecto 2\canciones\Shape of my Heart.mp3", format="mp3")
    print("Archivo de audio cargado correctamente")
except Exception as e:
    print(f"Error al cargar el archivo de audio: {e}")
