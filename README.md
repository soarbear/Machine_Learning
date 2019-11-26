# Machine learning
Machine learning examples for learning and practice. All tested on google colaboratory. Some examples are from "Machine Learning in Action" by Peter Harrington.

# Environment
Google Colab CPU, Ubuntu 18.04.3 LTS, Python 3.6.8, sklearn 0.21.3, Numpy 1.17.3, Pandas 0.25.2, keras 2.2.5

# kNN. 

  - **Target:** Find the class which new instance(point, number, alphabet etc) belongs to. 

  - **Description:** Find k(odd number) near points from dataset. The class to which many points belong is the result.

  - **Example:** Discriminate handwritten numbers from 0 to 9 using k-NearNeighbor method. In the handwritten example, in the case of test data, the accuracy rate was 98.7%, so kNN is a classification method that can be used to recognize handwritten digits.

![alt text](https://github.com/soarbear/Machine_Learning/blob/master/kNN/result_kNN.jpg)


# kd-tree. 

  - **Target:** Find the class which new instance(point, number, alphabet etc) belongs to. 

  - **Description:** Select the dimension x with the largest variance in the k-dimensional data set, then select the median m as the middle point of the dimension and split the data set to get 2 subsets.Repeat the process of above step for the 2 subsets until all subsets cannot be subdivided. Search for the nearest point from the root of kd-tree to leaf and reverse direction. The class of the nearest point is the result.
 
  - **Example:** New point is the green one.The nearest point found is the red one.

![alt text](https://github.com/soarbear/Machine_Learning/blob/master/kd_tree/kd_tree_newPoint.png)
![alt text](https://github.com/soarbear/Machine_Learning/blob/master/kd_tree/kd_tree_findNearestPoint.png)

# bayes. 
 
  - **Target:** Find the class which new instance(point, sentense, mail etc) belongs to.

  - **Description:** Calculate conditional probability by Bayes formula.
 
  - **Example:** Discriminate whether a vocalulary list is an abusive one or not.
  
  ![alt text](https://github.com/soarbear/Machine_Learning/blob/master/bayes/bayes_result.jpg)

# logistic_regression. 
 
  - **Target:** Find the class which new instance(point, sentense, mail etc) belongs to.

  - **Description:** Calculate the border for different classes with gradient ascent method.
 
  - **Example:** Draw the border of different groups of points.
  
  ![alt text](https://github.com/soarbear/Machine_Learning/blob/master/logistic_regression/logistic_regression.png)
  
