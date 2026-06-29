#!/usr/bin/env python3
"""Analyze Philippine budget data using Python + pandas."""

import json
import pandas as pd
from pathlib import Path

def main():
    # Load data
    json_file = Path("data/raw/gaa_2024_batch_0001.json")
    csv_file = Path("data/clean/gaa_2024.csv")

    print("=" * 60)
    print("PYTHON + PANDAS ANALYSIS")
    print("=" * 60)

    # Load from JSON
    print("\n📦 Loading JSON data...")
    with open(json_file) as f:
        data = json.load(f)
    print(f"   Loaded {len(data)} records")

    # Convert to DataFrame
    print("\n🔄 Converting to DataFrame...")
    df = pd.DataFrame(data)
    print(f"   Shape: {df.shape}")
    print(f"   Columns: {list(df.columns)}")

    # Basic stats
    print("\n📊 Basic Statistics:")
    print(f"   Total records: {len(df):,}")
    print(f"   Total budget: ₱{df['amount'].sum():,.2f}")

    # Department analysis
    print("\n💰 Budget by Department (Top 10):")
    # Extract department code from org_uacs_code
    df['dept_code'] = df['org_uacs_code'].str[:2]
    dept_budget = df.groupby('dept_code')['amount'].sum().sort_values(ascending=False).head(10)

    # Load department names
    with open('data/raw/departments.json') as f:
        departments = {d['code']: d['abbreviation'] for d in json.load(f)}

    for code, amount in dept_budget.items():
        dept_name = departments.get(code, f'Dept {code}')
        pct = (amount / df['amount'].sum()) * 100
        print(f"   {dept_name}: ₱{amount:>15,.2f} ({pct:.1f}%)")

    # Save to CSV
    print("\n💾 Saving to CSV...")
    df.to_csv(csv_file, index=False)
    print(f"   Saved to {csv_file}")

    # Quick analysis
    print("\n📈 Quick Analysis:")
    print(f"   Mean budget per item: ₱{df['amount'].mean():,.2f}")
    print(f"   Max budget item: ₱{df['amount'].max():,.2f}")
    print(f"   Min budget item: ₱{df['amount'].min():,.2f}")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
