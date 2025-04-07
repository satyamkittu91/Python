import pandas as pd

dataframe = pd.read_csv(r'Python/Libraries/datafile.csv')
dataframe1 = pd.read_csv(r'Python/Libraries/employees.csv')
dataframe2 = pd.read_csv(r'Python/Libraries/departments.csv')

#placing ID as index
dataframe.set_index('ID', inplace=True)

print(dataframe.head()) # Prints first five rows of the data

print(dataframe.info()) # information about the data

print(dataframe.describe()) # Statistical information about the columns and detailed info

# loc - Rows/columns by name/label

print(dataframe.loc[dataframe['Department'] == 'Engineering']) # prints the rows where department is engineer
print(dataframe.loc[dataframe['Department'] == 'Engineering', ['Name', 'Salary']]) # prints the specified columns
print(dataframe.loc[dataframe['Salary'] > 60000])
print(dataframe.loc[dataframe['PerformanceRating'] >= 4.5, ['Name', 'PerformanceRating']])
print(dataframe.loc[104])


# iloc - Rows/columns by position/index
print(dataframe.iloc[0])
print(dataframe.iloc[0:3])
print(dataframe.iloc[0, 1])
print(dataframe.iloc[:, 1]) # Get all the rows from the salary column
print(dataframe.iloc[-3:, [1, 4]]) # columns : Age (1), joiningDate (4)
print(dataframe.iloc[0:3, 1:4]) # rows : 0 to 2 (3 not included), columns : 1 to 3 (4 not included)


# Basic Cleaning
dataframe.dropna() # drops the rows with any missing values
dataframe.dropna(axis=1) # drops the columns with any missing values
dataframe.fillna(0) # fills the missing values with 0
dataframe.fillna(method='ffill') # forward fill the missing values
dataframe.fillna(method='bfill') # backward fill the missing values
dataframe.drop_duplicates() # drops the duplicate rows
dataframe.drop_duplicates(subset=['Name']) # drops the duplicate rows based on the name column
dataframe.drop_duplicates(subset=['Name'], keep='last') # keeps the last duplicate row
dataframe.drop_duplicates(subset=['Name'], keep=False) # drops all the duplicate rows
dataframe.astype({'Salary': 'int'}) # changes the data type of the salary column to int


# Grouping and Aggregation
dataframe.groupby('Department').mean() # groups the data by department and calculates the mean of each group
dataframe.value_counts() # counts the number of occurrences of each value in the dataframe
dataframe.groupby('Department')['Salary'].mean() # groups the data by department and calculates the mean salary of each group
dataframe.groupby('Department')['Salary'].agg(['mean', 'max']) # groups the data by department and calculates the mean and max salary of each group
dataframe.groupby('Department')['Salary'].agg(['mean', 'max']).reset_index() # resets the index after grouping


# Merging and Joining
dataframe3 = dataframe1.merge(dataframe2, on='DepartmentID') # merges the two dataframes on the department ID column
dataframe1.merge(dataframe2, on='DepartmentID', how='inner') # inner join
dataframe1.merge(dataframe2, on='DepartmentID', how='outer') # outer join
dataframe1.merge(dataframe2, on='DepartmentID', how='left') # left join
dataframe1.merge(dataframe2, on='DepartmentID', how='right') # right join
dataframe1.merge(dataframe2, on='DepartmentID', how='cross') # cross join
dataframe1.merge(dataframe2, left_on='DepartmentID', right_on='ID') # merges the two dataframes on the department ID column
dataframe1.merge(dataframe2, left_on='DepartmentID', right_on='ID', suffixes=('_emp', '_dept')) # adds suffixes to the columns with same name

# Concat
pd.concat([dataframe1, dataframe2], axis=0) # concatenates the two dataframes vertically
pd.concat([dataframe1, dataframe2], axis=1) # concatenates the two dataframes horizontally
pd.concat([dataframe1, dataframe2], axis=0, ignore_index=True) # ignores the index while concatenating
pd.concat([dataframe1, dataframe2], axis=1, ignore_index=True) # ignores the index while concatenating
pd.concat([dataframe1, dataframe2], axis=0, keys=['emp', 'dept']) # adds keys to the concatenated dataframe
pd.concat([dataframe1, dataframe2], axis=1, keys=['emp', 'dept']) # adds keys to the concatenated dataframe