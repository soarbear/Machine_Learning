'''
Created on Oct 27, 2010
Logistic Regression Working Module
@author: Peter
'''
from numpy import *
#
# Load dataset, points(x1,x2) from 2 classes.
#
def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('/content/drive/My Drive/Colab Notebooks/Machine_Learning/logistic_regression/testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat
#
# Activation function.
#
def sigmoid(inX):
    return 1.0/(1+exp(-inX))
#
# Calulate weights with gradient asent method.
#
def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)             #convert to NumPy matrix
    labelMat = mat(classLabels).transpose() #convert to NumPy matrix
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):              #heavy on matrix operations
        h = sigmoid(dataMatrix*weights)     #matrix mult
        error = (labelMat - h)              #vector subtraction
        weights = weights + alpha * dataMatrix.transpose()* error #matrix mult
    return weights
#
# Plot points and border line.
#
def plotBestFit(weights):
    import matplotlib.pyplot as plt
    dataMat,labelMat=loadDataSet()
    dataArr = array(dataMat)
    #print(f"dataArr[0,1]: {dataArr[0,1]}, dataArr[0,2]: {dataArr[0,2]}")
    n = shape(dataArr)[0] 
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    print(f"xcord1: {xcord1}, ycord1: {ycord1}")
    print(f"xcord2: {xcord2}, ycord2: {ycord2}")
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0,0]-weights[1,0]*x)/weights[2,0]
    #print(f"weights:{weights}\nx:{x}\ny:{y}")
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()
#
# Classsify new point.
#
def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5: return 1.0
    else: return 0.0
#
# main.
#
if __name__ == '__main__':
  dataMatrix, classLabels = loadDataSet()
  weights = gradAscent(dataMatrix, classLabels)
  plotBestFit(weights)
