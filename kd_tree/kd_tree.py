# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
#from time import time

#
# load data from dataset file. 
#
def load_data(fileName):
    data_mat = []
    with open(fileName) as fd:
        for line in fd.readlines():
            data = line.strip().split()
            data = [float(item) for item in data]
            data_mat.append(data)
    data_mat = np.array(data_mat)
    label = data_mat[:, 2]
    data_mat = data_mat[:, :2]
    return data_mat, label
#
# create a tree for dataset.
#
def create_kdtree(dataset, depth):
    n = np.shape(dataset)[0]
    tree_node = {}
    if n == 0:
        return None
    else:
        n, m = np.shape(dataset)
        split_axis = depth % m
        depth += 1
        tree_node['split'] = split_axis
        dataset = sorted(dataset, key=lambda a: a[split_axis])
        num = n // 2
        tree_node['median'] = dataset[num]
        tree_node['left'] = create_kdtree(dataset[:num], depth)
        tree_node['right'] = create_kdtree(dataset[num + 1:], depth)
        return tree_node
#
# search k near points on the tree. 
#
def search_kdtree(tree, data):
    k = len(data)
    if tree is None:
        return [0] * k, float('inf')
    split_axis = tree['split']
    median_point = tree['median']
    if data[split_axis] <= median_point[split_axis]:
        nearest_point, nearest_distance = search_kdtree(tree['left'], data)
    else:
        nearest_point, nearest_distance = search_kdtree(tree['right'], data)
    
    # the distance between data to current point.
    now_distance = np.linalg.norm(data - median_point)
    if now_distance < nearest_distance:
        nearest_distance = now_distance
        nearest_point = median_point.copy()
        
    # the distance between hyperplane.
    split_distance = abs(data[split_axis] - median_point[split_axis])
    if split_distance > nearest_distance:
        return nearest_point, nearest_distance
    else:
        if data[split_axis] <= median_point[split_axis]:
            next_tree = tree['right']
        else:
            next_tree = tree['left']
        near_point, near_distance = search_kdtree(next_tree, data)
        if near_distance < nearest_distance:
            nearest_distance = near_distance
            nearest_point = near_point.copy()
        return nearest_point, nearest_distance
#
# main.
#
if __name__ == '__main__':
    data_mat, label = load_data('/content/drive/My Drive/Colab Notebooks/Machine_Learning/kd_tree/dataset.txt')
    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    ax.scatter(data_mat[:, 0], data_mat[:, 1], c=label, cmap=plt.cm.Paired)

    new_point = [2, 4.5]
    kdtree = create_kdtree(data_mat, 0)
    print(kdtree)
    #start = time()
    nearest_point, near_dis= search_kdtree(kdtree, new_point)
    #print(time()-start)
    ax.scatter(new_point[0], new_point[1], c='g', s=50)
    ax.scatter(nearest_point[0], nearest_point[1], c='r', s=50)
    plt.show()
