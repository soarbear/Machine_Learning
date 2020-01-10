# Machine learning
Machine learning examples for learning and practice. All tested on google colaboratory. Some examples are from "Machine Learning in Action" by Peter Harrington.

# Environment
Google Colab CPU, Ubuntu 18.04.3 LTS, Python 3.6.8, sklearn 0.21.3, Numpy 1.17.3, Pandas 0.25.2, keras 2.2.5

# kNN

  - **Target:** Find the class which new instance(point, number, alphabet etc) belongs to. 

  - **Description:** Find k(odd number) near points from dataset. The class to which many points belong is the result.

  - **Example:** Discriminate handwritten numbers from 0 to 9 using k-NearNeighbor method. In the handwritten example, in the case of test data, the accuracy rate was 98.7%, so kNN is a classification method that can be used to recognize handwritten digits.

![alt text](https://github.com/soarbear/Machine_Learning/blob/master/kNN/result_kNN.jpg)


# kd-tree

  - **Target:** Find the class which new instance(point, number, alphabet etc) belongs to. 

  - **Description:** Select the dimension x with the largest variance in the k-dimensional data set, then select the median m as the middle point of the dimension and split the data set to get 2 subsets.Repeat the process of above step for the 2 subsets until all subsets cannot be subdivided. Search for the nearest point from the root of kd-tree to leaf and reverse direction. The class of the nearest point is the result.
 
  - **Example:** New point is the green one.The nearest point found is the red one.

![alt text](https://github.com/soarbear/Machine_Learning/blob/master/kd_tree/kd_tree_newPoint.png)
![alt text](https://github.com/soarbear/Machine_Learning/blob/master/kd_tree/kd_tree_findNearestPoint.png)

# Bayes
 
  - **Target:** Find the class which new instance(point, sentense, mail etc) belongs to.

  - **Description:** Calculate conditional probability by Bayes formula.
 
  - **Example:** Discriminate whether a vocalulary list is an abusive one or not.
  
  ![alt text](https://github.com/soarbear/Machine_Learning/blob/master/bayes/bayes_result.jpg)

# Logistic_regression
 
  - **Target:** Find the class which new instance(point, sentense, mail etc) belongs to.

  - **Description:** Calculate the border for different classes with gradient ascent method.
 
  - **Example:** Draw the border of different groups of points.
  
  ![alt text](https://github.com/soarbear/Machine_Learning/blob/master/logistic_regression/logistic_regression.png)
  
# SVM
  
  - **Target:** Find the class which new instance(point, number, alphabet etc) belongs to. 
  
  - **Description:** Assuming that multiple samples can be classified, linear SVM is applied by classifying samples belonging to different labels in a straight line. However, if such a straight line does not exist, kernel tricks are used to find the hyperplane for sample classification in the mapped high-dimensional space, and nonlinear SVM is applied. Unlike logistic regression, the constraint is that the sample is at the boundary because it maximizes the interval between the samples closest to the boundary. The Lagrange multiplier method is used to simplify and solve the optimal problem with constraints to the problem without constraints.
  
  - **Example:** Draw the border of different groups of points.
  
  ![alt text](https://github.com/soarbear/Machine_Learning/blob/master/svm/svm_gaussian_kernel.png)

# AdaBoost
  
  - **Target:** Build adaboost classifier to classify new instance.
  
  - **Description:** Can someone create a powerful classifier using multiple weak classifiers? From this question, AdaBoost (Adaptive Boosting) was born. The process is as follows. Give weight d to the training samples. Their weights d are initialized to equal values. First train the weak classifier with the training data, calculate the error rate ε of the classifier, and then repeat the training with the same data set. In the second training of the classifier, the sample weight d is readjusted. The weight d of correctly classified samples is reduced, and the weight d of misclassified samples is increased. AdaBoost linearly synthesizes each classification result from a plurality of weak classifiers with a weight α assigned based on each error rate to obtain a final result.
  
  - **Example:** classify new two points with adaboost classifier.
  
  ![alt text](https://github.com/soarbear/Machine_Learning/blob/master/adaboost/adaboost_test.jpg)
  
# Regression

  - **Target:** Find an equation for the target value with respect to continuous input variable.
  
  - **Description:** Regression is the process of predicting a target value similar to classification. The difference
between regression and classification is that the variable forecasted in regression is continuous, whereas it’s discrete in classification. Regression is one of the most useful tools in statistics.
  
  - **Example:** Calculate weights with forward stagewise regression.
  
  ![alt text](https://github.com/soarbear/Machine_Learning/blob/master/regression/forward_stagewise_regression.jpg)

# Decision_tree

  - **Target:** Make a regression tree for decrete data, a model tree for continous data. 
  
  - **Description:** CART(Classification And Regression Tree).
  
  - **Example:** Make a regression tree for decrete samples, a model tree for continous samples. Compare regression tree with liear regression.
  
  ![alt text](https://github.com/soarbear/Machine_Learning/blob/master/decision_tree/regression_tree.png)

# k_means

  - **Target:** Using the cluster's mean, classify all samples into k clusters determined in advance.
  
  - **Description:** 1. Find the cluster center closest to all samples → 2. Update the cluster center → Execute 1 again → Execute 2 again. Repeat the execution of 1 until the cluster center does not change.
  
  - **Example:** Assign points to 4 clusters.
  
  ![alt text](https://github.com/soarbear/Machine_Learning/blob/master/k_means/k_means_test.jpg)
  
# Apriori 
The Apriori algorithm needs a minimum support level as an input and a data set. The algorithm will generate a list of all candidate itemsets with one item. The transaction data set will then be scanned to see which sets meet the minimum support level. Sets that don’t meet the minimum support level will get tossed out. The remaining sets will then be combined to make itemsets with two elements. Again, the transaction dataset will be scanned and itemsets not meeting the minimum support level will get tossed. This procedure will be repeated until all sets are tossed out.

# FP_Growth
  - **Description:**  The FP-growth algorithm is faster than Apriori because it requires only two scans of the database, whereas Apriori will scan the dataset to find if a given pattern is frequent or not—Apriori scans the dataset for every potential frequent item. On small datasets, this isn’t a problem, but when you’re dealing with larger datasets, this will be a problem. The FP-growth algorithm  scans the dataset only twice. The basic approach to finding frequent itemsets using the FP-growth algorithm is as follows:
  1 Build the FP-tree. 
  2 Mine frequent itemsets from the FP-tree.

# PCA
 - **Description:** The first method for dimensionality reduction is called principal component analysis (PCA). In PCA, the dataset is transformed from its original coordinate system to a new coordinate system. The new coordinate system is chosen by the data itself. The first new axis is chosen in the direction of the most variance in the data. The second axis is orthogonal to the first axis and in the direction of an orthogonal axis with the largest variance. This procedure is repeated for as many features as we had in the original
data. We’ll find that the majority of the variance is contained in the first few axes. Therefore, we can ignore the rest of the axes, and we reduce the dimensionality of our data. 
