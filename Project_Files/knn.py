import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.inspection import permutation_importance


# load the data
data = pd.read_csv('finaldrugdataset.csv')

# select features and target variable
X = data[['Age', 'Gender', 'Education', 'Nscore', 'Ascore', 'Impulsive', 'SS', 'Cscore', 'Oscore', 'Escore']]
y = data['DrugUse']

# split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# perform k-NN classification with 7, 10, and 15 nearest neighbors
for n_neighbors in [3, 11, 15]:
    # initialize the k-NN classifier
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    # fit the model on the training data
    knn.fit(X_train, y_train)
    # predict drug use on the test data
    y_pred = knn.predict(X_test)
    # evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"k-NN with {n_neighbors} neighbors has accuracy of {accuracy:.4f}")


# Load the data
data = pd.read_csv('finaldrugdataset.csv')

# Split the data into features and target
X = data[['Age', 'Gender', 'Education', 'Nscore', 'Ascore', 'Impulsive', 'SS', 'Cscore', 'Oscore', 'Escore']]
y = data['DrugUse']

# Create the KNN model with 7 nearest neighbors
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the model to the data
knn.fit(X, y)

# Calculate the feature importance using permutation importance
result = permutation_importance(knn, X, y, n_repeats=10, random_state=42)
importance = result.importances_mean

# Sort the features by importance in descending order
sorted_idx = importance.argsort()[::-1]

# Plot the feature importances
plt.barh(range(X.shape[1]), importance[sorted_idx])
plt.yticks(range(X.shape[1]), X.columns[sorted_idx])
plt.xlabel('Mean Decrease Impurity')
plt.show()
