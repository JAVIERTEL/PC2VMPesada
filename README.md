# 1. Despliegue de la aplicación en máquina virtual pesada 

 1.1. Lo primero que hemos hecho es crear una máquina virtual en Google Cloud, habilitando el uso de http y https y usando un sistema operativo Ubuntu que nos permitiese ejecutar el script de Python y no nos generase problemas de dependencias. A continuación, hemos creado una regla de Firewall habilitando el puerto 9080. 

1.2 Hemos desarrollado el script de Python con las especificaciones requeridas lo hemos importado a la máquina virtual (clonando este repositorio):
```
git clone https://github.com/JAVIERTEL/PC2VMPesada.git
```
```
cd PC2VMPesada
```
y  ejecutado con : 
```
python3 ./GoogleCloud.py 
```
1.3 Hemos accedido a él mediante http://<ip_publica>:9080/productpage  

 

 

 
