# API REST
 un servicio que sea capaz de reconocer el palíndromo más largo dentro de una cadena de texto


API REST
servicios de integración
pruebas unitarias y demás
componentes
artefactos de software


Pre-requisitos 📋]
Puedes ver los requisitos de que se usan para desarrollar este proyecto

### instalar
para instalar la aplicacion es necesario correr los siguientes pasos

---
# Construido con 🛠️
se usa las siguientes tecnologias.

marshmallow
validate, serialize, and deserialize data.
---
### structure
```
    __init__.py
    app.py          # this file contains your app and routes
    resources/
        __init__.py
        foo.py      # contains logic for /Foo
        bar.py      # contains logic for /Bar
    common/
        __init__.py
        util.py     # just some common infrastructure
```
# end-points
para ver que endpoints tiens

![](https://i.imgur.com/cN5lRqY.png)



# testing
for running testing in the file use
```
python -m  src.test.test_largest_palindrome
```
