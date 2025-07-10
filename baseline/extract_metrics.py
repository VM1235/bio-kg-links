import re
import ast
import csv

# Step 1: Read raw text
with open('baseline/transE_metrics.txt', 'r') as f:
    raw = f.read().strip()

# Step 2: Insert commas between top-level sections (head, tail, both)
cleaned = re.sub(r'(\bhead|\btail|\bboth):', r"'\1':", raw)  # quote top-level keys
cleaned = re.sub(r"(?<=\})\s*(?='(head|tail|both)')", ",\n", cleaned)  # insert comma between dicts

# Step 3: Wrap in {}
cleaned = "{" + cleaned + "}"

# Step 4: Parse as Python dict
try:
    metrics = ast.literal_eval(cleaned)
except Exception as e:
    print("❌ Failed to parse metrics:", e)
    exit()

# Step 5: Extract hits@k to CSV
with open('baseline/transE_hits_summary.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Split', 'View', 'Hits@1', 'Hits@3', 'Hits@5', 'Hits@10'])

    for split in metrics:
        for view in metrics[split]:
            data = metrics[split][view]
            writer.writerow([
                split,
                view,
                data.get('hits_at_1', 'N/A'),
                data.get('hits_at_3', 'N/A'),
                data.get('hits_at_5', 'N/A'),
                data.get('hits_at_10', 'N/A'),
            ])

print("✅ Successfully saved to baseline/transE_hits_summary.csv")
