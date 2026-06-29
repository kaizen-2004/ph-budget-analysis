#!/usr/bin/env python3
"""Generate realistic Philippine national budget sample data for demonstration."""

import csv
import random
from pathlib import Path

# Real Philippine government departments
departments = [
    "Department of Education",
    "Department of Health",
    "Department of Public Works and Highways",
    "Department of National Defense",
    "Department of Social Welfare and Development",
    "Department of Agriculture",
    "Department of Finance",
    "Department of Justice",
    "Department of the Interior and Local Government",
    "Department of Trade and Industry",
    "Department of Science and Technology",
    "Department of Transportation",
    "Department of Environment and Natural Resources",
    "Department of Labor and Employment",
    "Department of Agrarian Reform",
    "Department of Tourism",
    "Department of Energy",
    "Department of Foreign Affairs",
    "Department of Budget and Management",
    "Department of Information and Communications Technology",
]

# Budget categories
categories = [
    "Personnel Services",
    "MOOE (Maintenance and Other Operating Expenses)",
    "Capital Outlays",
    "Financial Expenses",
]

def generate_budget_data(year: int) -> list[dict]:
    """Generate realistic budget data for a given year."""
    rows = []
    base_budget = 4_000_000_000_000  # ~4 trillion PHP base

    for dept in departments:
        # Each department gets a portion of the budget
        dept_base = base_budget * random.uniform(0.02, 0.12)

        for cat in categories:
            if cat == "Personnel Services":
                amount = dept_base * random.uniform(0.4, 0.6)
            elif cat == "MOOE (Maintenance and Other Operating Expenses)":
                amount = dept_base * random.uniform(0.2, 0.35)
            elif cat == "Capital Outlays":
                amount = dept_base * random.uniform(0.1, 0.25)
            else:  # Financial Expenses
                amount = dept_base * random.uniform(0.02, 0.08)

            # Add some data quality issues for realism
            actual_amount = amount

            rows.append({
                "Department": dept,
                "Category": cat,
                "Year": year,
                "Amount_PHP": round(actual_amount, 2),
                "Status": random.choice(["Approved", "Released", "Obligated", "Disbursed"]),
            })

    return rows

def inject_data_issues(rows: list[dict]) -> list[dict]:
    """Inject realistic data quality issues."""
    for i, row in enumerate(rows):
        # Random missing values (5% chance)
        if random.random() < 0.05:
            row["Amount_PHP"] = ""

        # Random encoding issues (represent as special chars)
        if random.random() < 0.03:
            row["Department"] = row["Department"].replace("Department", "Dept.")

        # Random duplicates (3% chance)
        if random.random() < 0.03:
            row["Status"] = row["Status"]  # Duplicate status

    return rows

def main():
    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate data for multiple years (with some quality issues)
    for year in range(2015, 2025):
        rows = generate_budget_data(year)
        rows = inject_data_issues(rows)

        filename = output_dir / f"national_budget_{year}.csv"

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Department", "Category", "Year", "Amount_PHP", "Status"])
            writer.writeheader()
            writer.writerows(rows)

        print(f"Generated: {filename} ({len(rows)} rows)")

    # Create one messy file with different encoding issues
    messy_filename = output_dir / "budget_2020_messy.csv"
    with open(messy_filename, "w", newline="", encoding="latin-1") as f:
        writer = csv.DictWriter(f, fieldnames=["Department", "Category", "Year", "Amount_PHP", "Status"])
        writer.writeheader()
        for row in generate_budget_data(2020):
            # Add extra whitespace
            row["Department"] = f"  {row['Department']}  "
            # Add inconsistent category names
            if row["Category"] == "MOOE (Maintenance and Other Operating Expenses)":
                row["Category"] = "MOOE"
            writer.writerow(row)

    print(f"\nGenerated messy file: {messy_filename}")
    print("\nData generation complete!")

if __name__ == "__main__":
    main()
