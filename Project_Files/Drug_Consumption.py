import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv('drugconsumption.csv')
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Replace missing values with NaN
df = df.replace("", pd.NaT)

# Remove rows with missing values
df = df.dropna()

# dropping the column that is not needed in the data set which is ID

df.pop('ID')

print(df)
# Define the columns containing numerical values

# Define the name of the specific column to filter
column_name = 'Semer'

# Define the desired value to keep
desired_value = 'CL0'

# Use boolean indexing to select the rows with the desired value
mask = df[column_name] == desired_value

# Drop the rows with a value not equal to the desired value in the specified column
df = df[mask]

#Drop Semer
df.pop('Semer')
print(df)


# Replace CL0 and CL1 with 0, and the rest with 1
df.replace(to_replace=["CL0", "CL1"], value=0, inplace=True)
df.replace(to_replace=["CL2", "CL3", "CL4", "CL5", "CL6"], value=1, inplace=True)


#Decode column Age 

#'18-24' age -> 0
#'25-34' age -> 1
#'35-44' age -> 2
#'45-54' age -> 3
#'55-64' age -> 4
#'65+'   age -> 5

def changeAge(x):
    if (x == -0.95197):
        x = 0
    elif (x == -0.07854):
        x = 1
    elif (x == 0.49788):
        x = 2
    elif (x == 1.09449):
        x = 3
    elif (x == 1.82213):
        x = 4
    elif (x == 2.59171):
        x = 5
    return x

df['Age'] = df['Age'].map(changeAge)

#Decode Gender

# Female -> 0
# Male   -> 1

def changeGender(x):
    if (x == 0.48246 ):
        x = 0
    elif (x == -0.48246 ):
        x = 1
    return x

df['Gender'] = df['Gender'].map(changeGender)

#Decode Education

# Left school before 16 years                          -> 0
# Left school at 16 years                              -> 1
# Left school at 17 years                              -> 2
# Left school at 18 years                              -> 3
# Some college or university, no certificate or degree -> 4
# Professional certificate/ diploma                    -> 5
# University degree                                    -> 6
# Masters degree                                       -> 7
# Doctorate degree                                     -> 8

def changeEducation(x):
  
  if (x == -2.43591):
    x = 0
  elif (x == -1.73790):
    x = 1
  elif (x == -1.43719):
    x = 2
  elif (x == -1.22751):
    x = 3
  elif (x == -0.61113):
    x = 4
  elif (x == -0.05921):
    x = 5
  elif (x == 0.45468):
    x = 6
  elif (x == 1.16365):
    x = 7
  elif (x == 1.98437):
    x = 8
  return x

df['Education'] = df['Education'].map(changeEducation)

#Decode country

#Australia -> 0
#Canada    -> 1
#New Zealand->2
#Other     -> 3
#Republic of Ireland ->4
#UK         ->5
#USA        ->6

def changeCountry(x):
  
  if (x == -0.09765):
    x = 0
  elif (x == 0.24923):
    x = 1
  elif (x == -0.46841):
    x = 2
  elif (x == -0.28519):
    x = 3
  elif (x == 0.21128):
    x = 4
  elif (x == 0.96082):
    x = 5
  elif (x == -0.57009):
    x = 6
  return x

df['Country'] = df['Country'].map(changeCountry)

#Decode Ethnicity

#Asian  -> 0
#Black  -> 1
#Mixed-Black/Asian -> 2
#Mixed-White/Asian -> 3
#Mixed-White/Black -> 4
#Other             -> 5
#White             -> 6

def changeEthnicity(x):
  
  if (x == -0.50212):
    x = 0
  elif (x == -1.10702):
    x = 1
  elif (x == 1.90725):
    x = 2
  elif (x == 0.12600):
    x = 3
  elif (x == -0.22166):
    x = 4
  elif (x == 0.11440):
    x = 5
  elif (x == -0.31685):
    x = 6
  return x

df['Ethnicity'] = df['Ethnicity'].map(changeEthnicity)
print(df)

# Save the modified data to a new CSV file
df.to_csv("modified_drug_dataset.csv", index=False)

# dropping the Country and Ethnicity columns
df.pop('Country')
df.pop('Ethnicity')
df.pop('Alcohol')
df.pop('Caff')
df.pop('Choc')

# Save the modified data to a new CSV file
df.to_csv("new_drugconsumption_dataset.csv", index=False)


# Load the dataset into a pandas dataframe
data = pd.read_csv('new_drugconsumption_dataset.csv')

# Create a new column called "drug_user" that combines the drug use outcomes
# across all drugs. If any of the drug use outcomes are 1 (i.e. the person has
# used that drug), then the "drug_user" column will be set to 1. Otherwise, it
# will be set to 0.
data['DrugUse'] = (data.iloc[:, 13:20] == 1).any(axis=1).astype(int)

# Drop the original drug use outcome columns, since they are no longer needed
data = data.drop(columns=['Amphet', 'Amyl', 'Benzos','Cannabis',
                           'Coke', 'Crack', 'Ecstasy', 'Heroin',
                          'Ketamine', 'Legalh', 'LSD', 'Meth', 'Mushroom',
                          'Nicotine', 'VSA'])
print(data)
data.to_csv('finaldrugdataset.csv', index=False)

