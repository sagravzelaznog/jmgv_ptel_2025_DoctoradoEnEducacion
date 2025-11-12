import os
import re

# Define el footer a agregar
footer = '''
    <footer style="background-color: var(--primary-color); color: white; text-align: center; padding: 2rem 0; margin-top: 3rem;">
        <div class="container">
            <p>&copy; JMGV-PTEL-2025. TODOS LOS DERECHOS RESERVADOS</p>
        </div>
    </footer>
'''

# Directorio donde están los archivos HTML
html_dir = r"c:\Users\admin\Documents\000 A PREPA\planeaciones especialidades\doctorado en educacion"

# Recorre todos los archivos HTML en el directorio
for filename in os.listdir(html_dir):
    if filename.endswith('.html'):
        filepath = os.path.join(html_dir, filename)
        
        try:
            # Lee el contenido del archivo
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Verifica si el footer ya existe
            if 'JMGV-PTEL-2025' in content:
                print(f'El archivo {filename} ya tiene el footer. Saltando...')
                continue
                
            # Busca el cierre del body y agrega el footer antes
            if '</body>' in content:
                new_content = content.replace('</body>', f'{footer}</body>')
                
                # Escribe el contenido actualizado
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f'Footer agregado a {filename}')
            else:
                print(f'No se encontró la etiqueta </body> en {filename}')
                
        except Exception as e:
            print(f'Error al procesar {filename}: {str(e)}')
