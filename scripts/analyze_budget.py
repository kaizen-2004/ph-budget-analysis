#!/usr/bin/env python3
"""Analyze Philippine budget data and generate insights for LinkedIn post."""

import csv
import json
from pathlib import Path
from collections import defaultdict

def load_departments(dept_file: Path) -> dict:
    """Load department code to name mapping."""
    with open(dept_file, 'r') as f:
        departments = json.load(f)
    return {d['code']: d['description'] for d in departments}

def analyze_budget(csv_file: Path, dept_mapping: dict):
    """Analyze budget data and return insights."""
    departments = defaultdict(float)
    total_amount = 0
    row_count = 0

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            amount = float(row.get('amount', 0) or 0)
            org_code = row.get('org_uacs_code', '')
            # Extract first 2 digits as department code
            dept_code = org_code[:2] if org_code else ''

            dept_name = dept_mapping.get(dept_code, f'Dept {dept_code}')

            departments[dept_name] += amount
            total_amount += amount
            row_count += 1

    # Get top 10 departments
    top_departments = sorted(departments.items(), key=lambda x: x[1], reverse=True)[:10]

    return {
        'total_records': row_count,
        'total_budget': total_amount,
        'unique_departments': len(departments),
        'top_departments': top_departments,
    }

def print_insights(insights: dict):
    """Print formatted insights."""
    print("=" * 60)
    print("PHILIPPINE NATIONAL BUDGET 2024 - ANALYSIS")
    print("=" * 60)

    print(f"\n📊 DATA OVERVIEW")
    print(f"   Total Records: {insights['total_records']:,}")
    print(f"   Total Budget: ₱{insights['total_budget']:,.2f}")
    print(f"   Unique Departments: {insights['unique_departments']:,}")

    print(f"\n💰 TOP 10 BUDGET ALLOCATIONS")
    print("-" * 60)
    for i, (dept, amount) in enumerate(insights['top_departments'], 1):
        percentage = (amount / insights['total_budget']) * 100 if insights['total_budget'] > 0 else 0
        print(f"   {i:2d}. {dept}: ₱{amount:>15,.2f} ({percentage:.1f}%)")

    print("\n" + "=" * 60)

def main():
    csv_file = Path("data/clean/gaa_2024.csv")
    dept_file = Path("data/raw/departments.json")

    if csv_file.exists() and dept_file.exists():
        dept_mapping = load_departments(dept_file)
        insights = analyze_budget(csv_file, dept_mapping)
        print_insights(insights)

        # Save insights to file
        output_file = Path("docs/INSIGHTS.md")
        with open(output_file, 'w') as f:
            f.write("# Philippine Budget 2024 - Key Insights\n\n")
            f.write(f"**Total Records:** {insights['total_records']:,}\n\n")
            f.write(f"**Total Budget:** ₱{insights['total_budget']:,.2f}\n\n")
            f.write(f"**Unique Departments:** {insights['unique_departments']:,}\n\n")
            f.write("## Top 10 Budget Allocations\n\n")
            f.write("| Rank | Department | Amount | Percentage |\n")
            f.write("|------|------------|--------|------------|\n")
            for i, (dept, amount) in enumerate(insights['top_departments'], 1):
                percentage = (amount / insights['total_budget']) * 100 if insights['total_budget'] > 0 else 0
                f.write(f"| {i} | {dept} | ₱{amount:,.2f} | {percentage:.1f}% |\n")

        print(f"\n✅ Insights saved to {output_file}")
    else:
        print(f"❌ Required files not found")

if __name__ == "__main__":
    main()
