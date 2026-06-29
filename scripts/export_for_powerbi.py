#!/usr/bin/env python3
"""Export Philippine budget data in Power BI-ready format."""

import pandas as pd
import sqlite3
from pathlib import Path

def main():
    csv_file = Path("data/clean/gaa_2024.csv")
    output_dir = Path("data/powerbi")
    output_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("POWER BI EXPORT")
    print("=" * 60)

    # Load data
    print("\n📦 Loading data...")
    df = pd.read_csv(csv_file, low_memory=False)

    # Load department mapping
    with open('data/raw/departments.json') as f:
        import json
        departments = {d['code']: d['description'] for d in json.load(f)}

    # Map department codes
    df['org_uacs_code'] = df['org_uacs_code'].fillna('').astype(str)
    df['dept_code'] = df['org_uacs_code'].str[:2]
    df['department'] = df['dept_code'].map(departments).fillna('Unknown')

    # Create summary by department
    print("\n📊 Creating department summary...")
    dept_summary = df.groupby('department').agg(
        total_budget=('amount', 'sum'),
        item_count=('amount', 'count'),
        avg_budget=('amount', 'mean'),
        max_budget=('amount', 'max'),
    ).reset_index()
    dept_summary = dept_summary.sort_values('total_budget', ascending=False)
    dept_summary['pct_of_total'] = (dept_summary['total_budget'] / dept_summary['total_budget'].sum() * 100).round(2)

    # Create summary by region
    print("\n🗺️ Creating region summary...")
    region_summary = df[df['region_code'].notna() & (df['region_code'] != '')].groupby('region_code').agg(
        total_budget=('amount', 'sum'),
        item_count=('amount', 'count'),
    ).reset_index()
    region_summary = region_summary.sort_values('total_budget', ascending=False)

    # Create detailed table for Power BI
    print("\n📋 Creating detailed table...")
    detailed = df[['id', 'department', 'description', 'amount', 'fiscal_year', 'region_code']].copy()
    detailed.columns = ['Budget_ID', 'Department', 'Description', 'Amount_PHP', 'Fiscal_Year', 'Region']

    # Export to Excel (Power BI loves Excel)
    excel_file = output_dir / "philippine_budget_2024.xlsx"
    print(f"\n💾 Exporting to {excel_file}...")

    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        # Summary sheet
        dept_summary.to_excel(writer, sheet_name='Department_Summary', index=False)

        # Region summary sheet
        region_summary.to_excel(writer, sheet_name='Region_Summary', index=False)

        # Detailed data sheet (first 10,000 rows for performance)
        detailed.head(10000).to_excel(writer, sheet_name='Detailed_Data', index=False)

        # Statistics sheet
        stats = pd.DataFrame({
            'Metric': ['Total Records', 'Total Budget (PHP)', 'Unique Departments', 'Unique Regions', 'Average Budget', 'Max Budget', 'Min Budget'],
            'Value': [
                len(df),
                f"₱{df['amount'].sum():,.2f}",
                df['department'].nunique(),
                df['region_code'].nunique(),
                f"₱{df['amount'].mean():,.2f}",
                f"₱{df['amount'].max():,.2f}",
                f"₱{df['amount'].min():,.2f}",
            ]
        })
        stats.to_excel(writer, sheet_name='Statistics', index=False)

    print(f"✅ Excel file created: {excel_file}")

    # Also export as CSV files for direct Power BI import
    print("\n📄 Exporting CSV files...")
    dept_summary.to_csv(output_dir / "department_summary.csv", index=False)
    region_summary.to_csv(output_dir / "region_summary.csv", index=False)
    detailed.head(10000).to_csv(output_dir / "detailed_data.csv", index=False)

    print(f"✅ CSV files created in {output_dir}/")

    # Print summary
    print("\n" + "=" * 60)
    print("POWER BI IMPORT INSTRUCTIONS")
    print("=" * 60)
    print("""
1. Open Power BI Desktop
2. Click "Get Data" → "Excel Workbook"
3. Select: data/powerbi/philippine_budget_2024.xlsx
4. Choose sheets:
   - Department_Summary (for department analysis)
   - Region_Summary (for geographic analysis)
   - Detailed_Data (for drill-down)
   - Statistics (for KPIs)
5. Click "Load"
    """)

    print("=" * 60)

if __name__ == "__main__":
    main()
