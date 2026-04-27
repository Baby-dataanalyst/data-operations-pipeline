import pandas as pd
from datetime import date

# ------------------------------------------
# STEP 1: Load your dataset
# ------------------------------------------
df = pd.read_csv("pipeline_output.csv")

today = str(date.today())

# ------------------------------------------
# STEP 2: Filter for today's data
# ------------------------------------------
df["load_date"] = pd.to_datetime(df["load_timestamp"]).dt.date.astype(str)
df_today = df[df["load_date"] == today]

total_records = len(df_today)

# ------------------------------------------
# STEP 3: Check duplicates
# ------------------------------------------
duplicates = df_today[df_today.duplicated(subset=["customer_id"], keep=False)]
duplicate_count = len(duplicates)

# ------------------------------------------
# STEP 4: Check nulls
# ------------------------------------------
null_summary = df_today.isnull().sum()

# ------------------------------------------
# STEP 5: Check job status counts
# ------------------------------------------
status_summary = df_today["status"].value_counts()

# ------------------------------------------
# STEP 6: Generate report
# ------------------------------------------
report_lines = []
report_lines.append(f"Pipeline Validation Report — {today}")
report_lines.append("=" * 45)
report_lines.append(f"Total records loaded today : {total_records}")
report_lines.append(f"Duplicate records found    : {duplicate_count}")
report_lines.append("")
report_lines.append("Null Value Summary:")
for col, count in null_summary.items():
    report_lines.append(f"  {col}: {count} nulls")
report_lines.append("")
report_lines.append("Status Breakdown:")
for status, count in status_summary.items():
    report_lines.append(f"  {status}: {count}")
report_lines.append("")

# Flag issues
if total_records == 0:
    report_lines.append("ALERT: No data loaded today. Raise incident.")
elif duplicate_count > 0:
    report_lines.append(f"WARNING: {duplicate_count} duplicate records found.")
else:
    report_lines.append("All checks passed. Pipeline healthy.")

# ------------------------------------------
# STEP 7: Save report to file
# ------------------------------------------
report_text = "\n".join(report_lines)
filename = f"pipeline_report_{today}.txt"

with open(filename, "w") as f:
    f.write(report_text)

print(report_text)
print(f"\nReport saved as: {filename}")