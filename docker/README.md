# Directorio docker

En este directorio se encontrarán definidos los `Dockerfile` que permitirán la creación de las imágenes que se usarán como microservicios.

* Flask

# Flask

Para crear un contenedor con Python y Flask se usará como base el contenedor de Docker creado a partir de este [Dockerfile](https://github.com/frol/docker-alpine-python2/blob/master/Dockerfile).

Para el caso de este proyecto el Dockerfile se llamará `Dockerfile.flaskv2`. La creación del contenedor se hará a través del comando:

```
docker build -f Dockerfile.flaskv2 -t <tutag> .
```

`<tutag>` lo define usted. 
En mi caso es `josanabr/minflask:v2`. 
El `v2` porque hace referencia a Python 2.

## Probando el contenedor

Una vez se tiene creado el contenedor, se puede ejecutar una prueba de la siguiente manera:

```
docker run -p 5000:5000 --rm -v $(pwd):/shared josanabr/minflask:v2 /shared/app.py
```

Se asume que en el sitio donde ejecute el contenedor, se encuentra disponible el archivo `app.py` provisto en este directorio.

## Probando el contenedor con autenticación OAuth

Para llevar a cabo esta prueba se hace necesario que se creen credenciales en la plataforma de google [http://console.developers.google.com/](http://console.developers.google.com/).
Visitar el link `Credentials` y crear credenciales para su aplicación.

Para más detalles relacionados a la creación de credenciales usted puede visitar este [enlace1](https://pythonspot.com/login-to-flask-app-with-google/) o este otro [enlace2](http://bitwiser.in/2015/09/09/add-google-login-in-flask.html). 
En este último enlace hay un poco más de detalles respecto y está más actualizado.

Finalmente, en base al código de [enlace1](https://pythonspot.com/login-to-flask-app-with-google/) se creo el código [app-oauth.py](./app-oauth.py).
Debe cambiar las variables `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET` por los valores que tiene en su [consola de desarrollador de Google](http://console.developers.google.com/).

```
docker run -p 5000:5000 --rm -v $(pwd):/shared josanabr/minflask:v2 /shared/app-oauth.py
```


