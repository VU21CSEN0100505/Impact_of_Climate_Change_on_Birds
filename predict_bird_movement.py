import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load bird data
bird_data_path = r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\combined_occurrence.csv"
bird_data = pd.read_csv(bird_data_path)

# Check the column names to confirm the structure
print("Columns in dataset:", bird_data.columns)

# Add current climate data (mock example, replace with actual data if available)
bird_data["Climate"] = [25.0] * len(bird_data)  # Replace with actual climate data

# Prepare data for training
X = bird_data[["decimalLatitude", "decimalLongitude", "Climate"]]  # Correct column names
y = bird_data["species"]  # Adjust based on actual column for species

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Predict future bird locations
# Replace climate data for future prediction
bird_data["Climate"] = [28.0] * len(bird_data)  # Replace with future climate data
X_future = bird_data[["decimalLatitude", "decimalLongitude", "Climate"]]
future_predictions = model.predict(X_future)

# Add predictions to the dataset
bird_data["Future Predictions"] = future_predictions

# Save predictions to a CSV file
output_path = r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\future_bird_predictions.csv"
bird_data.to_csv(output_path, index=False)
print(f"Saved predictions to {output_path}")
