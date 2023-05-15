from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt


# load data and separate into X (features) and y (target variable)
data = pd.read_csv('finaldrugdataset.csv')

# assume X has 10 columns for personality traits and y has 1 column for drug use
X = data.iloc[:, [0, -2]]
y = data.iloc[:, -1]

# split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# oversample the training data using RandomOverSampler
oversample = RandomOverSampler(sampling_strategy='minority')
X_train_over, y_train_over = oversample.fit_resample(X_train, y_train)

# fit a random forest model on the oversampled training data
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train_over, y_train_over)

# predict on the test set using the trained random forest model
y_pred = rf.predict(X_test)

# evaluate the performance using confusion matrix and classification report
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# plot feature importances in ascending order
feat_importances = pd.Series(rf.feature_importances_, index=X.columns)
plt.suptitle('Random Forest features') # set title
feat_importances.sort_values().tail(2).plot(kind='barh')
plt.ylabel('Features') # Set ylabel
plt.xlabel('Relative Importance')
plt.show()

import seaborn as sns

# plot the confusion matrix
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='Blues', fmt='g')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
