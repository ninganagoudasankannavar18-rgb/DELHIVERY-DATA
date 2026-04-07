import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("delhivery_data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Dataset overview
print(df.head())
print(df.info())
print(df.describe())

sns.set(style="whitegrid")

# Histogram of actual delivery time
plt.figure(figsize=(8,5))
sns.histplot(df['actual_time'], kde=True)
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery Time")
plt.ylabel("Frequency")
plt.show()

# Distance vs Time
plt.figure(figsize=(8,5))
sns.scatterplot(x=df['osrm_distance'], y=df['actual_time'])
plt.title("Distance vs Delivery Time")
plt.xlabel("Distance")
plt.ylabel("Time Taken")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Matrix")
plt.show()

#Save Cleaned Dataset

df.to_csv("cleaned_delhivery_data.csv",index=False)
print("Cleaned dataset saved as cleaned_delhivery_data.csv")