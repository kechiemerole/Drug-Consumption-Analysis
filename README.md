# Drug-Consumption-Analysis

**Data Description**

The Drug Consumption (Quantified) dataset is a collection of data from a survey of 1885 individuals, which includes information about the respondents' drug consumption and personality traits. The dataset contains 19 columns, including 12 attributes that measure personality traits. 
The dataset also includes information on the respondents' drug consumption habits, where participants were asked about their use of 18 drugs, including alcohol, cannabis, cocaine, nicotine, and heroin, as well as a fictitious drug called Semeron. Respondents were asked to report the frequency of their drug use.

**Data Plan**

This project was an effort towards finding the relationship between drug addiction, personality traits, and other demographic information. The approach and methodology involved in collecting, processing, cleaning, transforming, analyzing and presenting data ensures that the project is well organized, transparent and reproducible, using the steps involved in the process of Data Analytics as an outline. 

**Data collection**

The data was obtained from the UCI Machine Learning Repository at: https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29. The data was collected through a survey where participants were asked to provide information about their personality, demographic information, and drug use habits.

**Data preprocessing**

The data was extracted in a form where the datasets were already quantified, which made preprocessing easier. The first column “ID” was dropped as I felt that it would not be useful in the data analysis. Those who claimed to have used Semeron are presumed to be over-claimants because it is not a legitimate drug. I excluded the people who replied to anything other than CL0 for Semeron from the data frame since it is not certain that their accounts of their drug use are true and hence the Semeron column has been dropped.

**Data cleaning/integration**

Duplicate records were checked, including missing values, inconsistent values, outliers and duplicate rows. No null values were found. Additionally, I found mild outliers but decided to keep them since they seemed to be a result of natural variance. I also wanted to remove the Chocolate, Caffeine and Alcohol columns but decided to keep them and find any possible relationship between them and other attributes in the initial proposal.

**Data exploration**

Several graphs and matrices were made to determine significant relationships between different attributes. 

**Learning the application domain**
Learning the application domain involves gaining a deep understanding of the drug use context in which the data analysis is being conducted. I am not familiar with any of these drugs as well as the individual personality traits. I had to understand them to make it easier to work with the data.

**Modeling or Extracting patterns/knowledge**

Once the data had been cleaned, processed, and explored, the next step was to develop machine learning models to predict the relationship between the likelihood of drug addiction among all other factors. This may involve using techniques such as decision trees, random forests, logistic regression etc. to extract patterns or knowledge from the data. The models were also compared to identify the best-performing model.

**Model evaluation**

Model evaluation involves assessing the performance of the machine learning models developed in step 6. I will use model evaluation to compare the performance of the model chosen to identify the best-performing model in terms of evaluating the model's accuracy, precision, recall, and other metrics.

**Knowledge presentation**

