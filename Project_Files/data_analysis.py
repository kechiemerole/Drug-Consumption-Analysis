import matplotlib.pyplot as plt
import pandas as pd
 

#The dataset used is as a result of encoding the drugs and the demographic information
df = pd.read_csv('modified_drug_dataset.csv')


# Count the number of instances of each ethnicity
ethnicity_counts = df['Ethnicity'].value_counts()

# Plot a pie chart of the ethnicity data
plt.figure(figsize=(8,8))
plt.pie(ethnicity_counts.values, labels=ethnicity_counts.index, autopct='%1.1f%%')
plt.title('Ethnicity Distribution')
plt.show()
#___________________________________________________________________________________________________________________

# Plot a pie chart of the country data
Country_counts = df['Country'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(Country_counts.values, labels=Country_counts.index, autopct='%1.1f%%')
plt.title('Country Distribution')
plt.show()
#___________________________________________________________________________________________________________________


# Plot a pie chart of the gender data
gender_counts = df['Gender'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.show()
#___________________________________________________________________________________________________________________

# Plot a pie chart of the education data
edu_counts = df['Education'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(edu_counts.values, labels=edu_counts.index, autopct='%1.1f%%')
plt.title('Education Distribution')
plt.show()
#___________________________________________________________________________________________________________________
# # Plot the frequency distribution
# Load the data
data = pd.read_csv('new_drugconsumption_dataset.csv')

# Select the drug response columns
drug_responses = data.iloc[:, 10:]

# Categorize drug use into 1 and 0
drug_use = (drug_responses > 0).astype(int)

# Get the frequency of drug use
freq_data = drug_use.apply(pd.Series.value_counts)

# Plot the histogram
fig, ax = plt.subplots(figsize=(12, 6))
freq_data.T.plot(kind='bar', stacked=True, ax=ax)
plt.legend(["Non-User", "User"])
ax.set_xlabel('Drugs')
ax.set_ylabel('Number of Participants')
ax.set_title('Frequency Distribution of Drug Users')
plt.show()
#___________________________________________________________________________________________________________________


df = pd.read_csv('finaldrugdataset.csv')

# Create a histogram of drug users and non-users
plt.hist(df['DrugUse'], bins=2, rwidth=0.9, color='blue')

# Set the chart title and axes labels
plt.title('Drug Users vs Non-Users')
plt.xlabel('Drug Use')
plt.ylabel('Number of Participants')

# Set the x-axis tick labels
plt.xticks(range(2), ['Non-User', 'User'])

# Display the plot
plt.show()
#___________________________________________________________________________________________________________________
