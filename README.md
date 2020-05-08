# Data Project 4: FENIX APP 

## Tabla de contenido

1. [Departamento de Algoritmos de Imagen](#departamento)
2. [Modelos Utilizados](#modelos)
3. [Software & librerias utilizadas](#software)
4. [Datasets](#datasets)
    1. [Lista de Open Datasets](#opendata)
    2. [Datasets Propios](#customdata)
5. [Resultados](#resultados)


## Departamento de Algoritmos de Imagen <a name="departamento"></a>

Nuestro rol dentro del proyecto que gira en torno al Hackathon 4 y el desarrollo de la aplicación FENIX estaba encuadrado dentro del departamento de Imagen donde nos hemos encargado del desarrollo de los algoritmos de imagen que van a formar parte de la aplicación final. 

Nuestro principal cometido en el desarrollo de los algoritmos de imagen era implementar arquitecturas basadas en redes neuronales convolucionales para la detección de objetos existentes y pre-entrenadas. De esta manera, empleando transfer learning, hemos sido capaces de entrenar un detector de manos personalizado. Una vez entrenado el modelo, el último paso fue implementar tanto el modelo de detección de manos como el de caras en la misma aplicación, para cumplir con nuestros dos casos de uso principales:

**1. Evitar que los usuari@s se toquen la cara** (emitir un aviso en forma de sonido/ contador en el momento que esta situación se de).
 
**2. Recordar a los usuario que se pongan la mascarilla y que se la pongan de forma correcta** (Emitir un aviso recordando al usuario que no lleva puesta la mascarilla / alertarle de que la lleva puesta de forma incorrecta, no cubriendo las zonas delicadas (nariz y boca) que la mascarilla está destinada a proteger.
 
Este repo contiene los diferentes modelos que hemos desarrollado para cumplir con los siguientes cometidos que nos habían sido encargados:

* Implementar un modelo que fuera capaz de **detectar caras**
 
* Implementar un modelo que fuera capaz de **detectar manos**
 
* Combinar ambos modelos para **identificar cuando una persona se toca la cara**
 
* Implementar / crear un modelo que fuera capaz de **identificar si una persona lleva o no una mascarilla puesta**

## Modelos Utilizados <a name="modelos"></a>

Los siguientes modelos han sido implementados para cumplir la función de detección de objetos para nuestros diferentes casos de uso:

* Detección de caras : 

    - Libreria **Dlib** mediante **HOG** (Histogram Oriented Gradients + **SVM** (Support Vector Machines)


![image](https://github.com/diecalsa-EDEM/FenixCV/blob/master/src/face_detector.jpg)

* Detección de manos : 

   - **Yolov3** ([yolov3_custom.cfg](https://drive.google.com/file/d/1-a38MrTHHTl9yyyZEwBdl4la8PEYFsXG/view?usp=sharing),  [yolov3_custom.weights](https://drive.google.com/open?id=1pg6S0rmhrcFV01EED9tgHnPo8yuNdxQ4), [yolov3 notebook](https://github.com/diecalsa-EDEM/FenixCV/blob/facialDetection/1.Training/Train_YOLOv3.ipynb))
     
   ![image](https://github.com/diecalsa-EDEM/FenixCV/blob/master/src/mano.jpeg)

   - **RetinaNet** ([RetinaNet_notebook](https://github.com/diecalsa-EDEM/FenixCV/blob/facialDetection/1.Training/Train_Retinanet_Salim.ipynb))
    
  ![image](https://github.com/diecalsa-EDEM/FenixCV/blob/master/src/hand-salim.jpeg)

* Detección de mascarillas : 

    - **Yolov3** ([yolov3_custom.cfg](https://drive.google.com/open?id=1CK-jXpu0Op8wOYJchklCD4I2YuLT91iG), [yolov3_custom.weights](https://drive.google.com/open?id=1i7vTsoPTx3UUIefgmco5MRHDgg6Nq9hI), [yolov3_notebook](https://drive.google.com/open?id=1nUwsYnNTgkRei3AhK1AVCWDSHiQOBsdP))

![gif](https://github.com/diecalsa-EDEM/FenixCV/blob/facialDetection/src/MaskDetection.gif)


* Don't touch your face : 

![gif](https://github.com/diecalsa-EDEM/FenixCV/blob/facialDetection/src/DontTouchYourFace.gif)





## Software & librerias utilizadas <a name="software"></a>

* [LabelImg](https://github.com/tzutalin/labelImg) : Software de etiquetado de Imagenes [[link]]
* [OpenCV](https://github.com/opencv/opencv) : Biblioteca de Visión Artificial
* **Tensor Flow** : Biblioteca de Machine Learning
* **Keras** : Biblioteca de Redes Neuronales
* **Dlib** : Biblioteca de algortimos de Machine Leearning
* [Darknet](https://github.com/AlexeyAB/darknet): Biblioteca desarrollada para el entrenamiento, inferencia y evaluación de modelos YOLO 

## Datasets <a name="datasets"></a>

Durante el desarrollo del proyecto hemos utilizado una combinacion de datasets públicos y otros propios,generados para las necesidades especificas de nuestros casos de uso:

### Lista de Open Datasets <a name="opendata"></a>

* **COCO Dataset**: Dataset abierto que contiene más de 220k imágenes etiquetadas y 1.5 millón de clases de objetos diferentes.
* **Ego Hand Dataset**: Dataset creado por la Universidad de Indiana que contiene 15,083 manos etiquetadas y 48 videos diferentes de manos.
* **OID Dataset** : Dataset con 500 clases de objetos diferentes.
* **Medical Mask Dataset**: Dataset creado para una competición de Kaggle con 682 imagenes de gente portando mascarillas médicas.

### Datasets Propios <a name="customdata"></a>

Para complementar el entrenamiento de los modelos desarrollados y entrenados con los datasets públicos ya mencionados, generamos con fotos propias de los miembros del equipo y con colaboración de los compañeros de EDEM otros datasets con fotos mas enfocadas a los casos de uso que quiere detectar nuestros algoritmos de imagenconn el fin de mejorar la precisión y rapidez de nuestros modelos:

* Fotos de personas tocándose la cara
* Fotos de personas con mascarillas
* Fotos de manos con perfiles y angulos menos comunes


## Resultados <a name="resultados"></a>

### Accuracy 

| First Header  |    DATASET    |       mAP     |       FPS     | 
| ------------- | ------------- | ------------- | ------------- |
| RetinaNet     |    CUSTOM     |      64%      |      0.25     |
| YOLOv3        |    CUSTOM     |      63%      |      5.00     |
| Tiny YOLO     |    CUSTOM     |      33%      |      15.00    |

*NOTA*: El dataset de validación está compuesto por 200 imágenes etiquetadas por el equipo de trabajo.

## Authors
- Alberto Bort
- Diego Calvete
- Luis Araujo
- Miguel Ángel Aguilar
- Salim Chikh


![image](https://github.com/diecalsa-EDEM/FenixCV/blob/master/src/fd6815fb-e35b-44ff-ae8e-2e2cbaf2d396.jpeg)
