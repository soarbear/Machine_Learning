# Machine_Learning
Machine learning sample source code tested under Google Colaboratory for learning and practice. All tested on google colaboratory. Some examples are from "Machine Learning in Action" by Peter Harrington.
 
 - [x]**kNN.** 

  - **Target:** Find the class which new instance(point, number, alphabet etc) belongs to. 

  - **Procedure:** Find k(odd number) near points from dataset. The class to which many points belong is the rsult.

  - **Example:** Discriminate handwritten numbers from 0 to 9 using k-NearNeighbor method. In the handwritten example, in the case of test data, the accuracy rate was 98.7%, so kNN is a classification method that can be used to recognize handwritten digits.

![alt text](https://github.com/soarbear/Machine_Learning/blob/master/kNN/result_kNN.jpg)


 - [x]**kd-tree.** 

  - **Target:** Find the class which new instance(point, number, alphabet etc) belongs to. 

  - **Procedure:** Select the dimension x with the largest variance in the k-dimensional data set, then select the median m as the middle point of the dimension and split the data set to get 2 subsets.Repeat the process of above step for the 2 subsets until all subsets cannot be subdivided. Search for the nearest point from the root of kd-tree to leaf and reverse direction. The class of the nearest point is the reult.
 
  - **Example:** New point is the green one.The nearest point is the red one.

![alt text](https://github.com/soarbear/Machine_Learning/blob/master/kd_tree/kd_tree_newPoint.png)
![alt text](https://github.com/soarbear/Machine_Learning/blob/master/kd_tree/kd_tree_findNearestPoint.png)

 - [x]**- Continuing...** 
 
 Updated once a week.
