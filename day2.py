
#CNN = Convolutional  Neural network
# import necessary library
import numpy as np 
#numpy is  a library for numerical  operation in python
import tensorflow as tf
#tensorflow is the deep learning library used it to build and train the CNN
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
#load the MNIST dataset
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