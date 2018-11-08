
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>

\usepackage{amsmath}

# Notable Points

* the performance of these machine learning algorithms depends heavily on the representation of the data of the data given.

* Representation Learning 

* when designing features or algorithms for learning features, our goal is usually to separate the factors of variation that explain the observed data. for example when analyzing an image of a car, the factors of variation include the position of the car, its color, the angle and brightness of the sun.


## MuCulloch-Pitts Model of Neuron

* This model is also called linear thershold gate

 $$
Sum = \sum_{i=1}^{N} I_i W_i
 $$

 $$
 y = f(Sum)
 $$

 where :
 $ I_1,I_2,I_3,I_4,...,I_N$ are inputs
 
 $y = output$

![Image not found](/assets/images/history_of_deep_learning_files/Linear_Threshold_function.jpg)

*Linear Threshold Function*

![Image not found](/assets/images/history_of_deep_learning_files/McCulloch-Pitts_Model_of_Neuron.jpg)

*McCulloch-Pitts_Model_of_Neuron*



* This linear model could recognize two diﬀerent categories ofinputs by testing whether $f(x, w) $ is positive or negative


# Perceptron

# Adaptive Linear Neuron (ADALINE)
* The difference between ADALINE and MuCulloch-Pitts Model is Learning phase wights are adjusted according to the weighted sum inputs

The structure of ADALINE

![Image not found](/assets/images/history_of_deep_learning_files/ADALINE.jpg)

*ADALINE*

Equation 
$$
  y = \sum_{j=1}^{n} x_j*w_j + \theta
$$

where,
* x is the input vector
* w is the weight vector
* n is the number of inputs
* $ \theta  some constant$
* y is the output of the model

The weights are updated as 

$$
w \leftarrow w + \eta(o-y)x 
$$
The above update rule is stochastic gradient decent

The Error function

$$
E = (o - y)^2
$$


where,
* \eta  is the learning rate (some positive constant)
* y is the output of the model
* o is the target (desired) output

# MADALINE (many ADALINE)
* similar to ADALINE with three layers ( input ,hidden,output)
* its activation function is sign function.

<br>
<br>


ADALINE and MuCulloch-Pitts Model were linear models. Linear models were not able to compute XOR function. This was a significant limitation.


# Multilayer perceptorn



# Backpropagation

Backpropagation was an efficient method of computing gradients in directed graph of computations, such as neural network.


David Rumelhart, +Geoff Hinton et al and Yann LeCun, (independently) figured that if you had smooth (sigmoidal) outputs, you could use the chain rule and train multi-layer networks




