import pandas as pd

# Load all cleaned files
analysis = pd.read_csv("clean_analysis.csv")
balance = pd.read_csv("clean_balancesheet.csv")
cashflow = pd.read_csv("clean_cashflow.csv")
pl = pd.read_csv("clean_profitandloss.csv")

print("Files Loaded Successfully ✅")

# -----------------------------
# BASIC CHECK
# -----------------------------
print("\nAnalysis Data:")
print(analysis.head())

print("\nBalance Sheet Data:")
print(balance.head())

# -----------------------------
# SIMPLE ANALYSIS (IMPORTANT OUTPUT)
# -----------------------------

# 1. Top companies by ROE
if 'roe_value' in analysis.columns:
    top_roe = analysis.sort_values(by='roe_value', ascending=False).head(10)
    print("\nTop Companies by ROE:")
    print(top_roe[['company_1', 'roe_value']])

# 2. Top companies by Profit Growth
if 'profit_value' in analysis.columns:
    top_profit = analysis.sort_values(by='profit_value', ascending=False).head(10)
    print("\nTop Companies by Profit Growth:")
    print(top_profit[['company_1', 'profit_value']])

# 3. Top companies by Sales Growth
if 'sales_value' in analysis.columns:
    top_sales = analysis.sort_values(by='sales_value', ascending=False).head(10)
    print("\nTop Companies by Sales Growth:")
    print(top_sales[['company_1', 'sales_value']])

# -----------------------------
# SAVE FINAL OUTPUT
# -----------------------------
analysis.to_csv("final_analysis_output.csv", index=False)

print("\n✅ Final Output Saved: final_analysis_output.csv")