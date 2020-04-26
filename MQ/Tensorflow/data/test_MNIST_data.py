import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('./data/MNIST_data')

# MNIST数据探索
img = mnist.train.images
label = mnist.train.labels
img1 = img[550].reshape([28, 28])
plt.imshow(img1)
plt.show()
