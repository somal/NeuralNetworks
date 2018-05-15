import urllib
from urllib import request
import numpy as np

fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

# here goes your solution
Y = data[:, 0]
X = data[:, 1:]
ones = np.ones_like(Y).reshape((Y.shape[0], 1))
X = np.hstack((ones, X))

B = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
print(" ".join(["{}".format(x) for x in B]))
