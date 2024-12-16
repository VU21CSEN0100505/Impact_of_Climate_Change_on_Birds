import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load bird data
bird_data = pd.read_csv("combine_datasets.csv")

# Add current climate data (mock example for simplicity)
bird_data["Climate"] = [25.0] * len(bird_data)  # Replace with actual climate data

# Prepare data for training
X = bird_data[["Latitude", "Longitude", "Climate"]]
y = bird_data["Species"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict future bird locations (mock example)
bird_data["Future Climate"] = [28.0] * len(bird_data)  # Replace with future climate data
X_future = bird_data[["Latitude", "Longitude", "Future Climate"]]
future_predictions = model.predict(X_future)
bird_data["Future Predictions"] = future_predictions

# Save predictions
bird_data.to_csv("future_bird_predictions.csv", index=False)
print("Saved predictions to future_bird_predictions.csv")
