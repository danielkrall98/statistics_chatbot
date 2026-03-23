import pandas as pd

INPUT_FILE = "data/wien_bevoelkerung.csv"
OUTPUT_FILE = "data/cleaned_data.csv"

df = pd.read_csv(INPUT_FILE, sep=";", skiprows=4, encoding="utf-8")

# Rename Columns
df.columns = [
    "region",
    "total",
    "male",
    "female",
    "austrian_total",
    "austrian_male",
    "austrian_female",
    "foreign_total",
    "foreign_male",
    "foreign_female"
]

# Remove Rows
df = df.dropna(subset=["region"]) # Missing Data
df = df[~df["region"].str.contains("Quelle", na=False)] # Last Line ("Quelle ..."")
df["region"] = df["region"].str.replace(r"^\d+\.\s*", "", regex=True) # Numbering
# print(df.head())

# Convert to numeric (int)
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

df.to_csv(OUTPUT_FILE, index=False)

print("Cleaned data saved to", OUTPUT_FILE)