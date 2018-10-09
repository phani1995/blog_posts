# Backpropagation
which is a way of computing gradients of expressions through recursive application of chain rule.


All the variables are cached during forward pass, these values are used while computing gradients during backward pass. 
We can compute these values again but its better to cache.

Gates functions during backward pass
1. add gate
2. max gate
3. multiply gate


**add gate** : takes the gradient on its output and distributes it equally to  its input, regardless of what their values were during the forward pass.

**max gate** : distributes the gradient (unchanged) to exactly one of its input (the input which had highest value during forward pass)

**multiply gate** : local gradients are input values (except switched) and this is multiplied by gradient on its output during chain rule.