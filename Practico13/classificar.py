import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras
import matplotlib.pyplot as plt

''' El dataset contiene tres clases: elefantes, rinoserontes y bufalos
    y cada una de estas clases tiene alrededor de 200 imagenes de entranamiento
    y 50 de prueba  '''


train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.2,
                                   zoom_range=0.2)

test_datagen = ImageDataGenerator(rescale=1. / 255)

training_set = train_datagen.flow_from_directory('./dataset/train',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory('./dataset/test',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

model = tf.keras.models.Sequential([
    tf.keras.layers.experimental.preprocessing.Resizing(64, 64,
                                                        interpolation='bilinear'),
    tf.keras.layers.Conv2D(6, (6, 6), activation='relu',
                           input_shape=(64, 64, 3)),
    tf.keras.layers.Conv2D(12, (5, 5), strides=(2, 2), activation='relu'),
    tf.keras.layers.Conv2D(24, (4, 4), strides=(2, 2), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(rate=.25),
    tf.keras.layers.Dense(200, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

optimizer = tf.keras.optimizers.Adam(decay=.0001)

model.compile(optimizer=optimizer,
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_set, epochs=25)
model.evaluate(test_set)

b = test_set.next()
print(b[1][0:5])  # Imprimo las etiquetas verdaderas
model.predict(b[0][0:5])  # Calculo las probabilidades con el modelo

# ----------------------------------

img = keras.preprocessing.image.load_img(
    "./dataset/380.jpg", color_mode='rgb', target_size=None
)
img2 = keras.preprocessing.image.load_img(
    "./dataset/009.jpg", color_mode='rgb', target_size=None
)


def predic(img):
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)

    return predictions


predictions = predic(img)
predictions2 = predic(img2)

f = plt.figure()
f.add_subplot(1, 2, 1)
plt.title(str(predictions))
plt.suptitle('Imagenes separadas del dataset')
plt.imshow(img)

f.add_subplot(1, 2, 2)
plt.title(str(predictions2))
plt.imshow(img2)
plt.show(block=True)

score = predictions[0]
print("La primera imagen obtiene como presicion: " + str(score))
score2 = predictions2[0]
print("Y la segunda imagen: " + str(score2))
