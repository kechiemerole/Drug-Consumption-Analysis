# Import necessary libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd
from sklearn.model_selection import train_test_split


import matplotlib.pyplot as plt


# Load the data into a pandas dataframe
data = pd.read_csv('finaldrugdataset.csv')


# Select the independent variables
X = data[['Age', 'Gender','Education', 'Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'SS', 'Impulsive']]

# Select the dependent variable
y = data['DrugUse']


# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Balance the data using RandomUnderSampler
rus = RandomUnderSampler(random_state=0)
X_resampled, y_resampled = rus.fit_resample(X, y)

# Fit a logistic regression model to the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the performance of the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')

weights = pd.Series(model.coef_[0], index=X.columns.values) # Stores all important features for later use


plt.ylabel('Feature importances') # Set ylabel
plt.suptitle('Logistic regression') # set title
weights.sort_values(ascending = True)[-10:].plot(kind='barh') # Plotting of the top 10 features
plt.show() # Show graph

#_________________________________________________________________
#Logistic regression ROC curve
# Plot the ROC curve
from sklearn.metrics import roc_curve, auc

# Get predicted probabilities for the test data
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Calculate the false positive rate, true positive rate, and threshold for each threshold
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)

# Calculate the area under the curve (AUC)
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()


#_____________________________________________________________

# Evaluate the performance of the model of the subset feature selection of the logistic model

# Load the data into a pandas dataframe
data = pd.read_csv('finaldrugdataset.csv')


# Select the independent variables
X = data[['Age', 'Oscore', 'SS', ]]

# Select the dependent variable
y = data['DrugUse']


# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# oversample the training data using RandomOverSampler
oversample = RandomOverSampler(sampling_strategy='minority')
X_train_over, y_train_over = oversample.fit_resample(X_train, y_train)

# Fit a logistic regression model to the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the performance of the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f'Subset Accuracy: {accuracy}')
print(f'Subset Precision: {precision}')
print(f'Subset Recall: {recall}')
print(f'Subset F1 Score: {f1}')


weights = pd.Series(model.coef_[0], index=X.columns.values) # Stores all important features for later use


plt.ylabel('Feature importances') # Set ylabel
plt.suptitle('Logistic regression subset selection') # set title
weights.sort_values(ascending = True)[-10:].plot(kind='barh') # Plotting of the top features
plt.show() # Show graph

#_________________________________________________________________________________________
# create a box plot of age and drug use
sns.boxplot(x='DrugUse', y='Age', data=data)

# set the labels
plt.xlabel('Drug use')
plt.ylabel('Age')

# show the plot
plt.show()

#______________________________________________________________________________________________________________________
#ROC curve feature subset 
from sklearn.metrics import roc_curve, roc_auc_score

# Compute the predicted probabilities of the model on the test set
y_proba = model.predict_proba(X_test)[:, 1]

# Compute the false positive rate, true positive rate and thresholds of the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_proba)

# Compute the AUC score of the ROC curve
auc_score = roc_auc_score(y_test, y_proba)

# Plot the ROC curve
plt.plot(fpr, tpr, label=f'AUC = {auc_score:.2f}')
plt.plot([0, 1], [0, 1], linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show()
