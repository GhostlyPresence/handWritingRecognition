Handwriting recognition using convolutional neural network.
The network is trained using tensorflow on MNIST dataset.

MNIST is a dataset containing 60000 images of handwritten numbers.
Model is trained using 80% images as training set and 20% validation set.

Following is the architecture of the network:
Model: "sequential_15"

-----------------------------------------------------------------
Layer (type)                 Output Shape              Param #
=================================================================
conv2d_31 (Conv2D)           (None, 26, 26, 32)        320
-----------------------------------------------------------------
max_pooling2d_24 (MaxPooling (None, 13, 13, 32)        0
-----------------------------------------------------------------
conv2d_32 (Conv2D)           (None, 11, 11, 64)        18496
-----------------------------------------------------------------
max_pooling2d_25 (MaxPooling (None, 5, 5, 64)          0
-----------------------------------------------------------------
dropout_19 (Dropout)         (None, 5, 5, 64)          0
-----------------------------------------------------------------
flatten_14 (Flatten)         (None, 1600)              0
-----------------------------------------------------------------
dense_31 (Dense)             (None, 128)               204928
-----------------------------------------------------------------
dropout_20 (Dropout)         (None, 128)               0
-----------------------------------------------------------------
dense_32 (Dense)             (None, 10)                1290
=================================================================
Total params: 225,034
Trainable params: 225,034
Non-trainable params: 0

Using the above architecture an accuracy of around 98% was achived when tested on 10000 test images.
Using a deeper network or fine tuning a pre-trained architecture such as MobileNet , better accracy can be achieved.

The network was deployed on Flask web server.

The frontend is basic HTML CSS JS.



