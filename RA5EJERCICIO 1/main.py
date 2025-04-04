import xmltodict
import json

xml_data = """<alumnos>
  <alumno>
    <nombre>Ana Martínez</nombre>
    <edad>21</edad>
    <curso>DAW</curso>
  </alumno>
  <alumno>
    <nombre>Carlos Gómez</nombre>
    <edad>22</edad>
    <curso>DAM</curso>
  </alumno>
</alumnos>"""

# Convertir XML a diccionario
dict_data = xmltodict.parse(xml_data)

# Convertir a JSON
json_data = json.dumps(dict_data, indent=2, ensure_ascii=False)

# Guardar en un archivo JSON
with open("alumnos.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

print("✅ Archivo 'alumnos.json' generado con éxito.")
