# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('titanic.csv')

# Display basic information about the dataset
print("Dataset Information:")
print(data.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(data.head())

# Handle missing values (optional step, depending on analysis needs)
# Example: Fill missing age values with the median age
data['Age'].fillna(data['Age'].median(), inplace=True)

# Exploratory Data Analysis (EDA)
# 1. Calculate basic statistics
print("\nBasic Statistics:")
print(data.describe())

# 2. Distribution of passengers who survived vs. did not survive
plt.figure(figsize=(8, 5))
sns.countplot(x='Survived', data=data, palette='Set2')
plt.title("Distribution of Survival (0 = No, 1 = Yes)")
plt.show()

# 3. Survival rate by passenger class
plt.figure(figsize=(8, 5))
sns.countplot(x='Pclass', hue='Survived', data=data, palette='Set1')
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.legend(title="Survived", loc="upper right", labels=["No", "Yes"])
plt.show()

# 4. Age distribution by survival
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='Age', hue='Survived', multiple='stack', kde=True)
plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()

# 5. Average survival rate by gender
plt.figure(figsize=(8, 5))
sns.barplot(x='Sex', y='Survived', data=data, palette='pastel')
plt.title("Average Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.show()

# 6. Correlation heatmap for numerical features
plt.figure(figsize=(10, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Summarize insights
print("\nSummary of Insights:")
print("- More passengers in lower classes (Pclass = 3) did not survive compared to those in higher classes.")
print("- Women had a higher survival rate than men.")
print("- Younger passengers (especially children) had higher survival rates.")
print("- Passenger class and gender show strong influence on survival rate.")
