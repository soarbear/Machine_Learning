# Result

minSupport: 0.5, minConfidence: 0.7

[main] minSupport: 0.5

Lk: [[frozenset({5}), frozenset({2}), frozenset({3}), frozenset({1})], [frozenset({2, 3}), frozenset({3, 5}), frozenset({2, 5}), frozenset({1, 3})], [frozenset({2, 3, 5})], []]

suppDataList: {frozenset({1}): 0.5, frozenset({3}): 0.75, frozenset({4}): 0.25, frozenset({2}): 0.75, frozenset({5}): 0.75, frozenset({1, 3}): 0.5, frozenset({2, 5}): 0.75, frozenset({3, 5}): 0.5, frozenset({2, 3}): 0.5, frozenset({1, 5}): 0.25, frozenset({1, 2}): 0.25, 

frozenset({2, 3, 5}): 0.5}

[calcConf] frozenset({5})--> frozenset({2}), conf: 1.00

[calcConf] frozenset({2})--> frozenset({5}), conf: 1.00

[calcConf] frozenset({1})--> frozenset({3}), conf: 1.00

[main] minConfidence: 0.7

ruleList: [(frozenset({5}), frozenset({2}), 1.0), (frozenset({2}), frozenset({5}), 1.0), (frozenset({1}), frozenset({3}), 1.0)]

minSupport: 0.5, minConfidence: 0.5

[main] minSupport: 0.5
Lk: [[frozenset({5}), frozenset({2}), frozenset({3}), frozenset({1})], [frozenset({2, 3}), frozenset({3, 5}), frozenset({2, 5}), frozenset({1, 3})], [frozenset({2, 3, 5})], []]

suppDataList: {frozenset({1}): 0.5, frozenset({3}): 0.75, frozenset({4}): 0.25, frozenset({2}): 0.75, frozenset({5}): 0.75, 
frozenset({1, 3}): 0.5, frozenset({2, 5}): 0.75, frozenset({3, 5}): 0.5, frozenset({2, 3}): 0.5, frozenset({1, 5}): 0.25, frozenset({1, 2}): 0.25, frozenset({2, 3, 5}): 0.5}

[calcConf] frozenset({3})--> frozenset({2}), conf: 0.67

[calcConf] frozenset({2})--> frozenset({3}), conf: 0.67

[calcConf] frozenset({5})--> frozenset({3}), conf: 0.67

[calcConf] frozenset({3})--> frozenset({5}), conf: 0.67

[calcConf] frozenset({5})--> frozenset({2}), conf: 1.00

[calcConf] frozenset({2})--> frozenset({5}), conf: 1.00

[calcConf] frozenset({3})--> frozenset({1}), conf: 0.67

[calcConf] frozenset({1})--> frozenset({3}), conf: 1.00

[calcConf] frozenset({5})--> frozenset({2, 3}), conf: 0.67

[calcConf] frozenset({3})--> frozenset({2, 5}), conf: 0.67

[calcConf] frozenset({2})--> frozenset({3, 5}), conf: 0.67

[main] minConfidence: 0.5

ruleList: [(frozenset({3}), frozenset({2}), 0.67), (frozenset({2}), frozenset({3}), 0.67), (frozenset({5}), frozenset({3}), 0.67), (frozenset({3}), frozenset({5}), 0.67), (frozenset({5}), frozenset({2}), 1.0), (frozenset({2}), frozenset({5}), 1.0), (frozenset({3}), frozenset({1}), 0.67), (frozenset({1}), frozenset({3}), 1.0), (frozenset({5}), frozenset({2, 3}), 0.67), (frozenset({3}), frozenset({2, 5}), 0.67), (frozenset({2}), frozenset({3, 5}), 0.67)]
