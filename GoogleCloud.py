import subprocess
import os

def run_command(command):
    subprocess.call(command, shell=True)

# Establecemos la variable de entorno GRUPO_NUMERO
os.environ["GROUP_NUMBER"] = "47"

# Comprobamos que todas las dependencias estén actualizadas
run_command("sudo apt-get update -y")

# Descargamos pip3 para luego instalarlo en requirements
run_command("sudo apt install python3-pip -y")

# Descargamos los archivos proporcionados para la práctica
run_command("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git") 

# Usando pip3, instalamos las dependencias especificadas en el fichero requirements.txt
run_command("pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt")

fin = open("practica_creativa2/bookinfo/src/productpage/productpage_monolith.py", 'r') # Fichero de entrada necesario para ejecutar la aplicación
fout = open("practica_creativa2/bookinfo/src/productpage/productpage_monolith2.py", 'w') # Fichero de salida
for line in fin:
  if "'title': 'The Comedy of Errors'," in line :
    fout.write("'title': 'The Comedy of Errors ' +os.environ['GROUP_NUMBER'],")
  elif "'author': book['authors'][0]," in line :
    fout.write(line + " 'grupo' : os.environ['GROUP_NUMBER'],\n")
  else:
   fout.write(line)
fin.close()
fout.close()

run_command("sudo cp practica_creativa2/bookinfo/src/productpage/productpage_monolith2.py practica_creativa2/bookinfo/src/productpage/productpage_monolith.py")
run_command("sudo rm practica_creativa2/bookinfo/src/productpage/productpage_monolith2.py")

# Actualizamos el archivo productpage.html para que aparezca el nombre del grupo
input_file_path = "practica_creativa2/bookinfo/src/productpage/templates/productpage.html"
output_file_path = "practica_creativa2/bookinfo/src/productpage/templates/productpage_edit.html"

with open(input_file_path, 'r') as fin, open(output_file_path, 'w') as fout:
    for line in fin:
        if "{% block title %}Simple Bookstore App{% endblock %}" in line:
            fout.write("{% block title %}Simple Bookstore App {{ details.grupo }}{% endblock %}")
        else:
            fout.write(line)

# Copiamos el fichero editado al original
run_command(f"sudo cp {output_file_path} {input_file_path}")

# Borramos el fichero de edición
run_command(f"sudo rm {output_file_path}")

# Ejecutamos la aplicación especificando el puerto 9080
run_command("python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080")
