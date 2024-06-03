#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score , mean_absolute_error


# In[56]:


df = pd.read_csv('car data.csv')
df.head(10)


# In[57]:


df.info()


# In[58]:


df.describe().style.format(precision=2).background_gradient(cmap='RdBu')


# In[59]:


# Data types of columns
print(" Data types of columns:")
print(df.dtypes)


# In[60]:


# drop duplicate values
df = df.drop_duplicates()
df.duplicated().sum()


# In[61]:


numerical_features = ['Year', 'Driven_kms', 'Selling_Price', 'Present_Price']
for feature in numerical_features:
    plt.figure(figsize=(10, 6))
    sns.displot(data=df, x=feature, kde=True)
    plt.title(f'Distribution of {feature}')
    plt.show()


# In[62]:


# Select numerical columns
numerical_columns = ['Year', 'Selling_Price', 'Present_Price', 'Driven_kms', 'Owner']

# Create a DataFrame containing only the numerical columns
numerical_df = df[numerical_columns]

# Calculate the correlation matrix
correlation_matrix = numerical_df.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".3f")
plt.title('Correlation Heatmap')
plt.show()


# In[63]:


print(df['Fuel_Type'].value_counts())


# In[64]:


# encoding Columns
df.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}},inplace=True)

df.replace({'Selling_type':{'Dealer':0,'Individual':1}},inplace=True)

df.replace({'Transmission':{'Manual':0,'Automatic':1}},inplace=True)

df.head(10)


# In[72]:


# Feature and target variable
X = df.drop(['Car_Name','Selling_Price'], axis=1)
y = df['Selling_Price']

X


# In[66]:


# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[67]:


model = LinearRegression()
model.fit(X_train,y_train)


# In[68]:


# Evaluate the model
y_pred = model.predict(X_test)


# In[69]:


# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print(f'MAE: {mae}')
print(f'RMSE: {rmse}')


# In[79]:


# Testing model prediction
new_car = [[2014, 6.87 , 42450 , 1, 0, 0, 0 ]]
predicted_price = model.predict(new_car)
print('Predicted Selling Price:', predicted_price[0])