In this final step, the results of the data analysis will be presented in a way that is easily understandable by creating data visualizations, dashboards, and reports that summarize the key findings of the analysis



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
Participants were also questioned concerning their use of 18 legal and illegal drugs (alcohol, amphetamines, amyl nitrite, benzodiazepine, cannabis, chocolate, cocaine, caffeine, crack, ecstasy, heroin, ketamine, legal highs, LSD, methadone, mushrooms, nicotine and volatile substance abuse and one fictitious drug (Semeron) which was introduced to identify over-claimers. For each drug, they have to select one of the answers: never used the drug, used it over a decade ago, or in the last decade, year, month, week, or day. 
The team will attempt to approach the problem by considering a union of the respondents' answers and classify them into a binary classification as  “user” and “non-user.” "Never Used", and "Used over a Decade Ago" will form a class "Non-user" and all other classes will form a class "User".


**Motivation**
Drug use does not happen in isolation and there are several contributing factors that influence drug use and addiction. I was motivated to choose the dataset to prove the hypothesis that aims to find the correlation between personality traits, impulsivity, sensation seeking, and drug use. I wanted to use the dataset to develop insights into drug use patterns and understand more about how individuals with certain personality traits are addicted to certain drugs. In a broader context, I wanted to use predictive analytics because I believe that the project can inform decision-making in real-world scenarios such as healthcare that can be used to develop targeted interventions or public health campaigns. I also wanted to be able to identify potential risk factors which will help identify the individuals who are at higher risk of developing a drug addiction. 

**Problem Definition**
The goal was to build a model that will predict the likelihood of drug addiction based on, based on their personality traits and other demographic data. 

**Data Analysis**
Before I embarked on choosing which algorithms would best suit the data set, I first had to do the following:

Preprocess data: Previously in the proposal, I preprocessed the data by identifying and removing null values (which were not existent in the data set). I removed the column “ID” which I felt like was not necessary to keep in the dataset as it did not have any actual value. I also removed rows that responded to anything other than “CL0” for a fictitious drug called Semeron, as I felt that those responses were not honest and it is not possible to feel any effect from a placebo drug. Here, I preprocessed the data further by categorizing all the responses into user and non-user by assigning values “1” as user and “0” as non-user. The data now reflects the classification problem I aim to solve.

| Response | Response | Value | Class |
|----------|----------|-------|-------|
| 1. Never used     |  non-user | CL0   | 0     |
| 2. Used over a decade ago       |  non-user | CL1   | 0     |
| 3. Used in the last decade      |  user | CL2   | 1     |
| 4. Used in last year       |  user | CL3   | 1     |
| 5. Used in last month       |  user | CL4   | 1     |
| 6. Used in last week       |  user | CL5   | 1     |
| 7. Used in last day        |  user | CL6   | 1     |

I also decided to encode the data, since categorical variables like age, level of education, gender, country of residence, and ethnicity were already quantified in the original dataset. I have decided to give each value a code since the quantified values don’t have any actual meaning or use. This will help us to better understand the data and helps with the overall interpretability which I believe will improve the overall performance of the models
that will be used. Some of the categorical variables that have been encoded

Age
| Value   | Meaning   | Code |
|---------|-----------|------|
| -0.95197 | 18 - 24   | 0    |
| -0.07854 | 25 - 34   | 1    |
| 0.49788  | 35 - 44   | 2    |
| 1.09449  | 45 - 54   | 3    |
| 1.82213  | 55 - 64   | 4    |
| 2.59171  | 65+       | 5    |

Gender
| Value   | Meaning | Code |
|---------|---------|------|
| 0.48246 | Female  | 0    |
| -0.48246 | Male    | 1    |

Education
| Value   | Meaning                              | Code |
|---------|--------------------------------------|------|
| -2.43591 | Left School Before 16 years          | 0    |
| -1.73790 | Left School at 16 years              | 1    |
| -1.43719 | Left School at 17 years              | 2    |
| -1.22751 | Left School at 18 years              | 3    |
| -0.61113 | Some College, No Certificate Or Degree | 4    |
| -0.05921 | Professional Certificate/ Diploma    | 5    |
| 0.45468  | University Degree                     | 6    |
| 1.16365  | Masters Degree                        | 7    |
| 1.98437  | Doctorate Degree                      | 8    |

Country
| Value   | Meaning                | Code |
|---------|------------------------|------|
| -0.09765 | Australia              | 0    |
| 0.24923  | Canada                 | 1    |
| -0.46841 | New Zealand            | 2    |
| -0.28519 | Other                  | 3    |
| 0.21128  | Republic of Ireland    | 4    |
| 0.96082  | UK                     | 5    |
| -0.57009 | USA                    | 6    |

Ethnicity
| Value   | Meaning              | Code |
|---------|----------------------|------|
| -0.50212 | Asian                | 0    |
| -1.10702 | Black                | 1    |
| 1.90725  | Mixed-Black/Asian    | 2    |
| 0.12600  | Mixed-White/Asian    | 3    |
| -0.22166 | Mixed-White/Black    | 4    |
| 0.11440  | Other                | 5    |
| -0.31685 | White                | 6    |

There were limitations of this study since the collected sample was biased with respect to the general population, but it remained useful for risk evaluation. After encoding, I thought it was necessary to include visualizations of the categorical variables and I noticed the distribution of respondents has a higher population of white people. (I encoded white = 6). Since white people are dominant, I believe that correlating ethnicity with drug use will not give an accurate result and will not help out the classification issues in any way, hence this column was dropped. I also did the same with country, as there was not an even distribution with UK = “5” constituting a large proportion of the respondents.

![image](https://github.com/kechiemerole/Drug-Consumption-Analysis/assets/97633203/80049b7d-2d6e-471a-8f8c-bf3e69c6e0ae)

Since the motivation for the project is focused on drug prevention methods that can be implemented in healthcare policies to analyze and identify risks of drug addiction and use, the columns of the legal drugs: chocolate, caffeine, and alcohol, will be dropped, for the purity of the experiment and the focus put on illegal drugs.



The graph is a general overview of all the drugs in the dataset and their frequency of use.
![image](https://github.com/kechiemerole/Drug-Consumption-Analysis/assets/97633203/a38e9ad7-67b3-48d4-ac58-427d250b3394)
![image](https://github.com/kechiemerole/Drug-Consumption-Analysis/assets/97633203/872a6dd5-cd0b-427a-a13d-ff61b30cd66a)
According to the observations, people reduce using drugs as they grow older. 



### Chi-square Test:
Here, I aimed to identify the correlations between the features and target variable, using the chi-square test
of independence.
Hypothesis:
H0 - That the two categorical variables are independent of each other.
H1 - That the two categorical variables are dependent on each other.
Chi-square test on Education and Drug Use
I will draw the conclusions based on:
p < 0.05 — this means the two categorical variables are correlated.
p > 0.05 — this means the two categorical variables are not correlated.
Chi-square test results:
Chi-square statistic: 191.39
P-value: 0.0000
Degrees of freedom: 8
9
Using the table from https://www.mathsisfun.com/data/chi-square-table.html
With α set to be 0.05, and 8 degrees of freedom, the critical chi-square region is 15.51
As the calculated chi-square value (191.39) is greater than 15.51, it, therefore, falls in the rejection region, and
hence the null hypothesis is rejected and the alternate hypothesis is accepted. And since p < 0.05 — this means
the two categorical variables are correlated. I will perform the same chi-square test on other demographic
categorical variables to look for dependencies between them.

|              | Age     | Gender | Education | NScore | AScore |
|--------------|---------|--------|-----------|--------|--------|
| Chi-square   | 374.51  | 106.76 | 191.39    | 110.75 | 101.98 |
| P-value      | 0.0000  | 0.0000 | 0.0000    | 0.0000 | 0.0000 |
| Degrees of freedom | 5 | 1      | 8         | 48     | 40     |
| Critical Chi-square region | 11.07 | 3.841 | 15.51 | 65.17 | 55.75 |
| Correlation  | Yes     | Yes    | Yes       | Yes    | Yes    |

|              | Impulsive | SS     | CScore | OScore | EScore |
|--------------|-----------|--------|--------|--------|--------|
| Chi-square   | 180.38    | 369.63 | 215.78 | 110.75 | 49.84  |
| P-value      | 0.0000    | 0.0000 | 0.0000 | 0.0000 | 0.1620 |
| Degrees of freedom | 9   | 10     | 40     | 48     | 41     |
| Critical Chi-square region | 16.91 | 18.31 | 55.75 | 65.17 | 56.94 |
| Correlation  | Yes       | Yes    | Yes    | Yes    | Inconclusive |

For EScore, a Chi-square score of 49.84 with 41 degrees of freedom and a p-value of 0.1620 suggests that there
is not enough evidence to reject the null hypothesis that there is no significant association between the variables
being compared. In other words, the variables may be independent of each other. I have decided to still
include EScore in the predictions due to the evidence not being sufficient to accept the null hypothesis.
While visualizing the frequency distribution of the responses coded a 0 for non-user and 1 for users, I
realized that there is an uneven distribution between responses, which may make the data biased towards
non-users. I have decided to seek methods such as equal sampling or random sampling to balance the
distribution of drug frequency of use in the data set. Alternatively, I have also considered using a random
forest algorithm, which can handle imbalanced data sets more effectively.

![image](https://github.com/kechiemerole/Drug-Consumption-Analysis/assets/97633203/722d7dbf-13f7-4d48-89d9-8051ce75ea12)
![image](https://github.com/kechiemerole/Drug-Consumption-Analysis/assets/97633203/240c186f-63c6-4de1-919c-0004f10b2c47)


## Algorithms
While splitting the data into training and testing sets, I decided to use 40% of the data for training and 60% of
the data for testing.
Random Forest
While deciding on the best-fitting algorithm, I encountered class imbalance which occurs when the number of instances in one class is significantly higher or lower than in the other class. In this case, the number of drug users is much higher than the number of non-users, and this could affect the performance of some models that I was considering. In such cases, the model can become biased toward the majority class (drug users) and may struggle to correctly identify the minority class (non-user). This is because the model is trained on a dataset that is not representative of the population, and it may not have enough information to learn the patterns associated with the minority class. I am attempting to address this issue using an advanced machine learning algorithm such as random forest which is more robust to class imbalance. I was able to train the data to an accuracy of 81% in relation to the target variable “Drug Use” using 40% of the data for training and 60% for testing with an unlimited depth of 420 trees. After running the data through the algorithm, here are the
important features:
![image](https://github.com/kechiemerole/Drug-Consumption-Analysis/assets/97633203/9916ac32-e334-44cb-9a9f-97556a57654e)

The chart includes the 10 features that positively relate to Drug Use. Based on the results, I can see that Sensation seeking and Age are top contenders in their relationship to Drug Use. Sensation-seeking is a personality trait characterized by the tendency to seek out novel, intense, and exciting experiences. Individuals
with high levels of sensation seeking are often more willing to take risks and try new things it is no surprise that it is a top contender with openness to experience (OScore) as individuals high in openness to experience are more likely to seek out new experiences and sensations, and they are very similar personality traits and may enhance an individual's curiosity to explore and be adventurous, including experimenting with drugs.

Classification Report:
|           | Precision | Recall | F1-Score | Support |
|-----------|-----------|--------|----------|---------|
| 0         | 0.69      | 0.70   | 0.69     | 233     |
| 1         | 0.86      | 0.86   | 0.86     | 518     |
|-----------|-----------|--------|----------|---------|
| Accuracy  |      |        |       0.81    | 751     |
| Macro Avg | 0.78      | 0.78   | 0.78     | 751     |
| Weighted Avg | 0.81   | 0.81   | 0.81     | 751     |


Random forest evaluation metrics
1. Confusion matrix: This shows the number of correct and incorrect predictions made by the random forest algorithm
2. ROC Curve: The AUC ( Area under curve) suggests that the random forest algorithm has a good score
![image](https://github.com/kechiemerole/Drug-Consumption-Analysis/assets/97633203/c5dc35b4-044e-4d20-b729-da0c7ba5c6f5)

feature subset reduction
By using only the top most important features, I can simplify the model, reduce the dimensionality of the data, and improve the performance of the model by reducing overfitting. I will then use the reduced feature set to train and test a model, evaluate its performance, and compare it with the performance of the model using all the features. Below are the important features, the classification report and the results of the random forest algorithm.
Classification Report:
|           | Precision | Recall | F1-Score | Support |
|-----------|-----------|--------|----------|---------|
| 0         | 0.53      | 0.76   | 0.63     | 233     |
| 1         | 0.87      | 0.70   | 0.78     | 518     |
|-----------|-----------|--------|----------|---------|
| Accuracy  |     |        |      0.72      | 751     |
| Macro Avg | 0.70      | 0.73   | 0.70     | 751     |
| Weighted Avg | 0.76   | 0.72   | 0.73     | 751     |

In this case, the model has a higher precision for non-drug users (0.87) than drug users (0.53), which means that when the model predicts someone as a non-drug user, it is more likely to be correct than when it predicts someone as a drug user. The recall for non-drug users is 0.76, which means that the model correctly
identified 76% of non-drug users, while the recall for drug users is 0.70, which means that the model correctly identified 70% of drug users. The F1-score is a measure that balances precision and recall, with higher values indicating better overall performance. In this case, the F1-score for non-drug users is 0.63, and for drug users, it is 0.78. Overall, the model has an accuracy of 0.72, which means that it correctly classified 72% of all cases. In summary, these results suggest that the model has better performance in predicting non-drug users than drug users, but still has some room for improvement. I will consider different approaches to improve the model's performance, such as trying different algorithms.

![image](https://github.com/kechiemerole/Drug-Consumption-Analysis/assets/97633203/233f378b-f7bb-4aa0-b671-236c24a8adb3)

The features of relative importance with subset reduction still identify age and Sensation seeking as top
contenders.
![image](https://github.com/kechiemerole/Drug-Consumption-Analysis/assets/97633203/da051f0c-c308-4c45-ac8a-232bfa10e854)

Above is the ROC for the subsets of the random forest algorithm with 88% accuracy

