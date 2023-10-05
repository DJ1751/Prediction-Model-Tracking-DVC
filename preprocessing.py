import pandas as pd

# Load the data
bank_data = pd.read_csv(r"C:\Users\Dhruv\Desktop\DVCDEMO\bank-full.csv", delimiter=';')

# Data exploration
print(bank_data.info())  # Check data types and missing values
print(bank_data.describe())  # Summary statistics

# Convert categorical variables to factors
categorical_columns = bank_data.select_dtypes(include=['object']).columns
for col in categorical_columns:
    bank_data[col] = pd.Categorical(bank_data[col])

# Use one-hot encoding for categorical variables
bank_data = pd.get_dummies(bank_data, columns=categorical_columns, drop_first=True)

# Save the preprocessed data to a new CSV file if needed
bank_data.to_csv("preprocessed_bank_data.csv", index=False)

