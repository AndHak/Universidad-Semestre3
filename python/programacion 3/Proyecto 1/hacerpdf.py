import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

def crear_pdf(datos):
    pdf_path = "C:\\Users\\Public\\Documents\\Wondershare\\CreatorTemp\\tmp8ay9wn62.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)
    
    # Espacio inicial
    c.drawString(100, 770, "")
    c.drawString(100, 760, "")
    
    # Establecer título principal
    c.setFont("Helvetica-Bold", 24)
    c.setFillColorRGB(27/255, 73/255, 101/255)
    c.drawCentredString(300, 730, "My Travel")
    
    # Restablecer color y fuente para el contenido
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    
    # Información básica
    y_position = 710
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.darkblue)
    c.drawString(100, y_position, "Información Básica")
    
    y_position -= 20
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(100, y_position, f"Título: {datos['titulo']}")
    
    y_position -= 20
    c.drawString(100, y_position, f"Destino: {datos['destino']}")
    
    fecha_inicio_str = '-'.join(map(str, datos['fecha_inicio']))
    fecha_fin_str = '-'.join(map(str, datos['fecha_fin']))
    
    y_position -= 20
    c.drawString(100, y_position, f"Fecha de Inicio: {fecha_inicio_str}")
    
    y_position -= 20
    c.drawString(100, y_position, f"Fecha de Fin: {fecha_fin_str}")
    
    y_position -= 20
    c.drawString(100, y_position, f"Presupuesto: ${datos['presupuesto']:.2f}")
    
    y_position -= 20
    c.drawString(100, y_position, f"Personas: {datos['personas']}")
    
    # Espacio adicional
    y_position -= 40
    
    # Detalles de vuelos
    vuelos = datos.get('vuelos')
    if vuelos:
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.darkblue)
        c.drawString(100, y_position, "Detalles de Vuelos")
        
        y_position -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_position, "Ida")
        c.drawString(300, y_position, "Regreso")
        
        y_position -= 20
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        c.drawString(100, y_position, f"Fecha de Ida: {vuelos.get('fecha_ida', 'N/A')}")
        c.drawString(300, y_position, f"Fecha de Regreso: {vuelos.get('fecha_regreso', 'N/A')}")
        
        y_position -= 20
        c.drawString(100, y_position, f"Hora de Ida: {vuelos.get('hora_ida', 'N/A')} {vuelos.get('ampm_ida', 'N/A')}")
        c.drawString(300, y_position, f"Hora de Regreso: {vuelos.get('hora_regreso', 'N/A')} {vuelos.get('ampm_regreso', 'N/A')}")
        
        y_position -= 20
        c.drawString(100, y_position, f"Costo de Ida: ${vuelos.get('costo_ida', 'N/A')}")
        c.drawString(300, y_position, f"Costo de Regreso: ${vuelos.get('costo_regreso', 'N/A')}")
    
    # Espacio adicional
    y_position -= 40
    
    # Detalles de alojamiento
    alojamiento = datos.get('alojamiento')
    if alojamiento:
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.darkblue)
        c.drawString(100, y_position, "Detalles de Alojamiento")
        
        y_position -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_position, "Inicio")
        c.drawString(300, y_position, "Fin")
        
        y_position -= 20
        c.setFont("Helvetica", 12)
        c.setFillColor(colors.black)
        c.drawString(100, y_position, f"Fecha de Inicio: {alojamiento.get('fecha_inicio', 'N/A')}")
        c.drawString(300, y_position, f"Fecha de Fin: {alojamiento.get('fecha_fin', 'N/A')}")
        
        y_position -= 20
        c.drawString(100, y_position, f"Hora de Inicio: {alojamiento.get('hora_inicio', 'N/A')} {alojamiento.get('ampm_inicio', 'N/A')}")
        c.drawString(300, y_position, f"Hora de Fin: {alojamiento.get('hora_fin', 'N/A')} {alojamiento.get('ampm_fin', 'N/A')}")
        
        y_position -= 20
        c.drawString(100, y_position, f"Tipo: {alojamiento.get('tipo', 'N/A')}")
        c.drawString(300, y_position, f"Costo: ${alojamiento.get('costo', 'N/A')}")
        
        y_position -= 20
        c.drawString(100, y_position, f"Dirección: {alojamiento.get('direccion', 'N/A')}")
        y_position -= 20
        c.drawString(100, y_position, f"Info Adicional: {alojamiento.get('info_adicional', 'N/A')}")
    
    # Espacio adicional
    y_position -= 40
    
    # Detalles de gastos
    gastos = datos.get('Gastos')
    if gastos:
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.darkblue)
        c.drawString(100, y_position, "Detalles de Gastos")
        
        y_position -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_position, "Descripción")
        c.drawString(250, y_position, "Costo")
        c.drawString(350, y_position, "Fecha")
        
        for gasto in gastos:
            y_position -= 20
            c.setFont("Helvetica", 12)
            c.setFillColor(colors.black)
            c.drawString(100, y_position, f"{gasto[0]}")
            c.drawString(250, y_position, f"${gasto[1]}")
            c.drawString(350, y_position, f"{gasto[2]}")
    
    # Espacio adicional
    y_position -= 40

    # Detalles del itinerario
    itinerario = datos.get('Itinerario')
    if itinerario:
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.darkblue)
        c.drawString(100, y_position, "Detalles del Itinerario")
        
        y_position -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y_position, "Descripción")
        c.drawString(250, y_position, "Hora")
        c.drawString(350, y_position, "Fecha")
        
        for plan in itinerario:
            y_position -= 20
            c.setFont("Helvetica", 12)
            c.setFillColor(colors.black)
            c.drawString(100, y_position, f"{plan[0]}")
            c.drawString(250, y_position, f"{plan[1]} {plan[2]}")
            c.drawString(350, y_position, f"{plan[3]}")
    
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
