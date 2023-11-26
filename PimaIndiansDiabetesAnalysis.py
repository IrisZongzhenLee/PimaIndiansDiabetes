#!/usr/bin/env python
# coding: utf-8

# # Foundations of Data Science Project - Diabetes Analysis
# 
# ---------------
# ## Context
# ---------------
# 
# Diabetes is one of the most frequent diseases worldwide and the number of diabetic patients are growing over the years. The main cause of diabetes remains unknown, yet scientists believe that both genetic factors and environmental lifestyle play a major role in diabetes.
# 
# A few years ago research was done on a tribe in America which is called the Pima tribe (also known as the Pima Indians). In this tribe, it was found that the ladies are prone to diabetes very early. Several constraints were placed on the selection of these instances from a larger database. In particular, all patients were females at least 21 years old of Pima Indian heritage. 
# 
# -----------------
# ## Objective
# -----------------
# 
# Here, we are analyzing different aspects of Diabetes in the Pima Indians tribe by doing Exploratory Data Analysis.
# 
# -------------------------
# ## Data Dictionary
# -------------------------
# 
# The dataset has the following information:
# 
# * Pregnancies: Number of times pregnant
# * Glucose: Plasma glucose concentration over 2 hours in an oral glucose tolerance test
# * BloodPressure: Diastolic blood pressure (mm Hg)
# * SkinThickness: Triceps skin fold thickness (mm)
# * Insulin: 2-Hour serum insulin (mu U/ml)
# * BMI: Body mass index (weight in kg/(height in m)^2)
# * DiabetesPedigreeFunction: A function that scores the likelihood of diabetes based on family history.
# * Age: Age in years
# * Outcome: Class variable (0: a person is not diabetic or 1: a person is diabetic)

# ## Q 1: Import the necessary libraries and briefly explain the use of each library (3 Marks)

# In[5]:


# remove _____ & write the appropriate library name

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# #### Write your Answer here: 
Ans 1:
a) numpy - a library stands for numerical python; used for data computation 
b) matplotlib.pyplot - matplotlib is a library for 2D plotting; pyplot is the most common package that is simply and generate in less time
# ## Q 2: Read the given dataset (1 Mark)

# In[15]:


# remove _____ & write the appropriate function name

pima = pd.read_csv("diabetes.csv")


# ## Q3. Show the last 10 records of the dataset. How many columns are there? (1 Mark)

# In[23]:


# remove ______ and write the appropriate number in the function

pima.tail(10)


# #### Write your Answer here: 
# 
Ans 3: 9 columns; code - pima.info()
# ## Q4. Show the first 10 records of the dataset (1 Mark)

# In[25]:


# remove _____ & write the appropriate function name and the number of rows to get in the output

pima.head(10)


# ## Q5. What do you understand by the dimension of the dataset? Find the dimension of the `pima` dataframe. (1 Mark)

# In[28]:


# remove _____ & write the appropriate function name

pima.shape


# #### Write your Answer here: 
# 
Ans 5: There are 9 variables relating to aspects of diabetes, and 768 participants who are female at least 21 years old from the Indian pima hertiage.
# ## Q6. What do you understand by the size of the dataset? Find the size of the `pima` dataframe. (1 Mark)

# In[31]:


# remove _____ & write the appropriate function name

pima.size


# #### Write your Answer here: 
# 
Ans 6: the pima dataframe has 6912 entries.
# ## Q7. What are the data types of all the variables in the data set? (2 Marks)
# **Hint: Use the info() function to get all the information about the dataset.**

# In[33]:


# remove _____ & write the appropriate function name

pima.info()


# #### Write your Answer here: 
# 
Ans 7:
 0   Pregnancies               768 non-null    int64  
 1   Glucose                   768 non-null    int64  
 2   BloodPressure             768 non-null    int64  
 3   SkinThickness             768 non-null    int64  
 4   Insulin                   768 non-null    int64  
 5   BMI                       768 non-null    float64
 6   DiabetesPedigreeFunction  768 non-null    float64
 7   Age                       768 non-null    int64  
 8   Outcome                   768 non-null    int64  
# ## Q8. What do we mean by missing values? Are there any missing values in the `pima` dataframe? (2 Marks)

# In[38]:


# remove _____ & write the appropriate function name

pima.isnull().values.any()


# #### Write your Answer here: 
# 
Ans 8: Missing values is equivalent to entries that are null. pima dataframe doesn't contain any missing values
# ## Q9. What do the summary statistics of the data represent? Find the summary statistics for all variables except 'Outcome' in the `pima` data. Take one column/variable from the output table and explain all its statistical measures. (3 Marks)

# In[40]:


# remove _____ & write the appropriate function name

pima.iloc[:,0:8].describe()


# #### Write your Answer here: 
# 
Ans 9: The numpy summary statistics provide count, mean, std, min, 25%,median,75% percentile, and max. For example, for the age column, out of 768 participants, the average age is 33.24 with 11.76 standard deviation; minimum age of 21 and first quartile of 24, median of 29, third quartile of 41 and maximum age of 81. 
# ## Q 10. Plot the distribution plot for the variable 'BloodPressure'. Write detailed observations from the plot. (2 Marks)

# In[41]:


