

## Data Preprocessing

Normalization and Standardization

It only makes sense to apply this pre processing if you have a reason to believe that different input features have different scales (or units), but they should be of 

**Covariance matrix**

**Principal Component analysis**

**Whitening**

**Common pitfall** computing the mean and subtracting it from every image across the entire dataset and then splitting the data into train/val/test splits would be a mistake.
> The mean must only be computed only over the training data and then subtracted equally from all splits (train/test/val)

**All Zero Initialization** : there is no source of \ 
asymmetry between neurons if their weights are initialized to be the same.


**L2 regularization** adding this tem to weights (-neg)1/2*lamba*(wight)*2

**L1 regularization** lamba*|weight|

**Dropout** each training case in a mini-batch,\
we sample a thinned network by dropping out units.\ Forward \ and backpropagation for that training case are done only on this thinned network
