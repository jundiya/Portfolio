#Import required libraries
import pandas as pd
pd.options.display.max_columns=50

#Read the dataset into pandas dataframe
#Values is separated by semicolon
retail = pd.read_csv(r'D:/Python/DQLAB/Data Analyst Project_Business Decision Research/data_retail.csv', sep=';')

#Inspection data
print(retail.head())
print(retail.info())

#Convert dates to datetime format
retail['First_Transaction']=pd.to_datetime(retail['First_Transaction']/1000, unit='s', origin='1970-01-01')
retail['Last_Transaction']=pd.to_datetime(retail['Last_Transaction']/1000, unit='s', origin='1970-01-01')
print(retail.head())

#Check the last transaction date
print(retail['Last_Transaction'].max())

#Classify the customer churn with boolean
retail.loc[retail['Last_Transaction']<='2018-08-01','is_churn']=True
retail.loc[retail['Last_Transaction']>'2018-08-01','is_churn']=False
print(retail.head())
print(retail.info())
print(retail['is_churn'].value_counts())

#Delete unnecessary column
del retail['no']
del retail['Row_Num']

import matplotlib.pyplot as plt
import seaborn as sns
#Visualization of customer acquisition by year
retail['Year_First_Transaction']=retail['First_Transaction'].dt.year
retail['Year_Last_Transaction']=retail['Last_Transaction'].dt.year
print(retail.head())

customer_year=retail.groupby(['Year_First_Transaction'])['Customer_ID'].count()
customer_year.plot(x='Year_First_Transaction', y='Customer_ID', kind='bar',
    title='Graph of Customer Acquisition by Year')
plt.xlabel('Year of First Transaction')
plt.ylabel('Number of Customer')
plt.tight_layout()
plt.show()

#Visualization of customer transaction by year
transaction_year=retail.groupby(['Year_First_Transaction'])['Count_Transaction'].sum()
transaction_year.plot(x='Year_First_Transaction', y='Count_Transaction', kind='bar',
    title='Graph of Customer Transaction by Year')
plt.xlabel('Year of First Transaction')
plt.ylabel('Number of Transaction')
plt.tight_layout()
plt.show()

#Visualization of average transaction amount by year
sns.pointplot(data=retail.groupby(['Year_First_Transaction', 'Product']).mean().reset_index(),
    x='Year_First_Transaction',
    y='Average_Transaction_Amount',
    hue='Product')
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xlabel('Year of First Transaction')
plt.ylabel('Average Transaction Amount')
plt.tight_layout()
plt.show()

#Pivot table
retail_piv=retail.pivot_table(index='is_churn', columns='Product', values='Customer_ID', aggfunc='count', fill_value=0)
print(retail_piv)

#Visualization of churn proportion by product
retail_piv.plot.pie(subplots=True, figsize=(10,7), layout=(-1,2), autopct='%1.0f%%', title='Churn Proportion by Product')
plt.tight_layout()
plt.show()

#Classify the count of transaction
def func(row):
    if row['Count_Transaction']==1:
        val='1.1'
    elif (row['Count_Transaction']>1 and row['Count_Transaction']<=3):
        val='2.2-3'
    elif (row['Count_Transaction']>3 and row['Count_Transaction']<=6):
        val='3.4-6'
    elif (row['Count_Transaction']>6 and row['Count_Transaction']<=10):
        val='4.7-10'
    else:
        val='5.>10'
    return val

retail['Count_Transaction_Group']=retail.apply(func, axis=1)

#Visualization of customer distribution by count transaction group
customer_transaction=retail.groupby(['Count_Transaction_Group'])['Customer_ID'].count()
customer_transaction.plot(x='Count_Transaction_Group', y='Customer_ID', kind='bar',
    title='Customer Distribution by Count Transaction Group')
plt.xlabel('Count Transaction Group')
plt.ylabel('Number of Customer')
plt.tight_layout()
plt.show()

#Classify the average of transaction amount
def f(row):
    if (row['Average_Transaction_Amount']>= 100000 and row['Average_Transaction_Amount'] <=200000):
        val ='1. 100.000 - 250.000'
    elif (row['Average_Transaction_Amount']>250000 and row['Average_Transaction_Amount']<=500000):
        val ='2. >250.000 - 500.000'
    elif (row['Average_Transaction_Amount']>500000 and row['Average_Transaction_Amount']<=750000):
        val ='3. >500.000 - 750.000'
    elif (row['Average_Transaction_Amount']>750000 and row['Average_Transaction_Amount']<=1000000):
        val ='4. >750.000 - 1.000.000'
    elif (row['Average_Transaction_Amount']>1000000 and row['Average_Transaction_Amount']<=2500000):
        val ='5. >1.000.000 - 2.500.000'
    elif (row['Average_Transaction_Amount']>2500000 and row['Average_Transaction_Amount']<=5000000):
        val ='6. >2.500.000 - 5.000.000'
    elif (row['Average_Transaction_Amount']>5000000 and row['Average_Transaction_Amount']<=10000000):
        val ='7. >5.000.000 - 10.000.000'
    else:
        val ='8. >10.000.000'
    return val

retail['Average_Transaction_Amount_Group']=retail.apply(f, axis=1)

#Visualization of customer distribution by average transaction amount group
customer_average = retail.groupby(['Average_Transaction_Amount_Group'])['Customer_ID'].count()
customer_average.plot(x='Average_Transaction_Amount_Group', y='Customer_ID', kind='bar',
    title='Customer Distribution by Average Transaction Amount Group')
plt.xlabel('Average Transaction Amount Group')
plt.ylabel('Number of Customer')
plt.tight_layout()
plt.show()

#Feature column and target
retail['Year_Diff']=retail['Year_Last_Transaction']-retail['Year_First_Transaction']
feature_column=['Average_Transaction_Amount', 'Count_Transaction', 'Year_Diff']
X=retail[feature_column]
y=retail['is_churn']
y=y.astype('int')

#Split to training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.25, random_state=0)

#Train, predict, and evaluate
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

#Initiate logreg model
logreg=LogisticRegression()

#Fit the model with data
logreg.fit(X_train, y_train)

#Predict the model
y_pred=logreg.predict(X_test)

#Evaluate the model using confusion matrix
cnf_matrix=confusion_matrix(y_test, y_pred)
print('Confusion matrix:\n', cnf_matrix)

#Visualization of confusion matrix
import numpy as np
class_names=[0,1]
fig, ax=plt.subplots()
tick_marks=np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap='YlGnBu', fmt='g')
ax.xaxis.set_label_position('top')
plt.title('Confusion Matrix', y=1.1)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.tight_layout()
plt.show()

#Accuracy, precision, and recall
from sklearn.metrics import accuracy_score, precision_score, recall_score
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred, average='micro'))
print('Recall:', recall_score(y_test, y_pred, average='micro'))