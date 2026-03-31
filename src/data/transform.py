import json

with open("accepted.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

results = []
for line in lines:
    line = line.strip()
    if not line:
        continue

    # Remove leading number and period (e.g., "1. ")
    idx = line.find(". ")
    if idx == -1:
        continue
    rest = line[idx + 2 :]

    # Split on semicolon to separate title from authors
    parts = rest.split("; ", 1)
    if len(parts) != 2:
        continue

    title = parts[0].strip()
    authors_str = parts[1].strip()

    # Split authors by comma, then also handle " and " between last two
    authors_raw = authors_str.split(", ")
    authors = []
    for a in authors_raw:
        # Handle " X and Y" pattern at the end
        and_idx = a.rfind(" and ")
        if and_idx != -1:
            authors.append(a[:and_idx].strip())
            authors.append(a[and_idx + 5 :].strip())
        else:
            authors.append(a.strip())

    results.append({"title": title, "authors": authors})

# Write to JSONL
with open("accepted.jsonl", "w", encoding="utf-8") as f:
    for entry in results:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

print(f"Processed {len(results)} entries")
