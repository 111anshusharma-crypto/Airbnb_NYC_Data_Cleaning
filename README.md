# Airbnb NYC 2019 Data Cleaning Project

## Project Overview

This project cleans and preprocesses the Airbnb NYC 2019 dataset.

## Dataset

New York City Airbnb Open Data 2019

Original dataset:
- Rows: 48,895
- Columns: 16

## Data Cleaning Tasks

- Missing value analysis
- Mean imputation
- Median imputation
- KNN imputation
- Duplicate detection
- Duplicate removal
- Category standardization
- Text value cleaning
- Date conversion
- Final validation

## Missing Value Handling

### reviews_per_month

Mean, Median, and KNN imputation methods were evaluated.

Median imputation was selected for the final cleaned dataset.

### name

Missing values were replaced with `Unknown`.

### host_name

Missing values were replaced with `Unknown`.

### last_review

Missing values were retained because they can represent listings
with no recorded review.

## Duplicate Handling

Duplicate rows were checked.

Result:

0 duplicate rows.

## Categorical Cleaning

The following columns were standardized:

- room_type
- neighbourhood_group
- neighbourhood

Whitespace was removed from categorical values.

## Final Dataset

Original:

48,895 rows × 16 columns

Cleaned:

48,895 rows × 16 columns

## Output

The cleaned dataset is generated as:

`data/processed/AB_NYC_2019_cleaned.csv`

A quality report is generated as:

`data/processed/DATA_QUALITY_REPORT.md`