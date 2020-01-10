'''
Created on Jun 14, 2011
FP-Growth FP means frequent pattern
the FP-Growth algorithm needs: 
1. FP-tree (class treeNode)
2. header table (use dict)
This finds frequent itemsets similar to apriori but does not 
find association rules.  
@author: Peter
'''
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode      #needs to be updated
        self.children = {} 
    
    def inc(self, numOccur):
        self.count += numOccur
        
    def disp(self, ind=1):
        print('  '*ind, self.name, ':', self.count)
        for child in self.children.values():
            child.disp(ind+1)

def createTree(dataSet, minSup=1): #create FP-tree from dataset but don't mine
    headerTable = {}
    #go over dataSet twice
    for trans in dataSet:#first pass counts frequency of occurance
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    headerTableCopy = headerTable.copy()
    for k in headerTableCopy.keys():  #remove items not meeting minSup
        if headerTable[k] < minSup: 
            del(headerTable[k])
    #headerTable = {k: v for k, v in sorted(headerTable.items(), key=lambda item: item[0])}
    #headerTable = {k: v for k, v in sorted(headerTable.items(), key=lambda item: item[1], reverse=True)}
    #print('step3 headerTable: ',headerTable)

    freqItemSet = set(headerTable.keys())
    #print('freqItemSet: ',freqItemSet)
    if len(freqItemSet) == 0: return None, None  #if no items meet min support -->get out
    for k in headerTable:
        headerTable[k] = [headerTable[k], None] #reformat headerTable to use Node link 
    #print('headerTable: ',headerTable)
    retTree = treeNode('Null Set', 1, None) #create tree
    for tranSet, count in dataSet.items():  #go through dataset 2nd time
        localD = {}
        for item in tranSet:  #put transaction items in order
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        localD = {k: v for k, v in sorted(localD.items(), key=lambda item: item[0])}

        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)#populate tree with ordered freq itemset
    return retTree, headerTable #return tree and header table

def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:#check if orderedItems[0] in retTree.children
        inTree.children[items[0]].inc(count) #incrament count
    else:   #add items[0] to inTree.children
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None: #update header table 
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:#call updateTree() with remaining ordered items
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)
        
def updateHeader(nodeToTest, targetNode):   #this version does not use recursion
    while (nodeToTest.nodeLink != None):    #Do not use recursion to traverse a linked list!
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode
        
def ascendTree(leafNode, prefixPath): #ascends from leaf node to root
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)
    
def findPrefixPath(basePat, treeNode): #treeNode comes from header table
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[0])]#(sort header table)
    print('bigL: ',bigL)
    for basePat in bigL:  #start from bottom of header table
        print('basePat: ',basePat)
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        print('finalFrequent Item: ',newFreqSet)    #append to set
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        print('condPattBases :',basePat, condPattBases)
        #2. construct cond FP-tree from cond. pattern base
        myCondTree, myHead = createTree(condPattBases, minSup)
        #print 'head from conditional tree: ', myHead
        if myHead != None: #3. mine cond. FP-tree
            print('step4 conditional tree for: ',newFreqSet)
            myCondTree.disp(1)            
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)

def loadSimpDat():
    '''
    simpDat = [['r', 'z', 'h', 'j', 'p'],
               ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               ['z'],
               ['r', 'x', 'n', 'o', 's'],
               ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]
    '''
    Dataset = [['A', 'B', 'C', 'E', 'F', 'O'],
               ['A', 'C', 'G'],
               ['E', 'I'],
               ['A', 'C', 'D', 'E', 'G'],
               ['A', 'C', 'E', 'G', 'L'],
               ['E', 'J'],
               ['A', 'B', 'C', 'E', 'F', 'P'],
               ['A', 'C', 'D'],
               ['A', 'C', 'E', 'G', 'M'],
               ['A', 'C', 'E', 'G', 'N']]
    return Dataset

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        #print('trans: ', trans)
        retDict[frozenset(trans)] = 1
    return retDict

minSup = 2
simpDat = loadSimpDat()
print('step1 dataSet: ',simpDat)
initSet = createInitSet(simpDat)
print('step2 sorted dataset: ',initSet)
myFPtree, myHeaderTab = createTree(initSet, minSup)
print('step3 FP-Tree: ')
myFPtree.disp()
print('step3 headerTable: ',myHeaderTab)
myFreqList = []
mineTree(myFPtree, myHeaderTab, minSup, set([]), myFreqList)
print('step4 myFreqList: ',myFreqList)
print('step4 myFPtree.children: ',{myFPtree.children.values()})
