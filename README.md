# Drug-Consumption-Analysis

**Data Description**

The Drug Consumption (Quantified) dataset is a collection of data from a survey of 1885 individuals, which includes information about the respondents' drug consumption and personality traits. The dataset contains 19 columns, including 12 attributes that measure personality traits. 
The dataset also includes information on the respondents' drug consumption habits, where participants were asked about their use of 18 drugs, including alcohol, cannabis, cocaine, nicotine, and heroin, as well as a fictitious drug called Semeron. Respondents were asked to report the frequency of their drug use.

**Data Plan**

This project was a team effort towards finding the relationship between drug addiction, personality traits, and other demographic information. The team will use a comprehensive outline for the approach and methodology involved in collecting, processing, cleaning, transforming, analyzing and presenting data to ensure that the project is well organized, transparent and reproducible, using the steps involved in the process of Data Analytics as an outline. 

**Data collection**

The data was obtained from the UCI Machine Learning Repository at: https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29. The data was collected through a survey where participants were asked to provide information about their personality, demographic information, and drug use habits.

**Data preprocessing**

The data was extracted in a form where the datasets were already quantified, which made preprocessing easier. We dropped the first column “ID” as we felt that it would not be useful in our data analysis. Those who claimed to have used Semeron are presumed to be over-claimants because it is not a legitimate drug. We will exclude these people who replied to anything other than CL0 for Semeron from the data frame since we can't be certain that their accounts of their drug use are true. We have also dropped the Semeron column.

**Data cleaning/integration**

We checked for duplicate records, missing values, inconsistent values, outliers and duplicate rows. We found no null values, and duplicate records. Additionally we found mild outliers but decided to keep them since they seemed to be a result of natural variance. We also wanted to remove Chocolate, Caffeine and Alcohol columns but decided to keep them and find any possible relationship between them and other attributes in our initial proposal.

**Data exploration**

Several graphs and matrices were made to determine significant relations between different attributes. 

**Learning the application domain**
Learning the application domain involves gaining a deep understanding of the drug use context in which the data analysis is being conducted. No one on the team is familiar with any of these drugs as well as the individual personality traits. We had to understand them to make it easier to work with our data.

**Modeling or Extracting patterns/knowledge**

Once the data had been cleaned, processed, and explored, the next step was to develop machine learning models to predict the relationship between the likelihood of drug addiction among all other factors. This may involved using techniques such as decision trees, random forests, logistic regression etc. to extract patterns or knowledge from the data. The models were also compared to identify the best performing model.

**Model evaluation**

Model evaluation involves assessing the performance of the machine learning models developed in step 6. We will use model evaluation to compare the performance of the model we have chosen to identify the best-performing model in terms of evaluate the model's accuracy, precision, recall, and other metrics.

**Knowledge presentation**

In this final step, we present the results of the data analysis in a way that is easily understandable through creating data visualizations, dashboards, and reports that summarize the key findings of the analysis



**Full Project Plan**

The Drug Consumption (Quantified) dataset is a collection of data from a survey of 1885 individuals, which includes information about the respondents' drug consumption and personality traits. For each respondent, 12 attributes are known: Personality measurements which include:
NEO-FFI-R (neuroticism, extraversion, openness to experience, agreeableness, and conscientiousness)
BIS-11 (impulsivity)
ImpSS (sensation seeking)
Level of education
Age
Gender
Country of residence 
Ethnicity. 
Participants were also questioned concerning their use of 18 legal and illegal drugs (alcohol, amphetamines, amyl nitrite, benzodiazepine, cannabis, chocolate, cocaine, caffeine, crack, ecstasy, heroin, ketamine, legal highs, LSD, methadone, mushrooms, nicotine and volatile substance abuse and one fictitious drug (Semeron) which was introduced to identify over-claimers. For each drug they have to select one of the answers: never used the drug, used it over a decade ago, or in the last decade, year, month, week, or day. 
The team will attempt to approach the problem by considering a union of the respondents' answers and classify them into a binary classification as  “user” and “non-user.” "Never Used", and "Used over a Decade Ago" will form a class "Non-user" and all other classes will form a class "User".


**Motivation**
Drug use does not happen in isolation and there are several contributing factors that influence drug use and addiction. We were motivated to choose the dataset to prove our hypothesis that aims to find the correlation between personality traits, impulsivity, sensation seeking, and drug use. We wanted to use the dataset to develop insights into drug use patterns and understand more about how individuals with certain personality traits are addicted to certain drugs. In a broader context, we wanted to use predictive analytics because we believe that our project can inform decision-making in real-world scenarios such as healthcare that can be used to develop targeted interventions or public health campaigns. We also wanted to be able to identify potential risk factors which will help identify the individuals who are at higher risk of developing a drug addiction. 

**Problem Definition**
The goal was to to build a model that will predict the likelihood of drug addiction based on, based on their personality traits and other deomgraphic data. 

**Data Analysis**
Before we embarked on choosing which algorithms would best suit our data set, we first had to do the following:

Preprocess data: Previously in our proposal, we preprocessed the data by identifying and removing null values (which were not existent in the data set). We removed the column “ID” which we felt like was not necessary to keep in the dataset as it did not have any actual value. We also removed rows that responded to anything other than “CL0” for a fictitious drug called Semeron, as we felt that those responses were not honest and it is not possible to feel any effect from a placebo drug. Here, we preprocessed the data further by categorizing all the responses into user and non-user by assigning values “1” as user and “0” as non-user. The data now reflects the classification problem we aim to solve.
