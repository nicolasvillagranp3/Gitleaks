# Gitleaks.
Proyecto que busca leaks de credenciales en github a través de la libreria GitPython, usando expresiones regulares y devolviendo un fichero json con
todos los leaks encontrados. Se ha implementado una barra de progreso y se ha desplegado a traves de Docker.
- Para lanzar el programa sera necesario crear una carpeta llamada 'out' dentro del directorio de trabajao.
## Compressed Skale.
Para el correcto funcionamiento del programa sera necesario descomprimir la carpeta  compressed_skale en el mismo directorio de trabajo que el resto de archivos.
## Requirements.
Para poder correr el programa hay que instalar los paquetes necesarios con sus correspondientes versiones. Se ejecutara el siguiente codigo en terminal:
>pip install -r requirements.txt
## Docker.
Para lanzar la imagen de docker habrá que seguir los siguientes pasos:
1. Crear la imagen: 
- El punto indica que se cogen todos los archivos del directorio en el que nos encontramos. Podemos llamar a la imagen como queramos, teniendo en cuenta que al ejecutarla tendremos que usar ese nombre.
>docker build . -t 'nombre con el que quieras llamarlo'
2. Una vez que tengamos la imagen creada tendremos que elegir un path absoluto del directorio al que queramos que se linkee el contenedor de docker
para que podamos ver la salida del programa.
- absolute_path = ['path del directorio de salida host']. En el caso en el que no exista el directorio que queremos linkear lo crea.
- Es importante mantener la estructura del siguiente comando. En particular el path tras ':' no debera ser alterado ya que es el directorio interno del contenedor.
>docker run -v absolute_path:/out 'nombre con el que hayas llamado a la imagen'.
