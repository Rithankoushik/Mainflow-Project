# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Datasets
student_mat = pd.read_csv('E:\\mainflow assignment\\student\\student1.csv',sep=';')
student_por = pd.read_csv('E:\\mainflow assignment\\student\\student2.csv',sep=';')

# Combine the Datasets
student_data = pd.concat([student_mat, student_por], ignore_index=True)

# Display Initial Data Information
print("First Few Rows of the Combined Dataset:")
print(student_data.head())
print("\nShape of Combined Dataset:", student_data.shape)
print("\nData Types:")
print(student_data.dtypes)

# Check for Missing Values
print("\nMissing Values in Each Column:")
print(student_data.isnull().sum())

# Data Cleaning
student_data.fillna(student_data.median(numeric_only=True), inplace=True)
student_data.drop_duplicates(inplace=True)
print("\nShape After Cleaning:", student_data.shape)

# Data Analysis Questions
# Question 1: Average Final Grade (G3)
average_final_grade = student_data['G3'].mean()
print("\nAverage Final Grade (G3):", average_final_grade)

# Question 2: Students Scoring Above 15 in Final Grade
students_above_15 = student_data[student_data['G3'] > 15].shape[0]
print("\nNumber of Students Scoring Above 15 in G3:", students_above_15)

# Question 3: Correlation Between Study Time and Final Grade
correlation = student_data['studytime'].corr(student_data['G3'])
print("\nCorrelation Between Study Time and Final Grade (G3):", correlation)

# Question 4: Average Final Grade by Gender
average_by_gender = student_data.groupby('sex')['G3'].mean()
print("\nAverage Final Grade by Gender:")
print(average_by_gender)

# Data Visualization
# Histogram of Final Grades
plt.figure(figsize=(8, 5))
plt.hist(student_data['G3'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Final Grades (G3)')
plt.xlabel('Final Grade (G3)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot of Study Time vs. Final Grade
plt.figure(figsize=(8, 5))
sns.scatterplot(x='studytime', y='G3', data=student_data, color='orange')
plt.title('Study Time vs Final Grade')
plt.xlabel('Study Time (hours per week)')
plt.ylabel('Final Grade (G3)')
plt.show()

# Bar Chart of Average Final Grade by Gender
plt.figure(figsize=(8, 5))
average_by_gender.plot(kind='bar', color=['blue', 'pink'])
plt.title('Average Final Grade by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Final Grade (G3)')
plt.xticks(rotation=0)
plt.show()

