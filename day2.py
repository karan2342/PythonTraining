# CNN = Convolutional Neural Network

# Import necessary libraries
import numpy as np
# numpy is a library for numerical operations in Python

import tensorflow as tf
# tensorflow is the deep learning library used to build and train the CNN

from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical

import matplotlib.pyplot as plt
# matplotlib is used to display images and compare predictions


# Load the MNIST dataset
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()


# Preprocessing: Normalize pixel values between 0 and 1
train_images = train_images / 255.0
test_images = test_images / 255.0


# Reshape images to (28, 28, 1) because MNIST images are grayscale
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

# Convert labels to one-hot encoded format
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Build the model
model = models.Sequential()

# First convolutional layer
model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)))
model.add(layers.MaxPooling2D((2,2)))

# Second convolutional layer
model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))


# Third convolutional layer
model.add(layers.Conv2D(64, (3,3), activation='relu'))

# Flatten the 3D output into 1D and add a dense layer
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))


# Output layer with 10 neurons (0-9 digits)
model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(
    train_images,
    train_labels,
    epochs=10,
    batch_size=64,
    validation_data=(test_images, test_labels)
)

# Evaluate the model on test data
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc * 100:.2f}%")

# Make predictions on test images
predictions = model.predict(test_images)
print(f"Prediction for first test image: {np.argmax(predictions[3])}")

# Display the first test image
plt.imshow(test_images[3].reshape(28,28), cmap='gray')
plt.title(f"Prediction Label: {predictions[3].argmax()}")
plt.show()