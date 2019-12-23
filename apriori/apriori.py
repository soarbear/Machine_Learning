'''
Created on Mar 24, 2011
Ch 11 code
@author: Peter
'''
from numpy import *
import math

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
                
    C1.sort()
    #print(f'[createC1] map(frozenset, C1): {map(frozenset, C1)}')
    return list(map(frozenset, C1))#use frozen set so we can use it as a key in a dict    

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if can not in ssCnt: ssCnt[can]=1
                else: ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    #print(f'[scanD] retList: {retList}, supportData: {supportData}')
    return retList, supportData

def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
    #print(f'[aprioriGen] k: {k}, Lk: {Lk}')
    for i in range(lenLk):
        for j in range(i+1, lenLk): 
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            #print(f'[aprioriGen] i: {i}, j: {j}, L1: {L1}, L2: {L2}, list(Lk[i]): {list(Lk[i])}, list(Lk[j]): {list(Lk[j])}')
            L1.sort(); L2.sort()
            if L1==L2: #if first k-2 elements are equal
                retList.append(Lk[i] | Lk[j]) #set union
    #print(f'[aprioriGen] retList: {retList}')
    return retList

def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    #print(f'[apriori]L:{L}')
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)#scan DB to get Lk
        supportData.update(supK)
        L.append(Lk)
        k += 1
        #print(f'[apriori] L:{L}')
    return L, supportData

def generateRules(L, supportData, minConf=0.7):#supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):#only get the sets with two or more items
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList         

def calcConf(freqSet, H, supportData, brl, minConf=0.7):
    prunedH = [] #create new list to return
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        if conf >= minConf: 
            print(f'[calcConf] {freqSet-conseq}--> {conseq}, conf: {conf:.2f}')
            brl.append((freqSet-conseq, conseq, round(conf,2)))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    #print(f'[rulesFromConseqonf] H[0]:{H[0]}, len(freqSet): {len(freqSet)}, freqSet: {freqSet}')
    if (len(freqSet) > (m + 1)): #try further merging
        Hmp1 = aprioriGen(H, m+1)#create Hm+1 new candidates
        #print(f'[rulesFromConseqonf] Hmp1:{Hmp1}')
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        #print(f'[rulesFromConseqonf] Hmp1:{Hmp1}')
        if (len(Hmp1) > 1):    #need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)
            
if __name__ == "__main__":
    dataSet = loadDataSet()
    minSupport = 0.5
    Lk, suppData = apriori(dataSet, minSupport)
    print(f'[main] minSupport: {minSupport}, Lk: {Lk}\nsuppDataList: {suppData}')
    minConfidence = 0.7
    ruleList = generateRules(L, suppData, minConfidence)
    print(f'[main] minConfidence: {minConfidence}\nruleList: {ruleList}')
    
