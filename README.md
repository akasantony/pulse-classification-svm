pulse-classification-svm
========================
A simple classifier that takes in age and pulse rate as features and classifies the emotion using an [Support Vector Machine](https://en.wikipedia.org/wiki/Support_vector_machine) classifier. Training data is present under ```assets/training_data/datasets.txt```

Introduction
-------
The basic idea behind this application is to understand human emotions based on the pulse-rate and age. The classifier is trained using age and pulse-rate as features. The emotions are classified into four classes angry, happy, excited, sad and are labeled from 0-3. The classifier then takes in array containing pulse-rate and age as input for predicting the emotion.

The ```pulseextraction``` module is used for detecting the pulse-rate of a human by analysing video samples of the person's finger. Frames are extracted from the video sample and based on the intensity of the Red component of the pixel in each frame a graph is plotted.

Dependencies
--------
This code is written in Python. To use the code you'll need the following:

* Python 2.7
* A recent version of [NumPy](http://www.numpy.org/) and [SciPy](http://www.scipy.org/)
* [scikit-learn](http://scikit-learn.org/stable/index.html)
* [OpenCV-Python](http://opencv.org/)
* [Matplotlib](http://matplotlib.org/)

Getting Started
-------
1. Get a copy of the code onto your local repository :

  ```git clone https://github.com/akasantony/pulse-classification-svm.git```

2. Run ```python script.py``` to load the training dataset and class labels as a NumPy array.

3. Run the code:

  ```python main.py```
