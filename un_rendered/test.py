# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
session = tf.InteractiveSession()

X = tf.constant(np.eye(10000))
Y = tf.constant(np.random.randn(10000, 300))

#print("{} Kb".format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))

Z = tf.matmul(X, Y)
Z.eval()

session.close()