# Python PCA
import numpy as np

def pca(X,k):#k is remained components
  # Calculate mean of each feature
  n_samples, n_features = X.shape
  mean=np.array([np.mean(X[:,i]) for i in range(n_features)])
  # Calculate normalization
  norm_X = X - mean
  # Calculate cov matrix
  cov_matrix = np.dot(np.transpose(norm_X), norm_X)
  # Calculate eigen vectors and eigen values
  eig_val, eig_vec = np.linalg.eig(cov_matrix)
  eig_pairs = [(np.abs(eig_val[i]), eig_vec[:,i]) for i in range(n_features)]
  # Sort eig_vec based on eig_val from big to small
  eig_pairs.sort(reverse=True)
  # Select the top k eig_vec
  feature = np.array([ele[1] for ele in eig_pairs[:k]])
  print(f'feature: {feature}')
  #print(f'norm_X: {norm_X}\ncov_matrix: {cov_matrix}\neig_val: {eig_val}\neig_vec: {eig_vec}\neig_pairs: {eig_pairs}\nfeature: {feature}')
  # Get new data
  data = np.dot(norm_X, np.transpose(feature))
  return data

X = np.array([[-1, 1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
print(pca(X,1))
