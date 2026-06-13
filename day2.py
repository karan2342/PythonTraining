
#CNN = Convolutional  Neural network
# import necessary library
import numpy as np 
#numpy is  a library for numerical  operation in python
import tensorflow as tf
#tensorflow is the deep learning library used it to build and train the CNN
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
#load the MNIST dataset
import matplotlib.pyplot as plt
#display an image so you can compare the model prediction with the actual digit


(train_image, train_labels), (test_images, test_labels) =datasets.mnist.load_data()


#preprocessing : Normalization the pixel value to between 0 and 1
train_images = train_images/255.0
test_images = test_images/255.0
#Reshape the image to ( 28 , 28, 1) as they are grayscale
train_images = train_images.reshape((train_images.shape[0], 28 , 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

#convert the labels to one-hot encoded format
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#BUild the model
model = models.sequential()

#First convolutional layer
model.add(layers.Conv2D(32, (3,3), activation = 'relu', input_shape=(28,28,1)))
model.add(layers.MaxPooling2D((2,2)))

#Second convolutional layer
model.add(layers.Conv2d(64 , (3,3), activation = 'relu' ))
model.add(layers.MaxPooling2d((2,2)))

#Third convolutional layer
model.add(layers.Conv2d(64, (3,3), activation = 'relu'))

#Flatten the 3d output to 1d and add a dense layer
model.add(layers.Flatten())
model.add(layers.Dense(64,activation='relu'))

#output layer with 10 neurons (for 10 digit classes)
model.add(layers.Dense(10, activation='softmax'))

#compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train the model
model.fit(
    train_images,
    train_labels,
    epochs=5,
    batch_size=64,
    validation_data=(test_images, test_labels)
)

#Evaluate the model on test data
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy : {test_acc * 100:.2f}%")

#Make Predictions on test images
predictions = model.predict(test_images)
print(f"Predictions for first train image: {np.argmax(predictions[0])}")

plt.imshow(test_images[0].reshape(28,28), cmap= 'gray')
plt.title(f"Prediction Label:  {predictions[0].argmax()}")
plt.show()