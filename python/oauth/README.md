# Directorio docker

En este directorio se encontrarán códigos relacionados a código que muestra como usar el protocolo de autenticación OAuth.

Para llevar a cabo esta prueba es necesario crear un contenedor como se indica en [este directorio](../../docker) sección Flask.

# Probando el contenedor con autenticación OAuth

Para llevar a cabo esta prueba se hace necesario que se creen credenciales en la plataforma de Google [http://console.developers.google.com/](http://console.developers.google.com/).
Visitar el link `Credentials` y crear credenciales para su aplicación.

Para más detalles relacionados a la creación de credenciales usted puede visitar este [enlace1](https://pythonspot.com/login-to-flask-app-with-google/) o este otro [enlace2](http://bitwiser.in/2015/09/09/add-google-login-in-flask.html). 
En este último enlace hay un poco más de detalles respecto a la creación de credenciales para aplicaciones web y está así mismo más actualizado.

Finalmente, en base al código de [enlace1](https://pythonspot.com/login-to-flask-app-with-google/) se creo el código [app-oauth.py](./app-oauth.py).
Debe cambiar los valores de las variables `GOOGLE_CLIENT_ID` y `GOOGLE_CLIENT_SECRET` por los valores que tiene en su [consola de desarrollador de Google](http://console.developers.google.com/).

```
docker run -p 5000:5000 --rm -v $(pwd):/shared josanabr/minflask:v2 /shared/app-oauth.py
```

