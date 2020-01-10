# Result

step1 dataSet:  [['A', 'B', 'C', 'E', 'F', 'O'], ['A', 'C', 'G'], ['E', 'I'], ['A', 'C', 'D', 'E', 'G'], ['A', 'C', 'E', 'G', 'L'], ['E', 'J'], ['A', 'B', 'C', 'E', 'F', 'P'], ['A', 'C', 'D'], ['A', 'C', 'E', 'G', 'M'], ['A', 'C', 'E', 'G', 'N']]

step2 sorted dataset:  {frozenset({'F', 'C', 'O', 'A', 'E', 'B'}): 1, frozenset({'A', 'G', 'C'}): 1, frozenset({'E', 'I'}): 1, frozenset({'C', 'D', 'A', 'G', 'E'}): 1, frozenset({'C', 'A', 'G', 'L', 'E'}): 1, frozenset({'J', 'E'}): 1, frozenset({'F', 'C', 'P', 'A', 'E', 'B'}): 1, frozenset({'A', 'D', 'C'}): 1, frozenset({'C', 'M', 'A', 'G', 'E'}): 1, frozenset({'C', 'N', 'A', 'G', 'E'}): 1}

step3 FP-Tree: 
   Null Set : 1
     A : 8
       C : 8
         E : 6
           B : 2
             F : 2
           G : 4
             D : 1
         G : 1
         D : 1
     E : 2
     
step3 headerTable:  {'F': [2, <__main__.treeNode object at 0x7f4bce92f7f0>], 'C': [8, <__main__.treeNode object at 0x7f4bcea1a8d0>], 'A': [8, <__main__.treeNode object at 0x7f4bcea1a358>], 'E': [8, <__main__.treeNode object at 0x7f4bce92f748>], 'B': [2, <__main__.treeNode object at 0x7f4bce92f7b8>], 'G': [5, <__main__.treeNode object at 0x7f4bce92f710>], 'D': [2, <__main__.treeNode object at 0x7f4bce92f940>]}
bigL:  ['A', 'B', 'C', 'D', 'E', 'F', 'G']
basePat:  A
finalFrequent Item:  {'A'}
condPattBases : A {}
basePat:  B
finalFrequent Item:  {'B'}
condPattBases : B {frozenset({'C', 'E', 'A'}): 2}

step4 conditional tree for:  {'B'}
   Null Set : 1
     A : 2
       C : 2
         E : 2
bigL:  ['A', 'C', 'E']
basePat:  A
finalFrequent Item:  {'A', 'B'}
condPattBases : A {}
basePat:  C
finalFrequent Item:  {'C', 'B'}
condPattBases : C {frozenset({'A'}): 2}

step4 conditional tree for:  {'C', 'B'}
   Null Set : 1
     A : 2
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'C', 'B', 'A'}
condPattBases : A {}
basePat:  E
finalFrequent Item:  {'E', 'B'}
condPattBases : E {frozenset({'C', 'A'}): 2}

step4 conditional tree for:  {'E', 'B'}
   Null Set : 1
     A : 2
       C : 2
bigL:  ['A', 'C']
basePat:  A
finalFrequent Item:  {'A', 'E', 'B'}
condPattBases : A {}
basePat:  C
finalFrequent Item:  {'C', 'E', 'B'}
condPattBases : C {frozenset({'A'}): 2}

step4 conditional tree for:  {'C', 'E', 'B'}
   Null Set : 1
     A : 2
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'C', 'E', 'B', 'A'}
condPattBases : A {}
basePat:  C
finalFrequent Item:  {'C'}
condPattBases : C {frozenset({'A'}): 8}

step4 conditional tree for:  {'C'}
   Null Set : 1
     A : 8
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'C', 'A'}
condPattBases : A {}
basePat:  D
finalFrequent Item:  {'D'}
condPattBases : D {frozenset({'C', 'G', 'E', 'A'}): 1, frozenset({'C', 'A'}): 1}

step4 conditional tree for:  {'D'}
   Null Set : 1
     A : 2
       C : 2
bigL:  ['A', 'C']
basePat:  A
finalFrequent Item:  {'A', 'D'}
condPattBases : A {}
basePat:  C
finalFrequent Item:  {'C', 'D'}
condPattBases : C {frozenset({'A'}): 2}

step4 conditional tree for:  {'C', 'D'}
   Null Set : 1
     A : 2
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'C', 'A', 'D'}
condPattBases : A {}
basePat:  E
finalFrequent Item:  {'E'}
condPattBases : E {frozenset({'C', 'A'}): 6}

step4 conditional tree for:  {'E'}
   Null Set : 1
     A : 6
       C : 6
bigL:  ['A', 'C']
basePat:  A
finalFrequent Item:  {'A', 'E'}
condPattBases : A {}
basePat:  C
finalFrequent Item:  {'C', 'E'}
condPattBases : C {frozenset({'A'}): 6}

step4 conditional tree for:  {'C', 'E'}
   Null Set : 1
     A : 6
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'C', 'E', 'A'}
condPattBases : A {}
basePat:  F
finalFrequent Item:  {'F'}
condPattBases : F {frozenset({'C', 'E', 'B', 'A'}): 2}

step4 conditional tree for:  {'F'}
   Null Set : 1
     A : 2
       B : 2
         C : 2
           E : 2
