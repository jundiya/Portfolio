#import library
import pandas as pd
pd.options.display.max_columns=50

#import dataset
df_load = pd.read_csv(r'D:/Python/DQLAB/Data Cleansing/dqlab_telco.csv')

#Show the number of rows and columns
print(df_load.shape)

#Show 5 rows to select
print('\n', df_load.head(5))

#Show the number of unique value of customerID
print('\n', df_load.customerID.nunique())

#Show the data type of each columns
print('\n', df_load.dtypes)

#Filter customerID with specific format
df_load['valid_id']=df_load['customerID'].astype(str).str.match(r'(45\d{9,10})')
df_load=(df_load[df_load['valid_id']==True]).drop('valid_id',axis=1)
print('\nJumlah ID Customer yang terfilter adalah', df_load['customerID'].count())
print('\n', df_load.dtypes)

#Drop duplicate rows
df_load.drop_duplicates()

#Drop duplicate customerID sorted by periode
df_load=df_load.sort_values('UpdatedAt',ascending=False).drop_duplicates(['customerID'])
print('\nJumlah ID Customer yang sudah dihilangkan duplikasinya (distinct) adalah',df_load['customerID'].count())

print('\nTotal missing values data dari kolom Churn', df_load['Churn'].isnull().sum())
#Drop all missing rows with specific column (Churn)
df_load.dropna(subset=['Churn'], inplace=True)
print('\n', df_load['Churn'].isnull().sum())
print('\nTotal baris dan kolom data setelah dihapus data missing values adalah', df_load.shape)

print('\nStatus missing values :',df_load.isnull().values.any())
print('\nJumlah missing values masing-masing kolom adalah:')
print(df_load.isnull().sum().sort_values(ascending=False))

#Handling missing values of tenure
df_load['tenure'].fillna(11, inplace=True)

#Handling missing values num vars (except Tenure)
for col_name in list(['MonthlyCharges','TotalCharges']):
    median=df_load[col_name].median()
    df_load[col_name].fillna(median, inplace=True)
print('\nJumlah missing values setelah di imputer datanya adalah:')
print(df_load.isnull().sum().sort_values(ascending=False))

print('\nPersebaran data sebelum outliers ditangani: ')
print(df_load[['tenure','MonthlyCharges','TotalCharges']].describe())

#Detect the outliers with box plot
import matplotlib.pyplot as plt
import seaborn as sns

#Insert the variable
plt.figure()
sns.boxplot(x=df_load['tenure'])
plt.show()

plt.figure()
sns.boxplot(x=df_load['MonthlyCharges'])
plt.show()

plt.figure()
sns.boxplot(x=df_load['TotalCharges'])
plt.show()

#Handling outliers with IQR
Q1=(df_load[['tenure', 'MonthlyCharges', 'TotalCharges']]).quantile(0.25)
Q3=(df_load[['tenure', 'MonthlyCharges', 'TotalCharges']]).quantile(0.75)

IQR=Q3-Q1
maximum=Q3+(1.5*IQR)
print('\nNilai maksimum dari masing-masing variable adalah:')
print(maximum)
minimum=Q1-(1.5*IQR)
print('\nNilai minimum dari masing-masing variable adalah:')
print(minimum)

more_than=(df_load>maximum)
lower_than=(df_load<minimum)
#Masking outliers
df_load=df_load.mask(more_than, maximum, axis=1)
df_load=df_load.mask(lower_than, minimum, axis=1)

print('\nPersebaran data setelah outliers ditangani:')
print(df_load[['tenure', 'MonthlyCharges', 'TotalCharges']].describe())

#Detect non-standard values
for col_name in list(['gender','SeniorCitizen','Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','Churn']):
  print('\nUnique values count variable', col_name)
  print(df_load[col_name].value_counts())

#Standarized the values
df_load = df_load.replace(['Wanita', 'Laki-Laki', 'Churn', 'Iya'],['Female', 'Male', 'Yes', 'Yes'])
for col_name in list(['gender', 'Dependents', 'Churn']):
    print('\nUnique values count variable',col_name)
    print(df_load[col_name].value_counts())