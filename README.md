<p align="center">
  <a href="https://docs.djangoproject.com/en/4.1/" target="blank"><img src="https://velog.velcdn.com/images/tiger/post/23a71530-d387-4af6-abe9-720d1fe360b6/image.png" width="250" alt="Nest Logo" /></a>
</p>
<h1 align="center">  Registro Usuarios </h1>
<p align="left">
   <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
  <img src="https://img.shields.io/badge/PYTHON-%20v3.9.13-green">
  <img src="https://img.shields.io/badge/Django-%20v4.1.5-green">
  <img src="https://img.shields.io/badge/DjangoRestFramework-%20v3.14.0-green">
  <img src="https://img.shields.io/badge/MySql-%20v8.0.32-blue">
  <img src="https://img.shields.io/badge/Docker-%20v20.10.20-blue">
</p>

# Descripcion del proyecto
El sistema de registro, como aplicacion back-end  expondra diferentes servicios en las cuales 
permitiran la manipulacion de los usuarios, siendo asi capas de realizar insert, update y poseer la faculta 
de consultar a la base de datos.


## :hammer:Funcionalidades del proyecto
- `Funcionalidad 1`: Funcionalidad para listar los usuarios.
- `Funcionalidad 2`: Funcionalidad para actualizar los usuarios.
- `Funcionalidad 3`: Funcionalidad para crear un nuevo usuario.
- `Funcionalidad 4`: Funcionalidad para escoger nacionalidad.


## ✔️:Tecnologias utilizadas
- `Python`
- `Django`
- `Django Rest Framework`
- `mysql-connector-python`
- `Docker`
- `MySql`

# Ejecutar en desarrollo
## 1. Clonar el repositorio

```
git clone https://github.com/criveral2/RiveraChristian-RegistroDeUsuarios-BackEnd.git
```
<br>

Configuracion Base de datos en el archivo **.env**

```
DB_NAME=registrosDB
DB_USER=cerocodigo
DB_PASSWORD=Cer0Cod1go
DB_HOST=localhost
DB_PORT=3306
```
<br>
Para poder probar la aplicacion e utilizado un contenedor de Docker en la cual 
estara montada nuestra base de datos MySql y esta nos permitira conectar
con la aplicacion de registros.

<br>

## 2. Tener Docker instalado
## 3. Levantar la base de datos

<br>

Para levantar nuestra base de datos abriremos nuestra terminal (**cmd**)
y nos posicionaremos en la rais de nuestro proyecto verificando que nuestro archivo
**docker-compose.yml** se encuentre en el directorio y posteriormente ejecutaremos:

<br>

Para levantar el servicio
```
docker-compose up
```
Para revisar si nuestro servicio esta correctamente levantado
```
docker ps -a
```
## 4. Compilar el proyecto

<br>

Dentro de nuestro proyecto clonado, posicionarce dentro del proyecto:
**\RiveraChristian-RegistroDeUsuarios-BackEnd-master**
verificaremos que se encuentren los archivos **seed.json, requirements.txt, .env**
posterior mente abriremos nuestro terminal (cmd) en esa ruta y ejecutaremos:
<br>

Para instalar nuestras dependencias
```
pip install -r requirements.txt
```

Para construir nuestro esquema de base de datos
```
python manage.py makemigrations
```

Para migrar el esquema a la base de datos
```
python manage.py migrate
```

Para cargar la semilla que contiene nuestras nacionalidades dentro de la base de datos
```
python manage.py loaddata seed.json
```

Y finalmente para ejecutar la aplicacion 
```
py manage.py runserver
```
# Servicios api rest
- `Funcionalidad 1`: Funcionalidad para listar los usuarios.
  </br>
  
   URL:
   ```
   http://localhost:8000/api/users/
   ```
  
- `Funcionalidad 2`: Funcionalidad para actualizar los usuarios.
  </br>
  
   URL:
   ```
   http://localhost:8000/api/users/0163952897
   ```
   JSON:
   ```
   {
    "id": "0163952897",
    "name": "Pablo Malla",
    "birth_date": "1997-03-28",
    "country": 2
   }
   ```
- `Funcionalidad 3`: Funcionalidad para crear un nuevo usuario.
  </br>
  
   URL:
   ```
   http://localhost:8000/api/users/nuevo
   ```
   JSON:
   ```
  {
    "id": "0163952897",
    "name": "Pablo Malla",
    "birth_date": "1997-11-05",
    "country": 1
  }
   ```
- `Funcionalidad 4`: Funcionalidad para escoger nacionalidad.
  </br>
  
   URL:
   ```
   http://localhost:8000/api/users/countries/
   ```

