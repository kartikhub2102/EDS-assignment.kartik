# Lab 5 - EDS Assignments

| File | Description |
|------|-------------|
| problem1.py | Write a Python program to analyze and visualize data from the Titanic dataset based on the following instructions:



Dataset Information:
The dataset is stored in a CSV file named titanic.csv and has been loaded using the pandas library. It contains the following columns:

Pclass: Passenger class (1 = First, 2 = Second, 3 = Third).
Gender: Gender of the passenger (male/female).
Age: Age of the passenger.
Survived: Survival status (0 = Did not survive, 1 = Survived).
Fare: Ticket fare paid by the passenger.




Visualization:
To represent these trends, you will create 5 visualizations using Matplotlib. The visualizations should be arranged in a 3x2 grid (3 rows and 2 columns).




Visualization Details:
Write the code to create a series of visualizations as follows:

Bar Plot (Pclass Distribution):

Create a bar plot to show the distribution of passengers across the different passenger classes (Pclass).
Use the color skyblue for the bars.
Title the plot as "Passenger Class Distribution".
Label the x-axis as "Pclass" and the y-axis as "Count".
Pie Chart (Gender Distribution):

Create a pie chart to display the distribution of male and female passengers.
Use lightblue for males and lightcoral for females.
Include percentages on the slices (use autopct='%1.1f%%').
Title the plot as "Gender Distribution".
Histogram (Age Distribution):

Create a histogram to visualize the distribution of passengers' ages.
Use lightgreen for the bars with black edges (edgecolor = 'black').
Set the number of bins to 8 for the histogram.
Title the plot as "Age Distribution".
Label the x-axis as "Age" and the y-axis as "Frequency".
Bar Plot (Survival Count):

Create a bar plot to show the count of passengers who survived and those who did not, based on the Survived column.
Use the colors lightblue for survivors (1) and lightcoral for non-survivors (0).
Title the plot as "Survival Count".
Label the x-axis as "Survived (0 = No, 1 = Yes)" and the y-axis as "Count".
Scatter Plot (Fare vs Age):

Create a scatter plot to visualize the relationship between the Fare and Age of passengers.
Use orange for the data points.
Title the plot as "Fare vs Age".
Label the x-axis as "Age" and the y-axis as "Fare".
 |

| problem2.py |  Write a Python code to plot a histogram for the distribution of the 'Age' column from the Titanic dataset. The histogram should display the frequency of different age ranges with the following specifications:

Use 30 bins for the histogram.
Set the edge color of the bars to black (k).
Label the x-axis as 'Age' and the y-axis as 'Frequency'.
Add the title "Age Distribution" to the histogram.|

| problem3.py | Write a Python code to plot a bar chart that shows the count of passengers who survived and did not survive in the Titanic dataset. The chart should display the following specifications:

Use the 'Survived' column to show the count of survivors (0 = Did not survive, 1 = Survived).
Set the chart type to 'bar'.
Add the title "Survival Count" to the chart.
Label the x-axis as 'Survived' and the y-axis as 'Count'.|

| problem4.py | Write a Python code to plot a stacked bar chart that shows the count of passengers who survived and did not survive, grouped by gender, in the Titanic dataset. The chart should display the following specifications:

Group the data by the 'Sex' column, then use the value_counts() function to count the occurrences of survivors (0 = Did not survive, 1 = Survived) for each gender.
Use a stacked bar chart to display the survival counts.
Add the title "Survival by Gender" to the chart.
Label the x-axis as 'Gender' and the y-axis as 'Count'.
The legend should indicate 'Not Survived' and 'Survived'.|


| problem5.py |Write a Python code to plot a stacked bar chart that shows the count of passengers who survived and did not survive, grouped by passenger class (Pclass), in the Titanic dataset. The chart should display the following specifications:

Group the data by the Pclass column and count the number of survivors (0 = Did not survive, 1 = Survived) for each class using value_counts().
Use a stacked bar chart to display the survival counts.
Add the title "Survival by Pclass" to the chart.
Label the x-axis as 'Pclass' and the y-axis as 'Count'.
The legend should indicate 'Not Survived' and 'Survived'.|

| problem6.py |Write a Python code to plot a stacked bar chart showing the survival count for passengers based on their embarkation location in the Titanic dataset.

The chart should display the following specifications:

Use the Embarked column to determine the embarkation location. After converting this column into dummy variables (using pd.get_dummies()), plot the survival count based on the Embarked_Q column (representing passengers who embarked from Queenstown) in relation to survival.
Set the chart type to 'bar' and make it stacked.
Add the title "Survival by Embarked " to the chart.
Label the x-axis as 'Embarked' and the y-axis as 'Count'.
Include a legend to distinguish between survivors and non-survivors (label the legend as 'Survived' and 'Not Survived').|

| problem7.py |Write a Python code to plot a boxplot that shows the distribution of the 'Age' column from the Titanic dataset across different passenger classes. The boxplot should display the following specifications:

Use the Pclass column to group the data for the boxplot.
Set the title of the plot to "Age by Pclass".
Remove the default subtitle with plt.suptitle('').
Label the x-axis as 'Pclass' and the y-axis as 'Age'.|

| problem8.py |Write a Python code to plot a boxplot that shows the distribution of the 'Age' column from the Titanic dataset based on whether passengers survived or not. The boxplot should display the following specifications:

Use the Survived column to group the data for the boxplot (0 = Did not survive, 1 = Survived).
Set the title of the plot to "Age by Survival".
Remove the default subtitle with plt.suptitle('').
Label the x-axis as 'Survived' and the y-axis as 'Age'.|

| problem9.py |Write a Python code to plot a boxplot that shows the distribution of the 'Fare' column from the Titanic dataset based on the passenger class (Pclass). The boxplot should display the following specifications:

Use the Pclass column to group the data for the boxplot.
Set the title of the plot to "Fare by Pclass".
Remove the default subtitle with plt.suptitle('').
Label the x-axis as 'Pclass' and the y-axis as 'Fare'.|

| problem10.py |Write a Python code to plot a scatter plot showing the relationship between the 'Age' and 'Fare' columns in the Titanic dataset. The scatter plot should display the following specifications:

Use the Age column for the x-axis and the Fare column for the y-axis.
Set the title of the plot to "Age vs. Fare".
Label the x-axis as 'Age' and the y-axis as 'Fare'.|

| problem11py |Write a Python code to plot a scatter plot showing the relationship between the 'Age' and 'Fare' columns in the Titanic dataset, with points color-coded by survival status. The scatter plot should display the following specifications:

Use the Age column for the x-axis and the Fare column for the y-axis.
Color the points based on the Survived column: Red for passengers who did not survive (Survived = 0). Blue for passengers who survived (Survived = 1).
Set the title of the plot to "Age vs. Fare by Survival".
Label the x-axis as 'Age' and the y-axis as 'Fare'.|
