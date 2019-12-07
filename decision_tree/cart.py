#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
from functools import namedtuple
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    dataset = []
    with open(filename, 'r') as f:
        for line in f:
            line_data = [float(data) for data in line.split()]
            dataset.append(line_data)
    return dataset

def split_dataset(dataset, feat_idx, value):
    ldata, rdata = [], []
    for data in dataset:
        if data[feat_idx] < value:
            ldata.append(data)
        else:
            rdata.append(data)
    return ldata, rdata

def create_tree(dataset, fleaf, ferr, opt=None):
    if opt is None:
        opt = {'err_tolerance': 1, 'n_tolerance': 4}

    feat_idx, value = choose_best_feature(dataset, fleaf, ferr, opt)
    if feat_idx is None:
        return value
    tree = {'feat_idx': feat_idx, 'feat_val': value}
    ldata, rdata = split_dataset(dataset, feat_idx, value)
    ltree = create_tree(ldata, fleaf, ferr, opt)
    rtree = create_tree(rdata, fleaf, ferr, opt)
    tree['left'] = ltree
    tree['right'] = rtree
    return tree

def fleaf(dataset):
    dataset = np.array(dataset)
    return np.mean(dataset[:, -1])

def ferr(dataset):
    dataset = np.array(dataset)
    m, _ = dataset.shape
    return np.var(dataset[:, -1])*dataset.shape[0]

def choose_best_feature(dataset, fleaf, ferr, opt):
    dataset = np.array(dataset)
    m, n = dataset.shape
    err_tolerance, n_tolerance = opt['err_tolerance'], opt['n_tolerance']

    err = ferr(dataset)
    best_feat_idx, best_feat_val, best_err = 0, 0, float('inf')

    for feat_idx in range(n-1):
        values = dataset[:, feat_idx]
        for val in values:
            ldata, rdata = split_dataset(dataset.tolist(), feat_idx, val)
            if len(ldata) < n_tolerance or len(rdata) < n_tolerance:
                continue
            new_err = ferr(ldata) + ferr(rdata)
            if new_err < best_err:
                best_feat_idx = feat_idx
                best_feat_val = val
                best_err = new_err

    if abs(err - best_err) < err_tolerance:
        return None, fleaf(dataset)

    ldata, rdata = split_dataset(dataset.tolist(), best_feat_idx, best_feat_val)
    if len(ldata) < n_tolerance or len(rdata) < n_tolerance:
        return None, fleaf(dataset)

    return best_feat_idx, best_feat_val

def get_nodes_edges(tree, root_node=None):
    Node = namedtuple('Node', ['id', 'label'])
    Edge = namedtuple('Edge', ['start', 'end'])

    nodes, edges = [], []
    if type(tree) is not dict:
        return nodes, edges
    if root_node is None:
        label = '{}: {}'.format(tree['feat_idx'], tree['feat_val'])
        root_node = Node._make([uuid.uuid4(), label])
        nodes.append(root_node)
    for sub_tree in (tree['left'], tree['right']):
        if type(sub_tree) is dict:
            node_label = '{}: {}'.format(sub_tree['feat_idx'], sub_tree['feat_val'])
        else:
            node_label = '{:.2f}'.format(sub_tree)
        sub_node = Node._make([uuid.uuid4(), node_label])
        nodes.append(sub_node)
        edge = Edge._make([root_node, sub_node])
        edges.append(edge)
        sub_nodes, sub_edges = get_nodes_edges(sub_tree, root_node=sub_node)
        nodes.extend(sub_nodes)
        edges.extend(sub_edges)
    return nodes, edges

def dotify(tree):
    content = 'digraph decision_tree {\n'
    nodes, edges = get_nodes_edges(tree)
    for node in nodes:
        content += '    "{}" [label="{}"];\n'.format(node.id, node.label)
    for edge in edges:
        start, end = edge.start, edge.end
        content += '    "{}" -> "{}";\n'.format(start.id, end.id)
    content += '}'
    return content

def regression_tree(data, tree):
    if type(tree) is not dict:
        return tree
    feat_idx, feat_val = tree['feat_idx'], tree['feat_val']
    if data[feat_idx] < feat_val:
        sub_tree = tree['left']
    else:
        sub_tree = tree['right']

    return regression_tree(data, sub_tree)