# remove _____ & write the appropriate library name

sns.displot(pima['BloodPressure'], kind='kde')
plt.show()


# #### Write your Answer here: 
# 
Ans 10: The distribution is bell shape close to a normal distribution with mean around 70. The y axis tells the percentage composition of the participants with the corresponding blood pressure.
# ## Q 11. What is the 'BMI' of the person having the highest 'Glucose'? (1 Mark)

# In[44]:


# remove _____ & write the appropriate function name

pima[pima['Glucose']==pima['Glucose'].max()]['BMI']


# #### Write your Answer here: 
# 
Ans 11: BMI is 42.9 for the person having the highest glucose level
# ## Q12.
# ### 12.1 What is the mean of the variable 'BMI'? 
# ### 12.2 What is the median of the variable 'BMI'? 
# ### 12.3 What is the mode of the variable 'BMI'?
# ### 12.4 Are the three measures of central tendency equal?
# 
# ### (3 Marks)

# In[45]:


# remove _____ & write the appropriate function name

m1 = pima['BMI'].mean()  # mean
print(m1)
m2 = pima['BMI'].median()  # median
print(m2)
m3 = pima['BMI'].mode()[0]  # mode
print(m3)


# #### Write your Answer here: 
# 
Ans 12: No, the mean (32.45) of the BMI is higher than the median and mode thara are 32.
# ## Q13. How many women's 'Glucose' levels are above the mean level of 'Glucose'? (1 Mark)

# In[48]:


# remove _____ & write the appropriate function name

pima[pima['Glucose']>pima['Glucose'].mean()].shape[0]


# #### Write your Answer here: 
# 
Ans 13: 343 women have their glucose levels are above the mean level of glucose
# ## Q14. How many women have their 'BloodPressure' equal to the median of 'BloodPressure' and their 'BMI' less than the median of 'BMI'? (2 Marks)

# In[50]:


# remove _____ & write the appropriate column name

pima[(pima['BloodPressure']==pima['BloodPressure'].median()) & (pima['BMI']<pima['BMI'].median())].shape[0]


# #### Write your Answer here: 
# 
Ans 14: 22 women have their blood pressure equal to the median of blood pressure and BMI less than the median of BMI
# ## Q15. Create a pairplot for the variables 'Glucose', 'SkinThickness', and 'DiabetesPedigreeFunction'. Write your observations from the plot. (4 Marks)

# In[52]:


# remove _____ & write the appropriate function name

sns.pairplot(data=pima,vars=['Glucose', 'SkinThickness', 'DiabetesPedigreeFunction'], hue='Outcome')
plt.show()


# #### Write your Answer here: 
# 
Ans 15: the diagonals provide the univaraite distributions of the corresponding variable. The higher level of glucose tend to be diabetics against skin thickness and dianbetes pedigree function. variables are not very correlated
# ## Q16. Plot the scatterplot between 'Glucose' and 'Insulin'. Write your observations from the plot. (2 Marks)

# In[53]:


# remove _____ & write the appropriate function name

sns.scatterplot(x='Glucose',y='Insulin',data=pima)
plt.show()


# #### Write your Answer here: 
# 
Ans 16: slight positive correlation between the glucose and insulin level
# ## Q 17. Plot the boxplot for the 'Age' variable. Are there outliers? (2 Marks)

# In[54]:


# remove _____ & write the appropriate function and column name 

plt.boxplot(pima['Age'])

plt.title('Boxplot of Age')
plt.ylabel('Age')
plt.show()


# #### Write your Answer here: 
# 
Ans 17: Yes there are a few outliers
# ## Q18. Plot histograms for the 'Age' variable to understand the number of women in different age groups given whether they have diabetes or not. Explain both histograms and compare them. (3 Marks)

# In[55]:


# remove _____ & write the appropriate function and column name

plt.hist(pima[pima['Outcome']==1]['Age'], bins = 5)
plt.title('Distribution of Age for Women who has Diabetes')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show() 


# In[56]:


# remove _____ & write the appropriate function and column name

plt.hist(pima[pima['Outcome']==0]['Age'], bins = 5)
plt.title('Distribution of Age for Women who do not have Diabetes')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# #### Write your Answer here: 
# 
Ans 18: Looking at the distribution of women who aren't diabetic, they are mostly young between 21 and 31. Compared to the distribution of women who are diabetic, the age range is wider.
# ## Q 19. What is the Interquartile Range of all the variables? Why is this used? Which plot visualizes the same? (2 Marks)

# In[58]:


# remove _____ & write the appropriate variable name

Q1 = pima.quantile(0.25)
Q3 = pima.quantile(0.75)
IQR = Q3 - Q1
print(IQR) 


# #### Write your Answer here: 
# 
Ans 19: Interquartile range tells the spread of the middle half of distribution. 
# ## Q 20. Find and visualize the correlation matrix. Write your observations from the plot. (3 Marks)

# In[61]:


# remove _____ & write the appropriate function name and run the code

corr_matrix = pima.iloc[:,0:8].corr()

corr_matrix


# In[62]:


# remove _____ & write the appropriate function name

plt.figure(figsize=(8,8))
sns.heatmap(corr_matrix, annot = True)

# display the plot
plt.show()

