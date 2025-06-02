import pandas as pd
df=pd.read_csv('retail_store_sales.csv') #reads csv
df.columns   #list of column names
df.columns = df.columns.str.strip().str.lower()
df.head() #views first five rows
df.info() #data types and non null contents
df.describe() #Summary statistics
df.isnull().sum() #counts missing vales per column
df.fillna(df.mean(numeric_only=True),inplace=True)
df['item']=df['item'].fillna(0)
df['discount applied']=df['discount applied'].fillna(0)
df.drop_duplicates(inplace=True)#remove duplicate rows 
df['transaction date']=pd.to_datetime(df['transaction date'],errors='coerce')#coverts to datetime
df['transaction date']=df['transaction date'].dt.strftime('%d-%m-%Y')
print(df.dtypes)#displays datatypes
print(df.isnull().sum())
print(df.columns.tolist())
print(df.head())

