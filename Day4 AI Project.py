import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv(r'G:\Datasets\student.csv')  # Ensure correct path

# Check column names in dataset
print("Columns in dataset:", df.columns)

# Compute average scores (only for the given subjects)
df['Average'] = df[['Maths', 'Physics', 'Chemistry', 'English']].mean(axis=1)

# Display each student's average score
print("Student Average Scores:\n", df[['Name', 'Average']])

# Find the student with the highest average score
top_student = df.loc[df['Average'].idxmax()]
print("\nStudent with the Highest Average Score:")
print(top_student[['Name', 'Average']])

# Calculate the average score for each subject
subject_averages = df[['Maths', 'Physics', 'Chemistry', 'English']].mean()
print("\nAverage Scores for Each Subject:")
print(subject_averages)

# Save the results to a new CSV file
df.to_csv(r'G:\Datasets\student_results.csv', index=False)
print("\nResults saved to 'student_results.csv'.")
