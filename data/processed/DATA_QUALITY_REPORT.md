# Airbnb NYC 2019 Data Quality Report
## 1. Dataset Overview
- Original rows: 48895
- Original columns: 16
- Cleaned rows: 48895
- Cleaned columns: 16

## 2. Missing Values Before Cleaning
- name: 16
- host_name: 21
- last_review: 10052
- reviews_per_month: 10052

## 3. Missing Values After Cleaning
- last_review: 10052

## 4. Duplicate Records
- Original duplicate rows: 0
- Cleaned duplicate rows: 0

## 5. Categorical Columns

### Room Type
- Private room
- Entire home/apt
- Shared room

### Neighbourhood Group
- Brooklyn
- Manhattan
- Queens
- Staten Island
- Bronx

## 6. Cleaning Methods Applied
- Mean imputation tested for reviews_per_month.
- Median imputation used for final reviews_per_month cleaning.
- KNN imputation tested for numerical missing values.
- Duplicate rows checked and removed.
- Categorical values standardized using whitespace removal.
- Missing name values replaced with 'Unknown'.
- Missing host_name values replaced with 'Unknown'.
- last_review converted to datetime format.

## 7. Final Dataset
- Cleaned dataset successfully created.
- File: data/processed/AB_NYC_2019_cleaned.csv
