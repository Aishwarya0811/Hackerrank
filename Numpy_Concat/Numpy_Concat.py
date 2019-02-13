import numpy as np
N, M, _ = [int(x) for x in raw_input().strip().split()]
a, b = map(lambda x: np.array([raw_input().strip().split() for i in xrange(int(x))], int), [N, M])
print np.concatenate((a, b), axis = 0)



