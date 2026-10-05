import pandas as pd

# Messy dataset
data = {
    "Name": ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Diya"],
    "Marks": [78, 92, None, 105, 64, 92],
    "City": [" Chennai ", "mumbai", "DELHI", "chennai", None, "mumbai"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Find invalid marks
invalid = df["Marks"].notna() & ~df["Marks"].between(0, 100)

# Turn invalid marks into missing values
df.loc[invalid, "Marks"] = None

# 3. Fill missing marks with the mean of valid marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# 4. Fill missing cities
df["City"] = df["City"].fillna("Unknown")

# 5. Clean city names
df["City"] = df["City"].str.strip().str.title()

print("\nCleaned Data:")
print(df)

# 6. Final validation
print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nAre all marks between 0 and 100?")
print(df["Marks"].between(0, 100).all())

# 7. Save cleaned dataset
df.to_csv("students_cleaned.csv", index=False)

print("\nCleaned data saved to students_cleaned.csv")
