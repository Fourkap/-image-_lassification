_Ce projet est réalisée dans le cadre de mon master 1 à l'école ITIC Paris_
# Classification d'image
Ce projet à pour but de faire de la classification d'images à partir d'images au format JPEG.

Ce projet est basé sur Keras. 

Keras est une API de Deep Learning écrite en Python, fonctionnant avec la plateforme d'apprentissage automatique TensorFlow. Elle a été développée dans le but de permettre une expérimentation rapide. La capacité de passer de l'idée au résultat aussi rapidement que possible est essentielle pour mener de bonnes recherches.
<hr>
[Le Dataset utilisé pour entrainer le modèle peut se télécharger sur le liens suivant:](https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip)

Tout les fichier .h5 sont les models entrainer, leur numeros correspond à chaque époque dans ce contexte plus il est élever plus le models est précis.
<hr>
Voici un exemple d'augmentation de la data. Cela correspond à ce code suivant:

       data_augmentation = keras.Sequential(
       [
           layers.experimental.preprocessing.RandomFlip("horizontal"),
           layers.experimental.preprocessing.RandomRotation(0.1),
      ]
     )
Se référer à l'image data-augmentation.jpg dans le repo.
<hr>
Le model est construit autour d'une petite version simple d'Xception network.
Xception est un model deep learning avec des convolutions séparables en profondeur. 
voir ce lien: https://arxiv.org/abs/1610.02357
<hr>

## Tester le model
Le fichier test.py permet de pré-process une image (peut importe la source) et de faire appel au model enregistrer au format .h5. 
Une fois l'image processer et analyser elle retournera en pourcentage si cet image est analyser en tant que chien ou chat.