def linear_regression(dataset):
    dataset = np.matrix(dataset)
    X_ori, y = dataset[:, :-1], dataset[:, -1]
    X_ori, y = np.matrix(X_ori), np.matrix(y)
    m, n = X_ori.shape
    X = np.matrix(np.ones((m, n+1)))
    X[:, 1:] = X_ori
    w = (X.T*X).I*X.T*y
    return w, X, y

def linear_fleaf(dataset):
    w, _, _ = linear_regression(dataset)
    return w

def linear_ferr(dataset):
    w, X, y = linear_regression(dataset)
    y_prime = X*w
    return np.var(y_prime - y)

def model_tree(data, tree):
    if type(tree) is not dict:
        w = tree
        y = np.matrix(data)*w
        return y[0, 0]
    feat_idx, feat_val = tree['feat_idx'], tree['feat_val']
    if data[feat_idx+1] < feat_val:
        return model_tree(data, tree['left'])
    else:
        return model_tree(data, tree['right'])

def get_corrcoef(X, Y):
    cov = np.mean(X*Y) - np.mean(X)*np.mean(Y)
    return cov/(np.var(X)*np.var(Y))**0.5

if '__main__' == __name__:
    # regression tree
    datafile = '/content/drive/My Drive/Colab Notebooks/Machine_Learning/CART/ex1.txt'
    dataset = load_data(datafile)
    tree = create_tree(dataset, fleaf, ferr, opt={'err_tolerance':1, 'n_tolerance':4})
    print(f'regression_tree: {tree}')
    dataset = np.array(dataset)
    plt.figure(figsize=(8, 6))
    plt.scatter(dataset[:, 0], dataset[:, 1])
    x = np.linspace(0, 1, 50)
    y = [regression_tree([i], tree) for i in x]
    plt.plot(x, y, c='r')
    plt.show()
    
    # model tree
    datafile = '/content/drive/My Drive/Colab Notebooks/Machine_Learning/CART/ex2.txt'
    dataset = load_data(datafile)
    tree = create_tree(dataset, linear_fleaf, linear_ferr, opt={'err_tolerance':0.1, 'n_tolerance':4})
    print(f'mode_tree: {tree}')
    dataset = np.array(dataset)
    plt.figure(figsize=(8, 6))
    plt.scatter(dataset[:, 0], dataset[:, 1])
    x = np.sort(dataset[:, 0])
    y = [model_tree([1.0] + [i], tree) for i in x]
    plt.plot(x, y, c='r')
    plt.show()

    # compare regression tree with linear regression
    data_train = load_data('/content/drive/My Drive/Colab Notebooks/Machine_Learning/CART/bikeSpeedVsIq_train.txt')
    data_test = load_data('/content/drive/My Drive/Colab Notebooks/Machine_Learning/CART/bikeSpeedVsIq_test.txt')
    dataset_test = np.matrix(data_test)
    m, n = dataset_test.shape
    testset = np.ones((m, n+1))
    testset[:, 1:] = dataset_test
    X_test, y_test = testset[:, :-1], testset[:, -1]

    w, X, y = linear_regression(data_train)
    y_lr = X_test*w
    y_test = np.array(y_test).T
    y_lr = np.array(y_lr).T[0]
    corrcoef_lr = get_corrcoef(y_test, y_lr)
    print('linear regression correlation coefficient: {}'.format(corrcoef_lr))

    tree = create_tree(data_train, fleaf, ferr, opt={'err_tolerance': 1, 'n_tolerance': 4})
    y_tree = [regression_tree([x], tree) for x in X_test[:, 1].tolist()]
    corrcoef_tree = get_corrcoef(np.array(y_tree), y_test)
    print('regression tree correlation coefficient: {}'.format(corrcoef_tree))

    plt.figure(figsize=(8, 6))
    plt.scatter(np.array(data_train)[:, 0], np.array(data_train)[:, 1])
    x = np.sort([i for i in X_test[:, 1].tolist()])
    y = [np.dot([1.0, i], np.array(w.T).tolist()[0]) for i in x]
    plt.plot(x, y, c='r')

    y = [regression_tree([i], tree) for i in x]
    plt.plot(x, y, c='y')
    plt.show()
