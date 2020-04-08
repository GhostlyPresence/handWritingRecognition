Handwriting recognition using convolutional neural network.
The network is trained using tensorflow on MNIST dataset.

MNIST is a dataset containing 60000 images of handwritten numbers.
Model is trained using 80% images as training set and 20% validation set.

Following is the architecture of the network:

         layers.Conv2D(32,input_shape=input_shape,kernel_size=(3,3),activation='relu')
         layers.MaxPool2D(pool_size=(2,2)),
         layers.Conv2D(64,kernel_size=(3,3),activation='relu'),
         layers.MaxPool2D(pool_size=(2,2)),
         layers.Dropout(0.25),
         layers.Flatten(),
         layers.Dense(128,activation='relu'),
         layers.Dense(64,activation='relu'),
         layers.Dropout(0.5),
         layers.Dense(num_category,activation='softmax')


Using the above architecture an accuracy of around 98% was achived when tested on 10000 test images.
Using a deeper network or fine tuning a pre-trained architecture such as MobileNet , better accracy can be achieved.

The network was deployed on Flask web server.

The frontend is basic HTML CSS JS.



