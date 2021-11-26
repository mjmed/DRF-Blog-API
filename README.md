# Blog API

## *Django REST Framework de cero a experto*

_Backend_ **Blog API** creado con _Django REST Framework_. Este _backend_ permite el registro y _login_ de usuarios. 

Incluye:
+ **Django REST Framework**
+ Autenticación **JWT**

### Librerías y paquetes utilizados:
- [**Django REST framework**](https://www.django-rest-framework.org/#installation)
- [**drf-yasg**](https://drf-yasg.readthedocs.io/en/stable/): para generar la documentación de manera automatica.
- [**Simple JWT**](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/): autenticación con Json Web Token.
- [**Django Filter**](https://www.django-rest-framework.org/#installation)


### Versión: 1.0.0

### Notas:
Comando para activar el entorno virtual:
```
./envs/blog/Scripts/activate
```

Comando para instalar las dependencias del proyecto desde el fichero requirements.txt (con el entorno virtual activado):
```
pip install -r requirements.txt
```

Comando para crear o actualizar el fichero requirements.txt (con el entorno virtual activado):
```
pip freeze > requirements.txt
```

Comando para ejecutar el servidor en desarrollo:
```
python manage.py runserver
```