#!/usr/bin/env python3
"""Convert Philippine budget JSON data to CSV format for analysis."""

import json
import csv
from pathlib import Path

def convert_budget_to_csv(input_file: Path, output_file: Path):
    """Convert budget JSON to CSV."""
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Extract relevant fields
    rows = []
    for item in data:
        row = {
            'id': item.get('id', ''),
            'budget_type': item.get('budget_type', ''),
            'fiscal_year': item.get('fiscal_year', ''),
            'amount': item.get('amount', 0),
            'description': item.get('description', ''),
            'prexc_fpap_id': item.get('prexc_fpap_id', ''),
            'org_uacs_code': item.get('org_uacs_code', ''),
            'region_code': item.get('region_code', ''),
            'funding_uacs_code': item.get('funding_uacs_code', ''),
            'object_uacs_code': item.get('object_uacs_code', ''),
        }
        rows.append(row)

    # Write CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Converted {len(rows)} records to {output_file}")
    return rows

def main():
    data_dir = Path("data/raw")
    output_dir = Path("data/clean")
    output_dir.mkdir(exist_ok=True)

    # Convert batch 1
    input_file = data_dir / "gaa_2024_batch_0001.json"
    output_file = output_dir / "gaa_2024.csv"

    if input_file.exists():
        rows = convert_budget_to_csv(input_file, output_file)

        # Print summary
        print(f"\nSummary:")
        print(f"- Total records: {len(rows)}")
        print(f"- Total budget amount: ₱{sum(r['amount'] for r in rows):,.2f}")
        print(f"- Unique departments: {len(set(r['org_uacs_code'] for r in rows if r['org_uacs_code']))}")
    else:
        print(f"File not found: {input_file}")

if __name__ == "__main__":
    main()
