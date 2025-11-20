from datetime import datetime

report_file = "daily_report.md"

today = datetime.now().strftime("%Y-%m-%d")

entry = f"\n## {today}\n- Worked on feature updates\n- Fixed bugs\n- Updated modules\n"

with open(report_file, "a") as f:
    f.write(entry)

print("Daily report updated")
