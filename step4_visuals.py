import pandas as pd
import matplotlib.pyplot as plt
import os

# 📁 Folder path
folder_path = r"E:\BOLDANAYSTICSCOMPANY\PROJECT2STOCKMARKETANAYSIS\DATASET2"

# 📂 Load cleaned file
file_path = os.path.join(folder_path, "clean_analysis.csv")
df = pd.read_csv(file_path)

print("✅ File loaded")

# --------------------------
# CLEAN FINAL (safety)
# --------------------------
df.columns = df.columns.str.strip().str.lower()

# Remove null values
df = df.dropna(subset=['company', 'sales_value', 'profit_value', 'roe_value'])

# --------------------------
# SAVE PATH
# --------------------------
os.chdir(folder_path)

# --------------------------
# CHART 1 — TOP SALES
# --------------------------
top_sales = df.sort_values(by='sales_value', ascending=False).head(10)

plt.figure()
plt.bar(top_sales['company'], top_sales['sales_value'])
plt.xticks(rotation=45)
plt.title("Top 10 Sales Growth")
plt.tight_layout()
plt.savefig("top_sales.png")
plt.close()

print("📊 top_sales.png saved")

# --------------------------
# CHART 2 — TOP PROFIT
# --------------------------
top_profit = df.sort_values(by='profit_value', ascending=False).head(10)

plt.figure()
plt.bar(top_profit['company'], top_profit['profit_value'])
plt.xticks(rotation=45)
plt.title("Top 10 Profit Growth")
plt.tight_layout()
plt.savefig("top_profit.png")
plt.close()

print("📊 top_profit.png saved")

# --------------------------
# CHART 3 — TOP ROE
# --------------------------
top_roe = df.sort_values(by='roe_value', ascending=False).head(10)

plt.figure()
plt.bar(top_roe['company'], top_roe['roe_value'])
plt.xticks(rotation=45)
plt.title("Top 10 ROE")
plt.tight_layout()
plt.savefig("top_roe.png")
plt.close()

print("📊 top_roe.png saved")

print("\n🎉 ALL CHARTS CREATED SUCCESSFULLY")