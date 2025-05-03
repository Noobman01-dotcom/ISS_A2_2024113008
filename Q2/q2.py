# Write answers for Q2 here
import os
import json
import csv

folder_path = "datasets"
all_keys = set()
key_value_rows = []

def extract_keys_and_values(data, parent_key=""):
    items = []
    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key
            all_keys.add(full_key)
            items.extend(extract_keys_and_values(value, full_key))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            full_key = f"{parent_key}[{i}]" if parent_key else f"[{i}]"
            items.extend(extract_keys_and_values(item, full_key))
    else:
        items.append((parent_key, data))
    return items

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                key_value_rows.extend(extract_keys_and_values(data))
            except Exception as e:
                print(f"Could not read {filename}: {e}")

print("All keys found:")
print(list(all_keys))

with open("output.csv", "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Key", "Value"])
    writer.writerows(key_value_rows)

print("✅ Done! Saved to output.csv")
