# GranjaAPP

# Instrucciones de instalación:
1. Validamos que la máquina tenga instalado Python 3.
2. Instalar modulo virtualenv de Python:
	`pip install virtualenv`
3. Creamos un ambiente virtual para instalar las dependencias del proyecto. 
  `virtualenv <Nombre del entorno>`

4. Activamos el entorno virtual, ingresamos dentro de la carpeta   <Nombre del entorno> y ejecutamos:
  `Scripts\activate`    WIN 
source venv/bin/activate LINUX

python -m pip install Pillow

5. Descargamos el repositorio de GitHub, con el siguiente comando (Validamos que la máquinatenga Git instalado):
  `git clone https://github.com/jturizo2/GranjaAPP`
6. Entramos a la carpeta del repositorio e instalamos las dependencias, con el siguiente comando:
  `pip install -r requirements.txt`
7. Realizamoslas migraciones necesarias a la base de datos. 
  `python manage.py makemigrations`               
  `python manage.py migrate`
8. En la carpeta base del proyecto, corremos el servidor de desarrollo:
	`python manage.py runserver`
	`python manage.py runserver 0.0.0.0:5000` .
sudo ufw allow 5000
 fuser -k -n tcp 3000

Run on differente port

9. Procedemosa utilizar la aplicación. Estará disponible en la URL:
  http://localhost:8000/
