from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Nombre del archivo PDF
pdf_file = "contrato.pdf"

# Crear el PDF
c = canvas.Canvas(pdf_file, pagesize=letter)
c.setFont("Helvetica", 12)

# Agregar contenido al PDF
c.drawString(100, 750, "Contrato de prestación de servicios")
c.drawString(100, 730, "Cliente: Juan Pérez")
c.drawString(100, 710, "Fecha: 15/03/2024")
c.drawString(100, 690, "Servicio: Desarrollo web")

# Guardar el archivo PDF
c.save()

print(f"✅ Archivo '{pdf_file}' creado con éxito.")

import fitz  # PyMuPDF

# Ruta del archivo PDF de entrada y del TXT de salida
pdf_file = "contrato.pdf"
txt_file = "contrato.txt"

try:
    # Abrir el PDF
    with fitz.open(pdf_file) as pdf:
        text = ""
        for page in pdf:  # Iterar sobre cada página del PDF
            text += page.get_text("text") + "\n"

    # Guardar el texto extraído en un archivo TXT
    with open(txt_file, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"✅ Texto extraído y guardado en '{txt_file}'.")
except FileNotFoundError:
    print(f"❌ Error: No se encontró el archivo '{pdf_file}'. Verifica la ruta.")
except Exception as e:
    print(f"❌ Error inesperado: {e}")


