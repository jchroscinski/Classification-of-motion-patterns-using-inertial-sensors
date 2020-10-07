# Introduction

The project includes the software part of my master's thesis, the topic of which is *classification of motion patterns using inertial sensors*.

The research consisted in designing and creating a device equipped with inertial sensors, in this case an accelerometer and a gyroscope. Then, the signals during the performance of six selected physical exercises were recorded. Later, proposing methods that will allow to test the accuracy of classification using neural networks. For this purpose, the method of resampling the signal to a constant data size and several selected methods of extracting signal features were used. Finally, the databases created in this way were implemented into neural networks using the *Keras* package.

## Database

The database was registered with the use of a designed and then manufactured device, the main elements of which were an acclerometer and a gyroscope with a frequency of 50 [Hz]. The device was placed on the left arm and calibrated before each registration. Raw signals were recorded for one hundred repetitions of each class, for a total of six hundred repetitions.

The recorded physical exercises include:
* burpees
* crunches
* jumping jacks
* push ups
* squats
* v ups

## extend

Due to the different time taken to perform even the same exercises, a program was written that allowed to equate the number of samples to a constant value. In this case, the *trapezoidal sampling method* was used.

[Trapezoidal_rule - wiki](https://en.wikipedia.org/wiki/Trapezoidal_rule)

## feature

In order to conduct further studies, it was decided to use several methods of extracting signal features used in *Human Activity Recognition* problems. The program allows you to extract selected features depending on the function called.

Selected methods of feature extraction:
* deviation,
* mean,
* mean deviation,
* root mean square,
* variance,

## architectures_of_neural_networks

Finally, the structure of neural networks based on the *Keras* library was designed.
Mainly *Dense* layers and the *relu* activation function were used.
Several configurations of the number of network layers and a different proportion of training and testing sets were tested.
The recognition accuracy obtained is in the range of 95 - 100%.