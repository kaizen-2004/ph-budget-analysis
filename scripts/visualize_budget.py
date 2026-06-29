#!/usr/bin/env python3
"""Visualize Philippine budget data with matplotlib."""

import pandas as pd
import matplotlib.pyplot as plt
import json
from pathlib import Path

def main():
    csv_file = Path("data/clean/gaa_2024.csv")
    output_dir = Path("data/charts")
    output_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("BUDGET VISUALIZATION")
    print("=" * 60)

    # Load data
    print("\n📦 Loading data...")
    df = pd.read_csv(csv_file, low_memory=False)

    # Load department mapping
    with open('data/raw/departments.json') as f:
        departments = {d['code']: d['description'] for d in json.load(f)}

    # Map department codes
    df['org_uacs_code'] = df['org_uacs_code'].fillna('').astype(str)
    df['dept_code'] = df['org_uacs_code'].str[:2]
    df['department'] = df['dept_code'].map(departments).fillna('Unknown')

    # Create visualizations
    print("\n📊 Creating charts...")

    # Set style
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Philippine National Budget 2024 Analysis', fontsize=16, fontweight='bold')

    # Chart 1: Budget by Department (Pie Chart)
    dept_budget = df.groupby('department')['amount'].sum().sort_values(ascending=False).head(6)
    colors = ['#0071E3', '#34C759', '#FF9500', '#FF3B30', '#AF52DE', '#5856D6']
    axes[0, 0].pie(dept_budget.values, labels=dept_budget.index, autopct='%1.1f%%', colors=colors, startangle=90)
    axes[0, 0].set_title('Budget Distribution by Department')

    # Chart 2: Top 10 Departments (Bar Chart)
    dept_budget_top10 = df.groupby('department')['amount'].sum().sort_values(ascending=True).tail(10)
    axes[0, 1].barh(dept_budget_top10.index, dept_budget_top10.values, color='#0071E3')
    axes[0, 1].set_xlabel('Budget (PHP)')
    axes[0, 1].set_title('Top 10 Departments by Budget')
    axes[0, 1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₱{x/1e6:.0f}M'))

    # Chart 3: Budget by Region (Bar Chart)
    region_budget = df[df['region_code'].notna() & (df['region_code'] != '')].groupby('region_code')['amount'].sum().sort_values(ascending=True).tail(10)
    axes[1, 0].barh([f'Region {r}' for r in region_budget.index], region_budget.values, color='#34C759')
    axes[1, 0].set_xlabel('Budget (PHP)')
    axes[1, 0].set_title('Top 10 Regions by Budget')
    axes[1, 0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'₱{x/1e6:.0f}M'))

    # Chart 4: Budget Distribution (Histogram)
    axes[1, 1].hist(df['amount'].clip(upper=df['amount'].quantile(0.95)), bins=50, color='#FF9500', edgecolor='white')
    axes[1, 1].set_xlabel('Budget Amount (PHP)')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].set_title('Budget Distribution (excluding outliers)')

    plt.tight_layout()
    chart_file = output_dir / 'budget_analysis.png'
    plt.savefig(chart_file, dpi=150, bbox_inches='tight')
    print(f"✅ Saved: {chart_file}")

    # Show plot
    plt.show()

    # Create a summary table
    print("\n📊 Summary Statistics:")
    print(f"   Total Records: {len(df):,}")
    print(f"   Total Budget: ₱{df['amount'].sum():,.2f}")
    print(f"   Unique Departments: {df['department'].nunique()}")
    print(f"   Top Department: {dept_budget.index[0]} (₱{dept_budget.values[0]:,.2f})")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
