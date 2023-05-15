from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Load the data into a pandas dataframe
data = pd.read_csv('finaldrugdataset.csv')

# Select the independent variables
X = data[['Age', 'Gender','Education', 'Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'SS', 'Impulsive']]

# Select the dependent variable
y = data['DrugUse']

# Balance the data using RandomUnderSampler
rus = RandomUnderSampler(random_state=0)
X_resampled, y_resampled = rus.fit_resample(X, y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.4, random_state=42)

# Create a decision tree classifier object
modelDT = DecisionTreeClassifier(max_depth=5, criterion='entropy', random_state=0)

# Fit the model to the training data
modelDT.fit(X_train,y_train)

# Run a prediction test on the test set
testPredict = modelDT.predict(X_test)

# Calculate and print the accuracy score of the model
accuracy = modelDT.score(X_test, y_test)
print("Accuracy: ", accuracy)

# Calculate and print the confusion matrix and classification report
cm = confusion_matrix(y_test, testPredict)
print("Decision Tree Confusion matrix:\n", cm)
cr = classification_report(y_test, testPredict)
print("Decision Tree Classification report:\n", cr)



# Plot the feature importances
featureImportances = pd.Series(modelDT.feature_importances_, index=X.columns.values)
plt.rcParams["figure.figsize"] = (8,6)
featureImportances.sort_values(ascending = True)[-10:].plot(kind='barh')
plt.tight_layout()
plt.show()
#___________________________________________________________________________________________________________________
#ROC Curve
from sklearn.metrics import roc_curve, auc

# Calculate the probability scores for the test set
y_scores = modelDT.predict_proba(X_test)[:,1]

# Calculate the false positive rate, true positive rate, and threshold values
fpr, tpr, thresholds = roc_curve(y_test, y_scores)

# Calculate the AUC (Area Under the Curve) score
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.plot(fpr, tpr, label='ROC curve (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()



#_________________________________________________________________________________________________________
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# Load the data into a pandas dataframe
data = pd.read_csv('finaldrugdataset.csv')

# Select the independent variables
X = data[['Age', 'Oscore','SS']]

# Select the dependent variable
y = data['DrugUse']

# Balance the data using RandomUnderSampler
rus = RandomUnderSampler(random_state=0)
X_resampled, y_resampled = rus.fit_resample(X, y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.4, random_state=42)

# Create a decision tree classifier object
modelDT = DecisionTreeClassifier(max_depth=5, criterion='entropy', random_state=0)

# Fit the model to the training data
modelDT.fit(X_train,y_train)

# Run a prediction test on the test set
testPredict = modelDT.predict(X_test)

# Calculate and print the accuracy score of the model
accuracy = modelDT.score(X_test, y_test)
print("Accuracy: ", accuracy)

# Calculate and print the confusion matrix and classification report
cm = confusion_matrix(y_test, testPredict)
print("Decision Tree subset Confusion matrix:\n", cm)
cr = classification_report(y_test, testPredict)
print("Decision Tree subset Classification report:\n", cr)

# Plot the feature importances
featureImportances = pd.Series(modelDT.feature_importances_, index=X.columns.values)
plt.rcParams["figure.figsize"] = (8,6)
featureImportances.sort_values(ascending = True)[-5:].plot(kind='barh')
plt.tight_layout()
plt.show()

#_______________________________________________________________________________
# Import necessary modules
from sklearn.metrics import roc_curve, roc_auc_score

# Get the predicted probabilities for the test set
y_prob = modelDT.predict_proba(X_test)[:,1]

# Calculate the ROC curve and AUC score
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
auc_score = roc_auc_score(y_test, y_prob)

# Plot the ROC curve
plt.plot(fpr, tpr, label='AUC = {:.2f}'.format(auc_score))
plt.plot([0, 1], [0, 1], linestyle='--', color='r', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for decision tree subset')
plt.legend()
plt.show()


#____________________________________________
#cross validation 
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

# Load the data into a pandas dataframe
data = pd.read_csv('finaldrugdataset.csv')

# Select the independent variables
X = data[['Age', 'Gender','Education', 'Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'SS', 'Impulsive']]

# Select the dependent variable
y = data['DrugUse']

# Create a decision tree classifier object
modelDT = DecisionTreeClassifier(max_depth=5, criterion='entropy', random_state=0)

# Perform cross-validation with 10 folds
scores = cross_val_score(modelDT, X, y, cv=10)

# Print the cross-validation scores
print("Cross-validation scores:", scores)

# Calculate the mean and standard deviation of the cross-validation scores
mean_score = scores.mean()
std_score = scores.std()

print("Mean score: {:.3f}".format(mean_score))
print("Standard deviation: {:.3f}".format(std_score))