bigL:  ['A', 'B', 'C', 'E']
basePat:  A
finalFrequent Item:  {'F', 'A'}
condPattBases : A {}
basePat:  B
finalFrequent Item:  {'F', 'B'}
condPattBases : B {frozenset({'A'}): 2}

step4 conditional tree for:  {'F', 'B'}
   Null Set : 1
     A : 2
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'F', 'B', 'A'}
condPattBases : A {}
basePat:  C
finalFrequent Item:  {'F', 'C'}
condPattBases : C {frozenset({'A', 'B'}): 2}

step4 conditional tree for:  {'F', 'C'}
   Null Set : 1
     A : 2
       B : 2
bigL:  ['A', 'B']
basePat:  A
finalFrequent Item:  {'F', 'A', 'C'}
condPattBases : A {}
basePat:  B
finalFrequent Item:  {'F', 'B', 'C'}
condPattBases : B {frozenset({'A'}): 2}

step4 conditional tree for:  {'F', 'B', 'C'}
   Null Set : 1
     A : 2
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'F', 'B', 'A', 'C'}
condPattBases : A {}
basePat:  E
finalFrequent Item:  {'F', 'E'}
condPattBases : E {frozenset({'C', 'B', 'A'}): 2}

step4 conditional tree for:  {'F', 'E'}
   Null Set : 1
     A : 2
       B : 2
         C : 2
bigL:  ['A', 'B', 'C']
basePat:  A
finalFrequent Item:  {'F', 'E', 'A'}
condPattBases : A {}
basePat:  B
finalFrequent Item:  {'F', 'E', 'B'}
condPattBases : B {frozenset({'A'}): 2}

step4 conditional tree for:  {'F', 'E', 'B'}
   Null Set : 1
     A : 2
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'F', 'E', 'B', 'A'}
condPattBases : A {}
basePat:  C
finalFrequent Item:  {'F', 'E', 'C'}
condPattBases : C {frozenset({'A', 'B'}): 2}

step4 conditional tree for:  {'F', 'E', 'C'}
   Null Set : 1
     A : 2
       B : 2
bigL:  ['A', 'B']
basePat:  A
finalFrequent Item:  {'F', 'E', 'A', 'C'}
condPattBases : A {}
basePat:  B
finalFrequent Item:  {'F', 'E', 'B', 'C'}
condPattBases : B {frozenset({'A'}): 2}

step4 conditional tree for:  {'F', 'E', 'B', 'C'}
   Null Set : 1
     A : 2
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'F', 'C', 'A', 'E', 'B'}
condPattBases : A {}
basePat:  G
finalFrequent Item:  {'G'}
condPattBases : G {frozenset({'C', 'A'}): 1, frozenset({'C', 'E', 'A'}): 4}

step4 conditional tree for:  {'G'}
   Null Set : 1
     A : 5
       C : 5
         E : 4
bigL:  ['A', 'C', 'E']
basePat:  A
finalFrequent Item:  {'A', 'G'}
condPattBases : A {}
basePat:  C
finalFrequent Item:  {'C', 'G'}
condPattBases : C {frozenset({'A'}): 5}

step4 conditional tree for:  {'C', 'G'}
   Null Set : 1
     A : 5
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'C', 'G', 'A'}
condPattBases : A {}
basePat:  E
finalFrequent Item:  {'G', 'E'}
condPattBases : E {frozenset({'C', 'A'}): 4}

step4 conditional tree for:  {'G', 'E'}
   Null Set : 1
     A : 4
       C : 4
bigL:  ['A', 'C']
basePat:  A
finalFrequent Item:  {'A', 'G', 'E'}
condPattBases : A {}
basePat:  C
finalFrequent Item:  {'C', 'G', 'E'}
condPattBases : C {frozenset({'A'}): 4}

step4 conditional tree for:  {'C', 'G', 'E'}
   Null Set : 1
     A : 4
bigL:  ['A']
basePat:  A
finalFrequent Item:  {'C', 'G', 'E', 'A'}
condPattBases : A {}
step4 myFreqList:  [{'A'}, {'B'}, {'A', 'B'}, {'C', 'B'}, {'C', 'B', 'A'}, {'E', 'B'}, {'A', 'E', 'B'}, {'C', 'E', 'B'}, {'C', 'E', 'B', 'A'}, {'C'}, {'C', 'A'}, {'D'}, {'A', 'D'}, {'C', 'D'}, {'C', 'A', 'D'}, {'E'}, {'A', 'E'}, {'C', 'E'}, {'C', 'E', 'A'}, {'F'}, {'F', 'A'}, {'F', 'B'}, {'F', 'B', 'A'}, {'F', 'C'}, {'F', 'A', 'C'}, {'F', 'B', 'C'}, {'F', 'B', 'A', 'C'}, {'F', 'E'}, {'F', 'E', 'A'}, {'F', 'E', 'B'}, {'F', 'E', 'B', 'A'}, {'F', 'E', 'C'}, {'F', 'E', 'A', 'C'}, {'F', 'E', 'B', 'C'}, {'F', 'C', 'A', 'E', 'B'}, {'G'}, {'A', 'G'}, {'C', 'G'}, {'C', 'G', 'A'}, {'G', 'E'}, {'A', 'G', 'E'}, {'C', 'G', 'E'}, {'C', 'G', 'E', 'A'}]
step4 myFPtree.children:  {dict_values([<__main__.treeNode object at 0x7f4bcea1a358>, <__main__.treeNode object at 0x7f4bce92f860>])}
