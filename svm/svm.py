# -*- coding: utf-8 -*-
import numpy as np
from sklearn import svm, datasets
import matplotlib.pyplot as plt
from itertools import product

if __name__ == '__main__':
    iris = datasets.load_iris()
    X = iris.data[:100, :2]
    X += np.random.uniform(0, 1.0, size=np.shape(X))
    y = iris.target[:100]
    h = 0.02
    cs = [0.1, 1000]
    gammas = [0.001, 10]

    svms = [svm.SVC(C=C, gamma=gamma).fit(X, y) for C, gamma in product(cs, gammas)]
    titles = ["C=0.01, gamma=0.001", "C=0.01, gamma=10", "C=1000, gamma=0.001", "C=1000, gamma=10"]
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    plt.figure(figsize=(10, 10))
    for i, clf in enumerate(svms):
        plt.subplot(2, 2, i + 1)
        plt.subplots_adjust(wspace=0.4, hspace=0.4)
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.2)
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
        plt.xlabel("X1")
        plt.ylabel("X2")
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.xticks(())
        plt.yticks(())
        plt.title(titles[i])
    plt.show()
    
