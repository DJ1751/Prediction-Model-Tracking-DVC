import pandas as pd
import dvc.api

def explore_data(bank_data):
    # Data exploration
    print(bank_data.info())  # Check data types and missing values
    print(bank_data.describe())  # Summary statistics

    # Convert categorical variables to factors
    categorical_columns = bank_data.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        bank_data[col] = pd.Categorical(bank_data[col])

    # Save the exploration result to a file
    exploration_result = pd.DataFrame(...)  # Replace with your result
    exploration_result.to_csv("exploration_result.txt", index=False)

    # Track the result file with DVC
    with dvc.api.open("data/exploration_result.txt", "w") as dvc_file:
        exploration_result.to_csv(dvc_file, index=False)

if __name__ == "__main__":
    # Load the data (assuming it's loaded in your main script)
    bank_data = pd.read_csv(r"C:\Users\Dhruv\Desktop\Folder\Data\Data\bank-full.csv", delimiter=';')
    
    # Call the exploration function
    explore_data(bank_data)
