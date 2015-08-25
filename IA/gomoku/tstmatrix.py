# caian 25/08/2015
# This is simple test file to diagonal function from matrix

from matrix import Matrix

m = Matrix(15,15):
for i in range(len(m)):
    m[i] = i

print m
for d in range(-30, 30):
    print m.diagonal(d)
