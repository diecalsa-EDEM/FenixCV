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

* Detección de caras : Libreria **Dlib** mediante **HOG** (Histogram Oriented Gradients + **SVM** (Support Vector Machines)
* Detección de manos : **Yolov3**
* Detección de mascarillas : **Yolov3**

## Software & librerias utilizadas

* **LabelImg** : Software de etiquetado de Imagenes
* **Open CV** : Biblioteca de Visión Artificial
* **Tensor Flow** : Biblioteca de Machine Learning
* **Keras** : Biblioteca de Redes Neuronales
* **Dlib** : Biblioteca de algortimos de Machine Leearning
* **Darknet**: Biblioteca desarrollada para el entrenamiento, inferencia y evaluación de modelos YOLO


## Datasets

Durante el desarrollo del proyecto hemos utilizado una combinacion de datasets públicos y otros propios,generados para las necesidades especificas de nuestros casos de uso:

### Lista de Open Datasets

* **COCOS Dataset**: Dataset abierto que contiene más de 220k imágenes etiquetadas y 1.5 millón de clases de objetos diferentes.
* **Ego Hand Dataset**: Dataset creado por la Universidad de Indiana que contiene 15,083 manos etiquetadas y 48 videos diferentes de manos.
* **OID Dataset** : Dataset con 500 clases de objetos diferentes.
* **Medical Mask Dataset**: Dataset creado para una competición de Kaggle con 682 imagenes de gente portando mascarillas médicas.

### Datasets Propios

Para complementar el entrenamiento de los modelos desarrollados y entrenados con los datasets públicos ya mencionados, generamos con fotos propias de los miembros del equipo y con colaboración de los compañeros de EDEM otros datasets con fotos mas enfocadas a los casos de uso que quiere detectar nuestros algoritmos de imagenconn el fin de mejorar la precisión y rapidez de nuestros modelos:

* Fotos de personas tocandose la cara
* Fotos de personas con mascarillas
* Fotos de manos con perfiles y angulos menos comunes


## Resultados

A continuación se puede comprobar los resultados de los diferentes detectores implementados al probarlo con imagenes propias.

### Don't touch your face!

[![](https://github.com/diecalsa-EDEM/FenixCV/tree/facialDetection/src/DontTouchYourFace.gif)]


### Detección de caras

![image](https://drive.google.com/uc?export=view&id=1-JRvBSVsyIIiurkOeqT2v5yhYteRkByL)


### Detección de manos

![image](https://drive.google.com/uc?export=view&id=1vptxGpEuBaQKWeaYOiHYOIWhVv0-gpFI)


### Detección de mascarillas

![image](https://drive.google.com/uc?export=view&id=1B4PV7oHRkyi3Zx08M68p81R7-Ph9Nz5H)
