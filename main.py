import pandas as pd

# Load the bird occurrence dataset
data_path = "climate change/bird dataset/occurrence.txt"  # Update with the actual path
bird_data = pd.read_csv(data_path, sep="\t")  # Adjust the delimiter if needed

# Display the first few rows
print("Bird Occurrence Dataset:")
print(bird_data.head())

# Check for missing values
print("\nMissing Values:")
print(bird_data.isnull().sum())

# Optional: Drop rows with missing values
bird_data = bird_data.dropna()

# Summary of the dataset
print("\nDataset Summary:")
print(bird_data.describe())
