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

