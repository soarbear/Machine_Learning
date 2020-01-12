from numpy import *

def loadExData():
    return[[0, 0, 0, 2, 2],
           [0, 0, 0, 3, 3],
           [0, 0, 0, 1, 1],
           [1, 1, 1, 0, 0],
           [2, 2, 2, 0, 0],
           [5, 5, 5, 0, 0],
           [1, 1, 1, 0, 0]]

dataSet = loadExData()
U, Sigma, VT = linalg.svd(dataSet)
print(f'dataSet:\n{dataSet}')
print(f'U:\n{U}\nSigma:\n{Sigma}\nVT:\n{VT}')

Sig3 = mat([[Sigma[0], 0, 0], [0, Sigma[1], 0], [0, 0, Sigma[2]]])
print(f'U[:,:3] * Sig3 * VT[:3,:]:\n{U[:,:3] * Sig3 * VT[:3,:]}')
