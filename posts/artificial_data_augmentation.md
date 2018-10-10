# Artificial Data Augmentation

## Introduction

`I` : Match the persons with the food below <br/>
Persons <br/>

<img src ="/assets/images/artificial_data_augmentation_files/person1.jpg" height="258" width="196" >
<img src ="/assets/images/artificial_data_augmentation_files/person2.png" height="258" width="258" >
<br>

Burgers<br/>

![Image not found](/assets/images/artificial_data_augmentation_files/small_burger.jpg)
![Image not found](/assets/images/artificial_data_augmentation_files/big_burger.jpg)

`You`: The big burger for the sumo and small burger for the teenager. <br/>

`I`:  Why would you match that way and why not the other way…?<br/>

`You`: The sumo need to wrestle he would require more energy and big burger would provide him that, as per teenager his usual life style small burger would be enough

>             "Same is the case with deep neutral networks"

The bigger the deep neural network is the more its hungry for the data. If there is not enough data to train a neural network, it might result in bad predictions.

But what if, you have only limited data and want to train a neural network. The come the process of **artificial data augmentation**. It’s a process of synthetic data creation from the existing data by making little modifications to the existing data to create data which in the perspective of neural network is unique.

Artificial Data Augmentation techniques 
When it comes to “Artificial Data Augmentation”
There are so many techniques that could be explored. Some of the notable mentions are …

>Note: We are taking Image data into consideration and it can be extrapolated to videos too

## Affine Transformations
1.	Translation (X-direction, Y-direction, Z-direction).
2.	Scale (In, Out) alias Zoom.
3.	Sheer.
4.	Rotation.
## Linear Transformations
5.	Brightness.
6.	Contrast.
7.	Gaussian Noise.
8.	Reducing the resolution (Resizing an Image with different Interpolation metrics)
## Orientation Transformations
9.	Flip horizontal.
10.	Flip vertical.
## Image Filters 
11.	Blur (Average, Gaussian, Median).
12.	Elongation (Vertical and Horizontal) Like Stretched out Image.
13.	Morphological Transformations.
14.	Colors Inversions of Objects.
## Real Life Scenarios 
15.	Dirt on camera lenses (leading to random dark spots on Image).
16.	Multiple random dark spots on the Image (Distorted Image).
17.	Fog.
18.	Rain.
19.	Snow.
20.	Dust in air.
21.	Seasonal Change.
22.	Light Reflections (Leading to white spots in the Image).
23.	Shaking of camera alias Image stabilization (In a video case).
24.	Channel shift Intensity.

One thing to be taken into consideration is not all transformations would apply for all the scenarios, based on the problem environment different transformation would be applied for different scenarios.

# Conclusion 
Based on the data available and data required synthetic data can be created using the different data augmentation techniques. This is done to make neural network get used to real time scenarios and make predictions in much robust environments which makes a deep neural network more powerful and less predictions errors.

