import pandas as pd
import scipy.stats as stats

# Load the data and select the relevant columns
data = pd.read_csv("finaldrugdataset.csv")
df = data
# Combine the drug use columns into a single column

# Create a contingency table
cont_table = pd.crosstab(df["Education"], df["DrugUse"])

# Perform the chi-square test
chi2, p, dof, expected = stats.chi2_contingency(cont_table)

# Print the results
print("Chi-square test results:")
print(f"Chi-square score: {chi2:.2f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)

#________________________________________________________________
# Create a contingency table
cont_table = pd.crosstab(df["Age"], df["DrugUse"])

# Perform the chi-square test
chi2, p, dof, expected = stats.chi2_contingency(cont_table)

# Print the results
print("Chi-square test results:")
print(f"Chi-square score: {chi2:.2f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)

####_____________________________________________________________
data = pd.read_csv("finaldrugdataset.csv")

cont_table = pd.crosstab(df["Nscore"], df["DrugUse"])

# Perform the chi-square test
chi2, p, dof, expected = stats.chi2_contingency(cont_table)

# Print the results
print("Chi-square test results for NScore and Drug Use:")
print(f"Chi-square score: {chi2:.2f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)

#_________________________________________________________________________
data = pd.read_csv("finaldrugdataset.csv")

cont_table = pd.crosstab(df["Escore"], df["DrugUse"])

# Perform the chi-square test
chi2, p, dof, expected = stats.chi2_contingency(cont_table)

# Print the results
print("Chi-square test results for EScore and Drug Use:")
print(f"Chi-square score: {chi2:.2f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)
#_______________________________________________________________________________

data = pd.read_csv("finaldrugdataset.csv")

cont_table = pd.crosstab(df["Ascore"], df["DrugUse"])

# Perform the chi-square test
chi2, p, dof, expected = stats.chi2_contingency(cont_table)

# Print the results
print("Chi-square test results for AScore and Drug Use:")
print(f"Chi-square score: {chi2:.2f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)

#______________________________________________
data = pd.read_csv("finaldrugdataset.csv")

cont_table = pd.crosstab(df["Gender"], df["DrugUse"])

# Perform the chi-square test
chi2, p, dof, expected = stats.chi2_contingency(cont_table)

# Print the results
print("Chi-square test results for Gender and Drug Use:")
print(f"Chi-square score: {chi2:.2f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)
#___________________________________________________________________

cont_table = pd.crosstab(df["SS"], df["DrugUse"])

# Perform the chi-square test
chi2, p, dof, expected = stats.chi2_contingency(cont_table)

# Print the results
print("Chi-square test results for SS and Drug Use:")
print(f"Chi-square score: {chi2:.2f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)

#___________________________________________________________________

cont_table = pd.crosstab(df["Impulsive"], df["DrugUse"])

# Perform the chi-square test
chi2, p, dof, expected = stats.chi2_contingency(cont_table)

# Print the results
print("Chi-square test results for Impulsive and Drug Use:")
print(f"Chi-square score: {chi2:.2f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)

#___________________________________________________________________

cont_table = pd.crosstab(df["Cscore"], df["DrugUse"])

# Perform the chi-square test
chi2, p, dof, expected = stats.chi2_contingency(cont_table)

# Print the results
print("Chi-square test results for CScore and Drug Use:")
print(f"Chi-square score: {chi2:.2f}")
print(f"P-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("Expected frequencies:")
print(expected)