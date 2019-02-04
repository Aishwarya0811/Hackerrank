import numpy
r, c = map(int, raw_input().split())
i = numpy.array([raw_input().split() for _ in range(r)], int)
print numpy.transpose(i)
print i.flatten()