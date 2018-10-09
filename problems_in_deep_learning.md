# Problems in Deep Learning 
## Primary Problem
## Computational Delay

When it comes to computation intensive tasks in computer science we can think of animation, video editing, game development, with the recent raise in deep learning it being the winner over all the other in computation hungry tasks. 

The basic process of deep learning involves taking similar kind of data and taking huge number of parameter and doing many number of computations to tune those parameters. In deep learning we have parameters around a hundreds of thousands which need to be tuned on 100’s of GB of data. 

Every code in deep learning involved crating a graph having parameters and passing data through the graph over and over again until the parameters are rightly tuned.

This data can be of all formats…
1. Text Data
2. Image Data
3. Audio Data
4. Video Data
5. Tabular Data

Text data and Tabular Data requires less computation power comparatively, when it comes to Image Audio and Video data they consist of row and columns of pixels which need to manipulated one after other. In order to breakdown a full HD image it would result in 1080 rows and 1980 columns 2138400 floating values per Image and video would have 2138400*(frames) of floating values in it. These values need to be passed through the graph with addition and multiplications in the graph and passing through activation function these would result in enormous number of simple addition and multiplication operations

So basically the problem could be boiled down to _**processor having gigantic number addition and multiplication operations in a queue**_.

The current way of solving these problems 

###  Using GPU’s

When it comes to parallel processing GPU is like an Elephant an CPU is like an ant. This difference comes due to number of cores the component has. A CPU would typically have 2 or 6 cores whereas GPU have thousands of cores. All the huge amount of addition and multiplication operations are handled by GPU by the technique of parallel processing most of the addition and multiplication operations are performed at the same time using the CUDA cores in the GPU which reduces the amount of time taken for.

### Using TPU’s

This one solution of created by google which is custom configured hardware for tensor computations. These graph computations would result in matrix multiplication which can be solved if there is custom hardware which only does matrix multiplication. This opportunity is exploited by google by making a hardware named TPU and putting it in their cloud systems.

Future possible solutions…
Deep Learning computations basically boils down to 
1. Matrix Multiplications
2. Data flow through graph
3. Parallel computations.
4. Reading and writing the data from disk
If any of these problems can be speed up it would result in less time for deep learning problems.

## Secondary Problem
## Lack of Data
Let’s say you want to detect faces then you would want face dataset. Let say you want to classify cars then you want to cars pictures of all the types of cars you want to classify.
In the world of deep learning everything depends on data you result are as good as the data you use to train the model. Creating a dataset had been an expensive and time consuming task since decades. 

Only since 2011 data flow have been increased due to advent of smartphone and more people using the internet creating the data, this result to big data. Then, in this world of big data where comes the problem of lack of data…?
* Out this created data most of the data would be privacy protected for research purpose we would require data with all copyrights. 
* Not every dataset is useful for your problem, there might just be not dataset useful for your well defined problem. 
* The data you want is subset of available dataset then you need to filter the existing dataset.
* The dataset might have similar data not the exact data you required.

Like the above problems there can be many more that will make data useless for deep learning use.

The art of collecting the data with proper permissions for research and commercial use is ‘creating a dataset’. There are many datasets for machine learning and deep learning online which can be used with different licenses. If your problem is very peculiar you might be having hard time finding the data related to it.

Find the data wouldn’t be enough to overcome this, then comes problems like
* Labeling the data (If it’s not a group activity it would take forever)
* Data might be biased (Which would result in model and predictions biased)
* Might be various formats need to be converted to one format.
* Resources to handle the data.
* Preprocessing of data like normalization, standardization, filling the missing values etc.
* Data transfer, Data streaming, Data formatting, Data Munging, Data wrangling etc. 

Like this many more problems exist in data acquiring phase and preprocessing phase. Thus, making the ‘Lack of data’ as a secondary problem in deep learning.

## Conclusion

There are many more problems exist in deep learning which are being tackle by frameworks and communities over the course of time. Let’s hope in we will come to a day when every data that being produced is analyzed and consumed by neural network for better world.