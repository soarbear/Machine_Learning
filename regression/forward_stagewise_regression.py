'''
Created on Jan 8, 2011

@author: Peter
'''
from numpy import *
from time import sleep
#import json
#import urllib2

def loadDataSet(fileName):      #general function to parse tab -delimited floats
  numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields 
  dataMat = []; labelMat = []
  fr = open(fileName)
  for line in fr.readlines():
    lineArr =[]
    curLine = line.strip().split('\t')
    for i in range(numFeat):
        lineArr.append(float(curLine[i]))
    dataMat.append(lineArr)
    labelMat.append(float(curLine[-1]))
  return dataMat,labelMat

def rssError(yArr,yHatArr): #yArr and yHatArr both need to be arrays
    return ((yArr-yHatArr)**2).sum()

def stageWise(xArr,yArr,eps=0.01,numIt=100):
  xMat = mat(xArr); yMat=mat(yArr).T
  yMean = mean(yMat,0)
  yMat = yMat - yMean     #can also regularize ys but will get smaller coef
  xMat = regularize(xMat)
  m,n=shape(xMat)
  #returnMat = zeros((numIt,n)) #testing code remove
  ws = zeros((n,1)); wsTest = ws.copy(); wsMax = ws.copy()
  for i in range(numIt):
    print(ws.T)
    lowestError = inf; 
    for j in range(n):
      for sign in [-1,1]:
        wsTest = ws.copy()
        wsTest[j] += eps*sign
        yTest = xMat*wsTest
        rssE = rssError(yMat.A,yTest.A)
        if rssE < lowestError:
          lowestError = rssE
          wsMax = wsTest
    ws = wsMax.copy()
    #returnMat[i,:]=ws.T
  #return returnMat

if __name__ == "__main__":
  xArr,yArr=loadDataSet('/content/drive/My Drive/Colab Notebooks/Machine_Learning/regression/abalone.txt')
  stageWise(xArr,yArr,0.001,5000)
