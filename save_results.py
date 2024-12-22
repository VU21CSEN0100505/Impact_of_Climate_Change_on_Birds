import pandas as pd

# Path to the predictions CSV file
predictions_path = r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\future_bird_predictions.csv"

# Load bird predictions
bird_predictions = pd.read_csv(predictions_path)

# Write a simple report
report = f"""
Bird Climate Analysis Report
============================
1. Bird data overlaid on climate maps.
2. Compared current and future climate maps.
3. Predicted bird movements based on climate changes.
4. Results saved as '{predictions_path}'.

Summary:
- Total birds analyzed: {len(bird_predictions)}
- Unique species: {bird_predictions['species'].nunique()}
- Predictions saved successfully.

"""

# Path to save the report
report_path = r"S:\Impact of Climate Change on Birds\Capstone 2\Climate change\bird dataset\climate_analysis_report.txt"

# Save the report
with open(report_path, "w") as f:
    f.write(report)

print(f"Report saved as '{report_path}'")
