import pandas as pd

# Load bird predictions
bird_predictions = pd.read_csv("future_bird_predictions.csv")

# Write a simple report
report = """
Bird Climate Analysis Report
============================
1. Bird data overlaid on climate maps.
2. Compared current and future climate maps.
3. Predicted bird movements based on climate changes.
4. Results saved as 'future_bird_predictions.csv'.

Summary:
- Total birds analyzed: {}
- Unique species: {}
- Predictions saved successfully.

""".format(len(bird_predictions), bird_predictions["Species"].nunique())

# Save the report
with open("climate_analysis_report.txt", "w") as f:
    f.write(report)

print("Report saved as 'climate_analysis_report.txt'")
