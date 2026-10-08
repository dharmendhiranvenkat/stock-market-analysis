import pandas as pd
import os

print("Checking files in folder...\n")
print(os.listdir())   # shows file names

print("\nLoading files...\n")

# LOAD FILES (skip first row to remove bad header)
analysis = pd.read_excel("analysis.xlsx", skiprows=1)
profitloss = pd.read_excel("Profitandloss.xlsx", skiprows=1)
balancesheet = pd.read_excel("balancesheet.xlsx", skiprows=1)
cashflow = pd.read_excel("cashflow.xlsx", skiprows=1)
proscons = pd.read_excel("prosandcons.xlsx", skiprows=1)
documents = pd.read_excel("documents.xlsx", skiprows=1)

print(" All files loaded\n")

# REMOVE UNNAMED COLUMNS
analysis = analysis.loc[:, ~analysis.columns.str.contains('^Unnamed', case=False)]
profitloss = profitloss.loc[:, ~profitloss.columns.str.contains('^Unnamed', case=False)]
balancesheet = balancesheet.loc[:, ~balancesheet.columns.str.contains('^Unnamed', case=False)]
cashflow = cashflow.loc[:, ~cashflow.columns.str.contains('^Unnamed', case=False)]
proscons = proscons.loc[:, ~proscons.columns.str.contains('^Unnamed', case=False)]
documents = documents.loc[:, ~documents.columns.str.contains('^Unnamed', case=False)]

print(" Unnamed columns removed\n")

# CLEAN COLUMN NAMES
analysis.columns = analysis.columns.str.strip().str.lower()
profitloss.columns = profitloss.columns.str.strip().str.lower()
balancesheet.columns = balancesheet.columns.str.strip().str.lower()
cashflow.columns = cashflow.columns.str.strip().str.lower()
proscons.columns = proscons.columns.str.strip().str.lower()
documents.columns = documents.columns.str.strip().str.lower()

print(" Column names cleaned\n")

# REMOVE EXTRA SPACES IN DATA
def clean_data(df):
    return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

analysis = clean_data(analysis)
profitloss = clean_data(profitloss)
balancesheet = clean_data(balancesheet)
cashflow = clean_data(cashflow)
proscons = clean_data(proscons)
documents = clean_data(documents)

print(" Extra spaces removed\n")

# HANDLE NULL VALUES
analysis.replace(['NULL', 'Null'], pd.NA, inplace=True)
profitloss.replace(['NULL', 'Null'], pd.NA, inplace=True)
balancesheet.replace(['NULL', 'Null'], pd.NA, inplace=True)
cashflow.replace(['NULL', 'Null'], pd.NA, inplace=True)
proscons.replace(['NULL', 'Null'], pd.NA, inplace=True)
documents.replace(['NULL', 'Null'], pd.NA, inplace=True)

print(" NULL values handled\n")

# SHOW DATA INFO
print("\n DATA INFO:\n")

print("ANALYSIS:")
print(analysis.info(), "\n")

print("PROFIT & LOSS:")
print(profitloss.info(), "\n")

print("BALANCE SHEET:")
print(balancesheet.info(), "\n")

print("CASH FLOW:")
print(cashflow.info(), "\n")

print("PROS & CONS:")
print(proscons.info(), "\n")

print("DOCUMENTS:")
print(documents.info(), "\n")

print(" STEP 1 COMPLETED SUCCESSFULLY ")
# ===== STEP 2: YEAR CLEANING =====

def clean_year(value):
    if pd.isna(value):
        return None

    value = str(value).strip()

    if "TTM" in value:
        return "TTM"

    try:
        # Convert like Mar-24 → Mar 2024
        if "-" in value:
            parts = value.split("-")
            month = parts[0]
            year = parts[1]

            if len(year) == 2:
                year = "20" + year

            return f"{month} {year}"

        return value

    except:
        return value


# APPLY TO ALL TABLES
if 'year' in analysis.columns:
    analysis['year'] = analysis['year'].apply(clean_year)

if 'year' in profitloss.columns:
    profitloss['year'] = profitloss['year'].apply(clean_year)

if 'year' in balancesheet.columns:
    balancesheet['year'] = balancesheet['year'].apply(clean_year)

if 'year' in cashflow.columns:
    cashflow['year'] = cashflow['year'].apply(clean_year)

print("\n Year cleaned successfully")

# CHECK RESULT
print("\n Sample years:")
if 'year' in analysis.columns:
    print(analysis['year'].unique()[:10])