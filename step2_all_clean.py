import pandas as pd
import os

folder_path = r"E:\BOLDANAYSTICSCOMPANY\PROJECT2STOCKMARKETANAYSIS\DATASET2"

# 🔥 READ (skip first garbage row)
analysis = pd.read_excel(os.path.join(folder_path, "analysis.xlsx"), skiprows=1)

# Clean column names
analysis.columns = analysis.columns.str.strip().str.lower()

# Rename
analysis.rename(columns={"company_id": "company"}, inplace=True)

# Drop id
if "id" in analysis.columns:
    analysis.drop(columns=["id"], inplace=True)


# 🔥 STRONG SPLIT FUNCTION (handles ALL cases)
def split_column(col):
    data = analysis[col].astype(str)

    # Fix missing colon cases like "5 Years 14%"
    data = data.str.replace(r"(\d+\s*Years)\s+(\-?\d+%)", r"\1: \2", regex=True)

    # Replace comma with colon
    data = data.str.replace(",", ":")

    split = data.str.split(":", n=1, expand=True)

    period = split[0].str.strip()

    value = (
        split[1]
        .str.replace("%", "", regex=False)
        .str.strip()
    )

    value = pd.to_numeric(value, errors='coerce')

    return period, value


# Apply
analysis['sales_period'], analysis['sales_value'] = split_column('compounded_sales_growth')
analysis['profit_period'], analysis['profit_value'] = split_column('compounded_profit_growth')
analysis['stock_period'], analysis['stock_value'] = split_column('stock_price_cagr')
analysis['roe_period'], analysis['roe_value'] = split_column('roe')


# Save
analysis.to_csv(os.path.join(folder_path, "clean_analysis.csv"), index=False)

print("✅ ANALYSIS CLEANED PERFECTLY")
print(analysis[['company','sales_value','profit_value','roe_value']].head())