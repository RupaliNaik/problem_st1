#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error


# In[2]:


df=pd.read_csv("C:/Users/Icon/Downloads/datascience-intern-main/housing_data.csv")


# In[3]:


df


# In[4]:


df.head(5)


# In[5]:


df.isna().sum()


# In[6]:


df.info()


# In[7]:


df.columns


# In[8]:


#Apply feature engineering
from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()
df[' Location']=label_encoder.fit_transform(df[' Location'])


# In[9]:


df.info()


# In[10]:


df.corr()


# In[11]:


#split data
x=df.drop(columns=[" SalePrice"])
y=df[" SalePrice"]


# In[12]:


x.shape


# In[13]:


y.shape


# In[14]:


#split data

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=0)


# In[15]:


#Build Model
from sklearn.ensemble import RandomForestClassifier
model1=RandomForestClassifier().fit(x_train,y_train)
prediction=model1.predict(x_test)
prediction


# In[16]:


#model Evaluation Technique
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
print(confusion_matrix(y_test,prediction))
print(accuracy_score(y_test,prediction))
print(classification_report(y_test,prediction))


# In[17]:


#root mean squared error (RMSE) 
y_pred=model1.predict(x_test)
score=model1.score(x_test,y_test)
mse=mean_squared_error(y_test,y_pred)
print("R2:{0:.3f},MSE:{1:.2f},RMSE:{2:.2f}".format(score,mse,np.sqrt(mse)))


# In[ ]:




