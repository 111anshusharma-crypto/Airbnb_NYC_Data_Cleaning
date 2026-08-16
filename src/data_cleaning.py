import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/AB_NYC_2019.csv")

print("Original Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nMissing Percentage:")
print((df.isnull().sum() / len(df) * 100).round(2))
# ---------------------------------------
# STEP 9: MISSING VALUE IMPUTATION
# ---------------------------------------

from sklearn.impute import KNNImputer

# Mean Imputation
df_mean = df.copy()

df_mean["reviews_per_month"] = df_mean["reviews_per_month"].fillna(
    df_mean["reviews_per_month"].mean()
)

print("\nMean Imputation:")
print("Missing reviews_per_month:",
      df_mean["reviews_per_month"].isnull().sum())


# Median Imputation
df_median = df.copy()

df_median["reviews_per_month"] = df_median["reviews_per_month"].fillna(
    df_median["reviews_per_month"].median()
)

print("\nMedian Imputation:")
print("Missing reviews_per_month:",
      df_median["reviews_per_month"].isnull().sum())


# KNN Imputation
df_knn = df.copy()

knn_columns = [
    "latitude",
    "longitude",
    "price",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
    "calculated_host_listings_count",
    "availability_365"
]

imputer = KNNImputer(n_neighbors=5)

df_knn[knn_columns] = imputer.fit_transform(
    df_knn[knn_columns]
)

print("\nKNN Imputation:")
print("Missing reviews_per_month:",
      df_knn["reviews_per_month"].isnull().sum())
print("\nMean value:",
      df["reviews_per_month"].mean())

print("Median value:",
      df["reviews_per_month"].median())
# ---------------------------------------
# STEP 10: DUPLICATE CHECK
# ---------------------------------------

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("Shape after removing duplicates:")
print(df.shape)
# ---------------------------------------
# STEP 10: DUPLICATE ROWS
# ---------------------------------------

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("Shape after removing duplicates:")
print(df.shape)
# ---------------------------------------
# STEP 11: CHECK CATEGORIES
# ---------------------------------------

print("\nRoom Type Categories:")
print(df["room_type"].unique())

print("\nNeighbourhood Group Categories:")
print(df["neighbourhood_group"].unique())

print("\nNumber of Neighbourhood Categories:")
print(df["neighbourhood"].nunique())

print("\nRoom Type Counts:")
print(df["room_type"].value_counts())

print("\nNeighbourhood Group Counts:")
print(df["neighbourhood_group"].value_counts())
# ---------------------------------------
# STEP 11.2: STANDARDIZE CATEGORIES
# ---------------------------------------

categorical_columns = [
    "room_type",
    "neighbourhood_group",
    "neighbourhood"
]

for col in categorical_columns:
    df[col] = df[col].astype("string").str.strip()

print("\nCategories after standardization:")

print("\nRoom Type:")
print(df["room_type"].unique())

print("\nNeighbourhood Group:")
print(df["neighbourhood_group"].unique())
# ---------------------------------------
# STEP 12: FINAL MISSING VALUE HANDLING
# ---------------------------------------

# Fill missing text values
df["name"] = df["name"].fillna("Unknown")
df["host_name"] = df["host_name"].fillna("Unknown")

# Convert last_review to datetime
df["last_review"] = pd.to_datetime(
    df["last_review"],
    errors="coerce"
)

# Fill missing reviews_per_month using median
median_reviews = df["reviews_per_month"].median()

df["reviews_per_month"] = df["reviews_per_month"].fillna(
    median_reviews
)

print("\nRemaining Missing Values:")
print(df.isnull().sum())
# ---------------------------------------
# STEP 13: FINAL VALIDATION
# ---------------------------------------

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())

print("\nFinal Missing Values:")
print(df.isnull().sum())

# Save cleaned dataset
output_path = "data/processed/AB_NYC_2019_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("File:", output_path)