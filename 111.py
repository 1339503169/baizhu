def bool_dist(X, Y=None, Y_norm_squared=None, squared=False):
    N = X.shape[1]
    print(N)
    print(X.shape)
    ret = np.zeros((X.shape[0], Y.shape[0]), dtype=np.float32)
    for i in range(X.shape[0]):
        for j in range(Y.shape[0]):
            ret[i, j] = np.sum(X[i] == Y[j]) / N
    return ret
X=[[1,2,3,4,5],[1,2,3,4,5]]
Y=[[1,2,2,3,4],[1,2,3,4,5]]
import numpy as np
X=np.asarray(X)
Y=np.asarray(Y)
print(bool_dist(X,Y))
print(X[0]==Y[0])


