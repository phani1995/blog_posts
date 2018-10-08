# Cifar-10 with Linear classifier

>** how to make the templated out of linear classifier **

[weight lifting Image](https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjpl6LNsfbdAhXJtI8KHbXlC6cQjRx6BAgBEAU&url=https%3A%2F%2Fpxhere.com%2Fen%2Fphoto%2F641586&psig=AOvVaw2jKwki3p2ptZ7MSFUX5Dqe&ust=1539072392843218)

## The Maths

The eqation of a Linear classifier would be like
$$ 
\begin{equation}
        ax= b \\tag{2.1}
\end{equation}
$$
where y is the score of each class ,
W is the weight matrix
b is the bais

lets just say for the sake of simplification there are three classes
1. cat
2. dog
3. Lion
      
Then the y (which is scores of all the three classed would appear like) ... **3*1 matrix**
$$
\begin{bmatrix}
    y_{1}        \\
    y_{2}        \\
    y_{3}       
\end{bmatrix}
$$
where y1 stands for score of first class and y2 stands for score of second class and so on...

Lets just say for the sake of simplicity every pricute we have is of 2by2 resolution. The picture is only 2 pixels wide and 2 pixels height

So with each image we would end up with a numpy array of 2 by 2. The array would look like this ... **2*2 matrix**
$$
\begin{bmatrix}
    x_{11} &  x_{12}\\
    x_{21} &  x_{22}\\
\end{bmatrix}
$$

This is a linear classifier not a convolutional neural network(topic for another time) so the weight need to be fattened so the image would look like ... **4*1 matrix**
$$
\begin{bmatrix}
    x_{11} \\
    x_{12} \\
    x_{21} \\  
    x_{22} \\
\end{bmatrix}
$$
we have just made a single dimentiona 

Then we take the bais and weight based on the defined inputs and outputs. The weight matrix would look like ... **4*3 matrix**
$$
\begin{bmatrix}
    w_{11} &  w_{12} & w_{13} & w_{14}\\
    w_{21} &  w_{22} & w_{23} & w_{24}\\
    w_{31} &  w_{32} & w_{33} & w_{34}\\
\end{bmatrix}
$$

and bais would look like ... **3*1 matrix**
$$
\begin{bmatrix}
    b_{1} \\
    b_{2} \\
    b_{3} \\
\end{bmatrix}
$$

fitting all the four in equation
it would look like ...
$$
\begin{bmatrix}
    y_{1}        \\
    y_{2}        \\
    y_{3}       
\end{bmatrix}
= 
\begin{bmatrix}
    w_{11} &  w_{12} & w_{13} & w_{14}\\
    w_{21} &  w_{22} & w_{23} & w_{24}\\
    w_{31} &  w_{32} & w_{33} & w_{34}\\
\end{bmatrix}
* 
\begin{bmatrix}
    x_{11} \\
    x_{12} \\
    x_{21} \\  
    x_{22} \\
\end{bmatrix}
+ 
\begin{bmatrix}
    b_{1} \\
    b_{2} \\
    b_{3} \\
\end{bmatrix}
$$
But wait, the equation can be much more consised ...
$$
\begin{bmatrix}
    y_{1}        \\
    y_{2}        \\
    y_{3}       
\end{bmatrix}
= 
\begin{bmatrix}
    w_{11} &  w_{12} & w_{13} & w_{14} &  b_{1} \\
    w_{21} &  w_{22} & w_{23} & w_{24} &  b_{2} \\
    w_{31} &  w_{32} & w_{33} & w_{34} &  b_{3} \\
\end{bmatrix}
*
\begin{bmatrix}
    x_{11} \\
    x_{12} \\
    x_{21} \\  
    x_{22} \\
    1      \\
\end{bmatrix} 
$$
> Note the above equation and equation above the above equation mean the same its just better way of writing it and frameworks would process the equatins in the above 
$$
y_{1} = w_{11}*x_{11} + w_{12} *x_{12} + w_{13} * x_{21} + w_{14}* x_{22} + 1* b_{1}
$$

