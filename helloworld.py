#! /usr/bin/env python3
#! _*_ coding: utf-8 _*_

'''
HelloWorld example using TensorFlow library.
'''

from __future__ import print_function
import tensorflow as tf
import os

# Simple hello world using TensorFlow

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Create a Constant op
# The op is added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.
hello = tf.constant('Hello, TensorFlow!')

# Start tf session
sess = tf.Session()

# Run the op
print(sess.run(hello))