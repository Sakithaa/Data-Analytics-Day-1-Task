import pandas as pd
df = pd.read_csv("netflix_titles.csv")  #Load the Data 
# print(df.head())

#Step 1
print("\n 1.Missing Values in each column  : ")
print(df.isnull().sum())
#To handle missing values 
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df.dropna(subset=['date_added'], inplace=True)
df['rating'] = df['rating'].fillna("Unrated")
df['duration'] = df['duration'].fillna("Unknown")
#Now check there are no missing values
print("\n After handling missing values:")
print(df.isnull().sum())

# #Step-2 :
print("\n2.Number of duplicate rows:")
print(df.duplicated().sum())
#if duplicate rows found remove them using this : 
df.drop_duplicates(inplace=True)   
print("After removing duplicates:", df.shape)

# #Step-3
print( " \n3.Standardize text values like gender, country names, etc")
df['type'] = df['type'].str.strip().str.title()
df['country'] = df['country'].str.strip()
df['rating'] = df['rating'].str.strip().str.upper()
df['listed_in'] = df['listed_in'].str.strip()
df['date_added'] = df['date_added'].str.strip()
# Print dataset to see changes
# print(df)


# #Step-4
print("\n 4.Convert date_added to datetime format and format it to dd-mm-yyyy")
df['date_added'] = pd.to_datetime(df['date_added'])                         # Step 4: Convert date_added to datetime format
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')                 # Format it to dd-mm-yyyy
# Print dataset columns to see changes
print(df['date_added'].head())

#Step-5
print("\n 5.Rename column headers to lowercase and replace spaces with underscores")
df.columns = df.columns.str.lower().str.replace(' ', '_')                   #Rename column headers to lowercase and replace spaces with underscores
# Print dataset to see changes
print(df.columns)

#Step-6 
print("\n 6.Check current data types of columns")
# First Check current data types
df['date_added'] = pd.to_datetime(df['date_added'], format="%d-%B-%Y", errors='coerce')
print(df.dtypes)


#Final Output: 
print("\nFinal DataFrame after all preprocessing steps:")
print(df)

df.to_excel("Day-1.xlsx", index=False)



