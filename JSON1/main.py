import xml.etree.ElementTree as ET
import json

xml_data = '''
<alumnos>
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
</alumnos>
'''

root = ET.fromstring(xml_data)

alumnos = []
for alumno in root.findall('alumno'):
    datos = {
        'nombre': alumno.find('nombre').text,
        'edad': int(alumno.find('edad').text),
        'curso': alumno.find('curso').text
    }
    alumnos.append(datos)

json_data = {'alumnos': alumnos}

with open('alumnos.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

print("JSON guardado en 'alumnos.json'")
