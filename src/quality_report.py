import pandas as pd

# ---------------------------------------
# STEP 14: FINAL DATA QUALITY REPORT
# ---------------------------------------

input_file = "data/raw/AB_NYC_2019.csv"
cleaned_file = "data/processed/AB_NYC_2019_cleaned.csv"

# Load datasets
original = pd.read_csv(input_file)
cleaned = pd.read_csv(cleaned_file)

# Create report
report = []

report.append("# Airbnb NYC 2019 Data Quality Report\n")

report.append("## 1. Dataset Overview\n")
report.append(f"- Original rows: {original.shape[0]}\n")
report.append(f"- Original columns: {original.shape[1]}\n")
report.append(f"- Cleaned rows: {cleaned.shape[0]}\n")
report.append(f"- Cleaned columns: {cleaned.shape[1]}\n")

report.append("\n## 2. Missing Values Before Cleaning\n")
missing_before = original.isnull().sum()

for column, value in missing_before.items():
    if value > 0:
        report.append(f"- {column}: {value}\n")

report.append("\n## 3. Missing Values After Cleaning\n")
missing_after = cleaned.isnull().sum()

for column, value in missing_after.items():
    if value > 0:
        report.append(f"- {column}: {value}\n")

report.append("\n## 4. Duplicate Records\n")
report.append(
    f"- Original duplicate rows: {original.duplicated().sum()}\n"
)
report.append(
    f"- Cleaned duplicate rows: {cleaned.duplicated().sum()}\n"
)

report.append("\n## 5. Categorical Columns\n")

report.append("\n### Room Type\n")
for value in cleaned["room_type"].unique():
    report.append(f"- {value}\n")

report.append("\n### Neighbourhood Group\n")
for value in cleaned["neighbourhood_group"].unique():
    report.append(f"- {value}\n")

report.append("\n## 6. Cleaning Methods Applied\n")
report.append("- Mean imputation tested for reviews_per_month.\n")
report.append("- Median imputation used for final reviews_per_month cleaning.\n")
report.append("- KNN imputation tested for numerical missing values.\n")
report.append("- Duplicate rows checked and removed.\n")
report.append("- Categorical values standardized using whitespace removal.\n")
report.append("- Missing name values replaced with 'Unknown'.\n")
report.append("- Missing host_name values replaced with 'Unknown'.\n")
report.append("- last_review converted to datetime format.\n")

report.append("\n## 7. Final Dataset\n")
report.append("- Cleaned dataset successfully created.\n")
report.append("- File: data/processed/AB_NYC_2019_cleaned.csv\n")

# Save report
with open(
    "data/processed/DATA_QUALITY_REPORT.md",
    "w"
) as file:
    file.writelines(report)

print("Quality report generated successfully!")
print("File: data/processed/DATA_QUALITY_REPORT.md")