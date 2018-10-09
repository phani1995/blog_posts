
The goal of optimization is to find optimal w that minimizes loss


**Convex Optimization** : problem of minimizing convex functions over convex sets.

> Our strategy will be to start with weights and iteratively refine it over time to get lower loss.

# Computing the Gradient
 * **Numerical Gradient** : slow, approximate and easy
 * **analytic Gradient** :  fast, exact and more error-prone ( In case of implementation for gradient decent )

 **gradient check** : to calculate analytic gradient to compare with numerical gradient to check its correctness of your implementation. 

 **mini batch gradient descent** : the gradient from a mini-batch is a good approximate of the gradient of the full objective.Therefore, much faster convergence can be achieved in practice by evaluating  the mini-batch gradients to perform more frequent parameter updates.

 > Note : we use powers of 2  in practice because many vectorized operations implementations work faster when their inputs are sized in powers of 2.
 