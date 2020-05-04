# Data Project 4: FENIX APP 
## Departamento de Algoritmos de Imagen

Nuestro rol dentro del proyecto que gira en torno al Hackathon 4 y el desarrollo de la aplicación FENIX estaba encuadrado dentro del departamento de Imagen donde nos hemos encargado del desarrollo de los algoritmos de imagen que van a formar parte de la aplicación final. 

Nuestro principal cometido en el desarrollo de los algoritmos de imagen era basarnos en modelos de detección de objetos ya existentes, que han funcionado de manera efectiva para la detección de caras y detección de manos y fusionarlos para que puedan funcionar juntos y cumplir con nuestros dos casos de uso principales:
 
**1. Evitar que los usuari@s se toquen la cara** (emitir un aviso en forma de sonido/ contador en el momento que esta situación se de).
 
**2. Recordar a los usuario que se pongan la mascarilla y que se la pongan de forma correcta** (Emitir un aviso recordando al usuario que no lleva puesta la mascarilla / alertarle de que la lleva puesta de forma incorrecta, no cubriendo las zonas delicadas (nariz y boca) que la mascarilla está destinada a proteger.
 
Este repo contiene los diferentes modelos que hemos desarrollado para cumplir con los siguientes cometidos que nos habían sido encargados:

* Implementar un modelo que fuera capaz de **detectar caras**
 
* Implementar un modelo que fuera capaz de **detectar manos**
 
* Combinar ambos modelos para **identificar cuando una persona se toca la cara**
 
* Implementar / crear un modelo que fuera capaz de **identificar si una persona lleva o no una mascarilla puesta**

## Modelos Utilizados

Los siguientes modelos han sido implementados para cumplir la función de detección de objetos para nuestros diferentes casos de uso:

* Detección de caras : **HOG** (Histogram Oriented Gradients + **SVM** (Support Vector Machines)
* Detección de manos : **Yolov3**
* Detección de mascarillas : **Yolov3**


## Resultados

A continuación se puede comprobar los resultados de los diferentes detectores implementados al probarlo con imagenes propias.

### Detección de caras



### Detección de manos



### Ambos detectores combinados



### Detección de mascarillas
