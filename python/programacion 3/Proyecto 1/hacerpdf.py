import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def crear_pdf(datos):
    pdf_path = "C:\\Users\\Public\\Documents\\Wondershare\\CreatorTemp\\tmp8ay9wn62.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    
    # Establecer título principal
    c.setFont("Helvetica-Bold", 24)
    c.setFillColorRGB(27/255, 73/255, 101/255)
    # Espacio adicional
    c.drawString(100, 530, "")
    # Espacio adicional
    c.drawString(100, 530, "")
    c.drawCentredString(300, 770, "My Travel")
    
    # Restablecer color y fuente para el contenido
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    
    # Información básica
    c.drawString(100, 750, f"Título: {datos['titulo']}")
    c.drawString(100, 730, f"Destino: {datos['destino']}")
    
    # Convertir los elementos de fecha_inicio y fecha_fin a cadenas
    fecha_inicio_str = '-'.join(map(str, datos['fecha_inicio']))
    fecha_fin_str = '-'.join(map(str, datos['fecha_fin']))
    
    c.drawString(100, 710, f"Fecha de Inicio: {fecha_inicio_str}")
    c.drawString(100, 690, f"Fecha de Fin: {fecha_fin_str}")
    c.drawString(100, 670, f"Presupuesto: {datos['presupuesto']}")
    c.drawString(100, 650, f"Personas: {datos['personas']}")

    # Espacio adicional
    c.drawString(100, 530, "")
    
    # Detalles de vuelos
    vuelos = datos.get('vuelos')
    if vuelos:
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.darkblue)
        c.drawString(100, 630, "Detalles de Vuelos:")
        
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, 610, "Ida:")
        c.drawString(300, 610, "Regreso:")
        
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        c.drawString(100, 590, f"Fecha de Ida: {vuelos.get('fecha_ida', 'N/A')}")
        c.drawString(300, 590, f"Fecha de Regreso: {vuelos.get('fecha_regreso', 'N/A')}")
        
        c.drawString(100, 570, f"Hora de Ida: {vuelos.get('hora_ida', 'N/A')} {vuelos.get('ampm_ida', 'N/A')}")
        c.drawString(300, 570, f"Hora de Regreso: {vuelos.get('hora_regreso', 'N/A')} {vuelos.get('ampm_regreso', 'N/A')}")
        
        c.drawString(100, 550, f"Costo de Ida: {vuelos.get('costo_ida', 'N/A')}")
        c.drawString(300, 550, f"Costo de Regreso: {vuelos.get('costo_regreso', 'N/A')}")
    
    # Espacio adicional
    c.drawString(100, 530, "")
    
    # Detalles de alojamiento
    alojamiento = datos.get('alojamiento')
    if alojamiento:
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.darkblue)
        c.drawString(100, 510, "Detalles de Alojamiento:")
        
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, 490, "Inicio:")
        c.drawString(300, 490, "Fin:")
        
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        c.drawString(100, 470, f"Fecha de Inicio: {alojamiento.get('fecha_inicio', 'N/A')}")
        c.drawString(300, 470, f"Fecha de Fin: {alojamiento.get('fecha_fin', 'N/A')}")
        
        c.drawString(100, 450, f"Hora de Inicio: {alojamiento.get('hora_inicio', 'N/A')} {alojamiento.get('ampm_inicio', 'N/A')}")
        c.drawString(300, 450, f"Hora de Fin: {alojamiento.get('hora_fin', 'N/A')} {alojamiento.get('ampm_fin', 'N/A')}")
        
        c.drawString(100, 430, f"Tipo: {alojamiento.get('tipo', 'N/A')}")
        c.drawString(300, 430, f"Costo: {alojamiento.get('costo', 'N/A')}")
        
        c.drawString(100, 410, f"Dirección: {alojamiento.get('direccion', 'N/A')}")
        c.drawString(100, 390, f"Info Adicional: {alojamiento.get('info_adicional', 'N/A')}")
    
    c.save()
    
    print(f"PDF created at {pdf_path}")
    abrir_pdf_temporalmente(pdf_path)

def abrir_pdf_temporalmente(pdf_path):
    # Esta función abre el PDF temporalmente
    if sys.platform == "win32":
        os.startfile(pdf_path)
    elif sys.platform == "darwin":
        os.system(f"open {pdf_path}")
    else:
        os.system(f"xdg-open {pdf_path}")

# Ejemplo de uso
datos = {
    "titulo": "Viaje a Paris",
    "destino": "Paris, Francia",
    "fecha_inicio": ["01", "Ene", 2024],
    "fecha_fin": ["10", "Ene", 2024],
    "presupuesto": 1500,
    "personas": 2,
    "vuelos": {
        "fecha_ida": "01-Ene-2024",
        "hora_ida": "10:00",
        "ampm_ida": "AM",
        "fecha_regreso": "10-Ene-2024",
        "hora_regreso": "08:00",
        "ampm_regreso": "PM",
        "costo_ida": 500,
        "costo_regreso": 500
    },
    "alojamiento": {
        "tipo": "Hotel",
        "direccion": "123 Rue de Paris",
        "fecha_inicio": "01-Ene-2024",
        "hora_inicio": "12:00",
        "ampm_inicio": "PM",
        "fecha_fin": "10-Ene-2024",
        "hora_fin": "10:00",
        "ampm_fin": "AM",
        "costo": 500,
        "info_adicional": "Hotel de 4 estrellas"
    }
}

crear_pdf(datos)
