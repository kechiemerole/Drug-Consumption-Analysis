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
X = data.iloc[:, :10]
y = data.iloc[:, 10:].values.ravel()

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
feat_importances.sort_values().tail(10).plot(kind='barh')
plt.ylabel('Features', fontsize=12) # Set ylabel
plt.xlabel('Relative Importance')
plt.show()

import seaborn as sns

# plot the confusion matrix
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='Blues', fmt='g')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

#__________________________________________________________________________________________
from sklearn.metrics import roc_curve, auc

# predict probabilities on the test set using the trained random forest model
y_prob = rf.predict_proba(X_test)[:, 1]

# calculate false positive rate, true positive rate, and threshold values
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# calculate area under the ROC curve (AUC)
roc_auc = auc(fpr, tpr)

# plot the ROC curve
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

###_________________________________________________________________

# plot feature importances for to subset of features in ascending order
feat_importances = pd.Series(rf.feature_importances_, index=X.columns)
plt.suptitle('Random Forest features') # set title
feat_importances.sort_values().tail(2).plot(kind='barh')
plt.ylabel('Features', fontsize=12) # Set ylabel
plt.xlabel('Relative Importance')
plt.show()

#____________________________________________________________________________
#plotting ROC curve for subset of important features 
from sklearn.metrics import roc_curve, auc

# Fit a random forest model to the training data
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Make predictions on the test data
y_pred_proba = rf.predict_proba(X_test)[:, 1]

# Compute the false positive rate (fpr) and true positive rate (tpr) for varying threshold values
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

# Compute the area under the ROC curve (AUC)
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})')

# Set the labels and title
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')

# Plot the random guessing line
plt.plot([0, 1], [0, 1], linestyle='--')

# Show the legend and plot
plt.legend()
plt.show()
