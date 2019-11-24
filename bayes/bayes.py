'''
Created on Oct 19, 2010

@author: Peter
'''
from numpy import *
#
# Load postingList -> myVocabList.
#
def loadDataSet():
  postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
               ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
               ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
               ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
               ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
               ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
  classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
  return postingList,classVec
#
# Create myVocabList from postingList.
#
def createVocabList(dataSet):
  vocabSet = set([])  #create empty set
  for document in dataSet:
      vocabSet = vocabSet | set(document) #union of the two sets
  return list(vocabSet)
#
# Create 2 vectors(2 categories) from myVocabList.
#
def setOfWords2Vec(vocabList, inputSet):
  returnVec = [0]*len(vocabList)
  for word in inputSet:
      if word in vocabList:
          returnVec[vocabList.index(word)] = 1
      else: print(f"the word: {word} is not in my Vocabulary!")
  return returnVec
#
# Create 2 conditional probability vectors(p0Vect & p1Vect) from trainMatrix.
# Create 1 category probabilitiesies(pAbusive) from trainCategory.
#
def trainNB0(trainMatrix,trainCategory):
  numTrainDocs = len(trainMatrix)
  numWords = len(trainMatrix[0])
  pAbusive = sum(trainCategory)/float(numTrainDocs)
  p0Num = ones(numWords); p1Num = ones(numWords)      #change to ones() 
  p0Denom = 2.0; p1Denom = 2.0                        #change to 2.0
  for i in range(numTrainDocs):
      if trainCategory[i] == 1:
          p1Num += trainMatrix[i]
          p1Denom += sum(trainMatrix[i])
      else:
          p0Num += trainMatrix[i]
          p0Denom += sum(trainMatrix[i])
  p1Vect = log(p1Num/p1Denom)          #change to log()
  p0Vect = log(p0Num/p0Denom)          #change to log()
  return p0Vect,p1Vect,pAbusive
#
# Perform bayes formula. 1: testEntry is abusive, 0: not abusive.
#
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
  p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
  p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
  if p1 > p0:
      return 1
  else: 
      return 0
#
# Test 2 testEntries.
#  
def testingNB():
  listOPosts,listClasses = loadDataSet()
  myVocabList = createVocabList(listOPosts)
  trainMat=[]
  for postinDoc in listOPosts:
      trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
  p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
  testEntry = ['love', 'my', 'dalmation']
  thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
  print(f"{testEntry}, 'classified as:' {classifyNB(thisDoc,p0V,p1V,pAb)}")
  testEntry = ['stupid', 'garbage']
  thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
  print(f"{testEntry}, 'classified as:' {classifyNB(thisDoc,p0V,p1V,pAb)}")
#
# main.
#
if __name__ == '__main__':
  testingNB()
