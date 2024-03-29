# -*- coding: utf-8 -*-
"""ANN_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15YoQ9TaU6pqBfI3vBlAQAoAUaNCrzWNj
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# We first verify the correct version of TF installed
# !pip install -q tensorflow-gpu==2.1.0

try:
  # %tensorflow_version only exists in Colab.
#   %tensorflow_version 2.x
except Exception:
  pass

import tensorflow as tf
print(tf.__version__)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import pandas as pd
import os
from mpl_toolkits.mplot3d import Axes3D
import os
import h5py
!pip install -q pyyaml

# Then, we create an artificial dataset
N = 1000
X = np.random.random((N, 2)) * 6 - 3 # Uniformly distributed between (-3, 3)
y = np.cos(2 * X[:,0]) + np.cos(3 * X[:,1])

"""This implements the function:

$$ y = \cos(2x_1) + cos(3x_2) $$
"""

# Plot the figure

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], y)

# After this, we start to build the model
# No activation function needed at end.
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, input_shape = (2,), activation= 'relu'),
    tf.keras.layers.Dense(1)
])

# Now we comepile the model
# Next, we compile the model, with default settings
optimizer = tf.keras.optimizers.Adam(1e-2)
model.compile(
    optimizer= optimizer,
    loss = 'mse',
)

# We print out a summery of our model
model.summary()

if not os.path.exists('./drive/MyDrive/AIwithTensorflow2/Feedforward Artificial Neural Networks/models'):   
    os.mkdir('./drive/MyDrive/AIwithTensorflow2/Feedforward Artificial Neural Networks/models')

tf.keras.utils.plot_model(model, to_file = './drive/MyDrive/AIwithTensorflow2/Feedforward Artificial Neural Networks/models/ANN_Regression.png')

# We create a ModelCheckpoint function for keeping track of the accuracy

if not os.path.exists('./drive/MyDrive/AIwithTensorflow2/Feedforward Artificial Neural Networks/models'):   
    os.mkdir('./drive/MyDrive/AIwithTensorflow2/Feedforward Artificial Neural Networks/models')

checkpoint_path = "./drive/MyDrive/AIwithTensorflow2/Feedforward Artificial Neural Networks/models/ANN_Regression.h5"
checkpoint_dir = os.path.dirname(checkpoint_path)

ModelCheckpoint = [tf.keras.callbacks.ModelCheckpoint(
    # filepath = 'content/drive/My Drive/Tensorflow 2.0 Course/Feedforward Artificial Neural Networks/models/MNIST.cpkt',
    filepath = checkpoint_path,
    monitor='val_loss',
    mode = 'min',
    save_best_only = True,
)]

r = model.fit(X, y, epochs= 100, callbacks= ModelCheckpoint)

# Plot the loss for checking convergence
plt.plot(r.history['loss'], label='loss')

# Plot the prediction surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], y)

# surface plot
line = np.linspace(-3, 3, 50) # 50 evenlyspaced points
xx, yy = np.meshgrid(line, line) # Create a meshgrid by doing a cross product
Xgrid = np.vstack((xx.flatten(), yy.flatten())).T # Need to flatted to then convert into the desired format
Yhat = model.predict(Xgrid).flatten()
ax.plot_trisurf(Xgrid[:,0], Xgrid[:,1], Yhat, linewidth=0.2, antialiased=True)
plt.show()

# Can it extrapolate?
# Plot the prediction surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], y)

# surface plot
line = np.linspace(-5, 5, 50)
xx, yy = np.meshgrid(line, line)
Xgrid = np.vstack((xx.flatten(), yy.flatten())).T
Yhat = model.predict(Xgrid).flatten()
ax.plot_trisurf(Xgrid[:,0], Xgrid[:,1], Yhat, linewidth=0.2, antialiased=True)
plt.show()

