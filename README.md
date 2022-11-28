# Gitleaks
Proyecto que busca leaks de credenciales en github a través de la libreria GitPython, usando expresiones regulares y devolviendo un fichero json con
todos los leaks encontrados. Se ha implementado una barra de progreso y se ha desplegado a traves de Docker.
## Docker
Para lanzar la imagen de docker habra que seguir los siguientes pasos:
Los archivos deben de ser extraidos en una carpeta en la que se trabajara desde la terminal. 
1. Crear la imagen: 
>>>docker build . -t 'nombre con el que quieras llamarlo'
- (El punto indica que se cogen todos los archivos del directorio en el que nos encontramos)
2. Una vez que tengamos la imagen creada tendremos que elegir un path absoluto del directorio al que queramos que se linkee el contenedor de docker.
para que podamos ver la salida. Esto se hara de la siguiente forma. 
absolute_path = ['path del directorio de salida host']. En el caso en el que no exista el directorio que queremos linkear lo crea.
>>>docker run -v absolute_path:/out 'nombre con el que hayas llamado a la imagen'
Es importante mantener la estructura del anterior comando. En particular el path tras ':' no debera ser alterado ya que es el directorio interno del contenedor.
