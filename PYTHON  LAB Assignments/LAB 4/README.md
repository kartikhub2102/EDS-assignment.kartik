# Lab 4 - EDS Assignments

| File | Description |
|------|-------------|

| problem1.py |Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:

The CSV file contains the columns: Date, Product, Quantity, Price, and City.
Group the data by Month and calculate the total sales for each month.
Find the month with the highest total sales and display it.
Also, display the total sales for the best month. |

| problem2.py | Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:

The CSV file contains the columns: Date, Product, Quantity, Price, and City.
Find the product that sold the most in terms of quantity sold.
Display the product that sold the most and the total quantity sold for that product.
 |

| problem3.py | Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:

The CSV file contains the columns: Date, Product, Quantity, Price, and City.
Group the data by City and calculate the total quantity of products sold for each city.
Find the city that sold the most products (based on the total quantity sold).
 |

| problem4.py | Write a Python program that takes the file name of a CSV file as input, reads the data, and performs the following operations:

The CSV file contains the following columns: Date, Product, Quantity, Price, and City.
For each date, find all pairs of products that were sold together (i.e., two products sold on the same date).
Output the product pair/s that was sold most frequently. |

| problem5.py | You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset. For each question, perform necessary data cleaning, transformations, and calculations as required.



Display the first 5 rows of the dataset.
Display the last 5 rows of the dataset.
Get the shape of the dataset (number of rows and columns).
Get a summary of the dataset (using .info()).
Get basic statistics (mean, standard deviation, etc.) of the dataset using .describe().
Check for missing values and display the count of missing values for each column.
Fill missing values in the ‘Age’ column with the median age.
Fill missing values in the ‘Embarked’ column with the most frequent value (mode()).
Drop the ‘Cabin’ column due to many missing values.
Create a new column, 'FamilySize' by adding the 'SibSp' and 'Parch' columns. |

| problem6.py |  You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset.

Create a new column ‘IsAlone’ which is 1 if the passenger is alone (FamilySize = 0), otherwise 0.
Convert the ‘Sex' column to numeric values (male: 0, female: 1).
One-hot encode the ‘Embarked’ column, dropping the first category.
Get the mean age of passengers.
Get the median fare of passengers.
Get the number of passengers by class.
Get the number of passengers by gender.
Get the number of passengers by survival status.
Calculate the survival rate of passengers.
Calculate the survival rate by gender.
|
| problem7.py | You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset.



Calculate the survival rate by class.
Calculate the survival rate by embarkation location (Embarked_S).
Calculate the survival rate by family size (FamilySize).
Calculate the survival rate by being alone (IsAlone).
Get the average fare by passenger class (Pclass).
Get the average age by passenger class (Pclass).
Get the average age by survival status (Survived).
Get the average fare by survival status (Survived).
Get the number of survivors by class (Pclass).
Get the number of non-survivors by class (Pclass).
 |
| problem8.py |You are provided with the Titanic dataset containing information about passengers on the Titanic. Your task is to write Python code to answer the following questions based on the dataset.



Get the number of survivors by gender (Sex).
Get the number of non-survivors by gender (Sex).
Get the number of survivors by embarkation location (Embarked_S).
Get the number of non-survivors by embarkation location (Embarked_S).
Calculate the percentage of children (Age < 18) who survived.
Calculate the percentage of adults (Age >= 18) who survived.
Get the median age of survivors.
Get the median age of non-survivors.
Get the median fare of survivors.
Get the median fare of non-survivors.  |