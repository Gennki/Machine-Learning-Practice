import tensorflow as tf
from mnist import input_data
import matplotlib.pyplot as plt
import numpy as np

mnist = input_data.read_data_sets("C:/Users/Flyn/Desktop/MachineLearning/tensorflow/mnist")

print(mnist.train.images.shape)

