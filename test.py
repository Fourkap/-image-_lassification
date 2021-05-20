from tensorflow import keras
import tensorflow as tf
import os
model = keras.models.load_model("save_at_25.h5")

image_size = (180, 180)
batch_size = 32

img = keras.preprocessing.image.load_img(
    "858743bb35_50169458_chien-min.jpg", target_size=image_size
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  

predictions = model.predict(img_array)
score = predictions[0]
print(
    "This image is %.2f percent cat and %.2f percent dog."
    % (100 * (1 - score), 100 * score)
)