
# coding: utf-8

# In[41]:


import pandas as pd
from pylab import rcParams
import seaborn as sns 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[42]:


df = pd.read_csv("/Users/meganpolak/Desktop/Dem_CSV.csv")


# In[43]:


# Q1 how many men and women are represented in the dataset?
df['sex'].value_counts()


# In[44]:


# Q2 what is the avarage age of women ?

columns_to_show=['sex','age']
print("\n\n Avarage age for Female is 36 ")
df.groupby(['sex'])[columns_to_show].describe(percentiles=[])


# In[45]:


# Q3
print("All nationalities:")
print(df.native_country.unique())

germans = df.loc[df['native_country'] == " Germany"].shape[0]
print("\nNo. of Germans:" ,germans)
tot = df.shape[0]
print("Percentage of Germans:",germans/tot*100)


# In[46]:


# Q4 & Q5 mean and standard diviation of age more then 50k and less then 50 K 


columns_to_show=['salary','age']
print("\n\n Age mean and std for people that earn <= 50k is 36.78 and 14.02 ")
print("\n\n Age mean and std for people that ern >50k is 44.2 and 10.51 ")
df.groupby(['salary'])[columns_to_show].describe(percentiles=[])


# In[49]:


# Q4 population histagram of peoples's education 
rcParams['figure.figsize']=20,7
pl=sns.countplot(x='education', data=df)
plt.show()


# In[48]:


# Q6

print("All nationalities:")
print(df.education.unique())

df_highsalary = df[df.salary == ' >50K']
print("\nNo. of high income people:",df_highsalary.shape[0])

cnt = df_highsalary[(df['education'] == ' Bachelors') | (df['education'] == '  Prof-school') | (df['education'] == '  Assoc-acdm') | (df['education'] == '  Masters') | (df['education'] == ' Doctorate')].shape[0]
print("\nNo. of people with atleast high school education with high salary:",cnt)

print("It is not true that all high salary have atleast high school education")


# In[7]:


# Q7

print("All Races:")
print(df.race.unique())

max_age = df[(df['race'] == ' Amer-Indian-Eskimo') & (df['sex'] == ' Male')]['age'].max()
print("\nMaximum age of men of Amer-Indian-Eskimo race:",max_age)


# In[8]:


#Q8

print("Marital Statuses:")
print(df.marital_status.unique())


x = df_highsalary[((df_highsalary['marital_status'] ==' Married-civ-spouse') | (df['marital_status'] ==' Married-spouse-absent') | (df['marital_status'] ==' Married-AF-spouse')) & (df['sex'] == ' Male')].shape[0]
y = df_highsalary[df['sex'] == ' Male'].shape[0] - x



print("\nNo. of married high salary men:",x)
print("Proportion of married high salary men:",x/(x+y))

print("\nNo. of single high salary men:",y)
print("Proportion of single high salary men:",y/(x+y))

print("\n\nClearly proportion of married high salary men is greater")


# In[9]:


# Q9

max_work = df.hours_per_week.max()

print("The maximum number of hours a person works per week:",max_work)

df_maxwork = df[df.hours_per_week == max_work]
print("No. of people work such a number of hours:" ,df_maxwork.shape[0])

print()
x = df_maxwork[df.salary == ' >50K'].shape[0]
print("The number of those who earn a lot (>50K) among them:" ,x )
print("The percentage of those who earn a lot (>50K) among them:" ,x/df_maxwork.shape[0]*100)


# In[10]:


# Q10

for country in df['native_country'].unique():
    if country == ' ?':
        continue
    df_country = df[df.native_country == country]
    x = df_country[df_country.salary == ' <=50K']['hours_per_week']
    y = df_country[df_country.salary == ' >50K']['hours_per_week']

    print("Average work hours for",country, " for those who earn a little:",x.mean())
    print("Average work hours for",country, " for those who earn a lot:",y.mean())
    print()
    
country = ' Japan'
df_country = df[df.native_country == country]
x = df_country[df_country.salary == ' <=50K']['hours_per_week']
y = df_country[df_country.salary == ' >50K']['hours_per_week']

print("\n\nFor Japan:")
print("Average work hours for those who earn a little:",x.mean())
print("Average work hours for those who earn a lot:",y.mean())

