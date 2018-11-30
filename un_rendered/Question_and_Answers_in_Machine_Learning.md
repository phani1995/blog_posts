

**Q. Is Gradient a vector or scalar..?**

Ans. The gradient is a vector operation which operates on a scalar function to produce a vector whose magnitude is the maximum rate of change of the function at the point of the gradient and which is pointed in the direction of that maximum rate of change. In rectangular coordinates the gradient of function f(x,y,z) is: 

$$
\nabla f =[i\frac{\partial}{\partial x}+j\frac{\partial}{\partial y}+\frac{\partial}{\partial z}]f
$$

If S is a surface of constant value for the function f(x,y,z) then the gradient on the surface defines a vector which is normal to the surface.

**Q. Difference between a gradient and directional derivative..?**

Gradient is multidimensional rate of change of given function and Directional derivative is the projection of that Gradient


**Q. Difference between a gradient and derivative..?**

derivative is in 2-D, for multi-dimensions its gradient (partial derivative with respective each direction). Derivative is a scalar whereas gradient is vector.


**Q.what is Jacobian  Matrix ..?**

**Q.what is Hessian Matrix ..?**

**Q.what is Newton–Raphson method ..?**

**Q.what is Difference between gradient descent and stochastic gradient descent ..?**
Gradient descent to take one step pass through all training samples.   
Stochastic gradient descent pass through single sample of training samples to take a step.  
mini batch gradient descent pass through small portion in powers of two (32,64,128) of training samples to take a step.

**Q.what is precession ..?**

Precession tries to answer the question, What proportion of positive identifications was actually correct..?    
The formula for precision
$$
Precision =\frac{TP}{TP+FP}
$$

where,   
TP - True Positive  
FP - False Positive

**Q.what is Recall ..?**
Recall tries to answer the question, What proportion of actual positives was identified correctly...?   
The formula for recall....  
$$
Precision =\frac{TP}{TP+FN}
$$

where,   
TP - True Positive  
FN - False Negative 

**Q.what is F1 score..?**

The traditional F-measure or balanced F-score (F1 score) is the harmonic mean of precision and recall. Its a statistical binary classification metric. Its value range between 0 and 1, where 1 being the best model and 0 being the worst.   
The formula for F1 score.... 
$$
 F1 = \Bigg(\frac{recall^{-1}+precision^{-1}}{2}\Bigg)^{-1}
$$
or 
$$
 F1 = 2  \frac{precision.recall}{precision+recall}
$$

**Q.what is Area under ROC Curve...?**

By taking True Positive Rate on y-axis   
True Positive Rate(TPR)   
TPR = \frac{TP}{TP + FN}

By takign False Positive Rate on x-axis   
False Positive Rate(FPR)   
FPR = \frac{FP}{FP+TN}

The two values are plotted at every threshold and ROC (receiver operating characteristic curve) is generated.   
![svg](/assets/images/Question_and_Answers_in_Machine_Learning_files/ROCCurve.svg)

The area under the ROC curve would determine how good the model is...   
![svg](/assets/images/Question_and_Answers_in_Machine_Learning_files/AUC.svg)

* AUC is scale-invariant. It measures how well predictions are ranked, rather than their absolute values.
* AUC is classification-threshold-invariant. It measures the quality of the model's predictions irrespective of what classification threshold is chosen.

if the AUC value is 0.5 its doing just as random predictor. AUC values should be 0.5 to  1 for a good model.

**Q.what is Prediction Bias...?**   
"average of predictions" should ≈ "average of observations"   
Prediction bias is a quantity that measures how far apart those two averages are. 

That is: 
$$
prediction bias = average of predictions - average of observations.
$$

