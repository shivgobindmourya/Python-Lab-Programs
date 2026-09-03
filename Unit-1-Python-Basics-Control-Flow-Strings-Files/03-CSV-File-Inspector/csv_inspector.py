import pandas as pd


# --------------------------------------------------
# 1. Read the CSV file
# --------------------------------------------------

df = pd.read_csv("practice.csv")

print("========== ORIGINAL DATASET ==========")
print(df)


# --------------------------------------------------
# 2. Check the size of the dataset
# --------------------------------------------------

print("\n========== DATASET SHAPE ==========")
print(df.shape)


# --------------------------------------------------
# 3. Check column names
# --------------------------------------------------

print("\n========== COLUMN NAMES ==========")
print(df.columns)


# --------------------------------------------------
# 4. Check data types
# --------------------------------------------------

print("\n========== DATA TYPES ==========")
print(df.dtypes)


# --------------------------------------------------
# 5. Display first 5 rows
# --------------------------------------------------

print("\n========== FIRST 5 ROWS ==========")
print(df.head())


# --------------------------------------------------
# 6. Generate statistical summary
# --------------------------------------------------

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())


# --------------------------------------------------
# 7. Check for missing values
# --------------------------------------------------

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# --------------------------------------------------
# 8. Remove rows containing missing values
# --------------------------------------------------

cleaned_df = df.dropna()

print("\n========== CLEANED DATASET ==========")
print(cleaned_df)


# --------------------------------------------------
# 9. Filter employees with salary > 50000
# --------------------------------------------------

high_salary_df = df[df["salary"] > 50000]

print("\n========== SALARY > 50000 ==========")
print(high_salary_df)


# --------------------------------------------------
# 10. Filter Engineering employees
# --------------------------------------------------

engineering_df = df[df["department"] == "Engineering"]

print("\n========== ENGINEERING EMPLOYEES ==========")
print(engineering_df)


# --------------------------------------------------
# 11. Engineering employees with salary > 50000
# --------------------------------------------------

engineering_high_salary_df = df[
    (df["department"] == "Engineering") &
    (df["salary"] > 50000)
]

print("\n========== ENGINEERING + SALARY > 50000 ==========")
print(engineering_high_salary_df)


# --------------------------------------------------
# 12. Save cleaned dataset
# --------------------------------------------------

cleaned_df.to_csv("cleaned_data.csv", index=False)


# --------------------------------------------------
# 13. Save high-salary employees
# --------------------------------------------------

high_salary_df.to_csv("high_salary.csv", index=False)


# --------------------------------------------------
# 14. Save Engineering employees
# --------------------------------------------------

engineering_df.to_csv("engineering_employees.csv", index=False)


print("\n========== FILES SAVED SUCCESSFULLY ==========")
print("cleaned_data.csv")
print("high_salary.csv")
print("engineering_employees.csv")