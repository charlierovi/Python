import fitz

with fitz.open("contrato.pdf") as pdf:
    texto_completo = ""
    for pagina in pdf:
        texto_completo += pagina.get_text()

with open("contrato.txt", "w", encoding="utf-8") as archivo_txt:
    archivo_txt.write(texto_completo)

print("Texto extraído y guardado correctamente en contrato.txt")
