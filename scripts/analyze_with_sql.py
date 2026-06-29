#!/usr/bin/env python3
"""Analyze Philippine budget data using SQL."""

import sqlite3
import pandas as pd
from pathlib import Path

def main():
    csv_file = Path("data/clean/gaa_2024.csv")
    db_file = Path("data/clean/budget.db")

    print("=" * 60)
    print("SQL ANALYSIS")
    print("=" * 60)

    # Load CSV into SQLite
    print("\n📦 Loading CSV into SQLite...")
    df = pd.read_csv(csv_file)

    conn = sqlite3.connect(db_file)
    df.to_sql('budget', conn, if_exists='replace', index=False)
    print(f"   Loaded {len(df)} records into {db_file}")

    # Query 1: Total budget
    print("\n💰 Query 1: Total Budget")
    result = conn.execute("SELECT SUM(amount) as total FROM budget").fetchone()
    print(f"   Total: ₱{result[0]:,.2f}")

    # Query 2: Top 5 departments
    print("\n📊 Query 2: Top 5 Departments")
    query = """
        SELECT
            org_uacs_code,
            COUNT(*) as item_count,
            SUM(amount) as total_budget,
            ROUND(SUM(amount) * 100.0 / (SELECT SUM(amount) FROM budget), 2) as percentage
        FROM budget
        WHERE org_uacs_code IS NOT NULL AND org_uacs_code != ''
        GROUP BY org_uacs_code
        ORDER BY total_budget DESC
        LIMIT 5
    """
    results = conn.execute(query).fetchall()
    for row in results:
        print(f"   {row[0]}: ₱{row[2]:>15,.2f} ({row[3]}%) - {row[1]} items")

    # Query 3: Budget by region
    print("\n🗺️ Query 3: Budget by Region")
    query = """
        SELECT
            region_code,
            SUM(amount) as total_budget
        FROM budget
        WHERE region_code IS NOT NULL AND region_code != ''
        GROUP BY region_code
        ORDER BY total_budget DESC
        LIMIT 5
    """
    results = conn.execute(query).fetchall()
    for row in results:
        print(f"   Region {row[0]}: ₱{row[1]:>15,.2f}")

    # Query 4: Average budget per item
    print("\n📈 Query 4: Statistics")
    query = """
        SELECT
            COUNT(*) as total_items,
            AVG(amount) as avg_budget,
            MAX(amount) as max_budget,
            MIN(amount) as min_budget
        FROM budget
    """
    result = conn.execute(query).fetchone()
    print(f"   Total items: {result[0]:,}")
    print(f"   Average budget: ₱{result[1]:,.2f}")
    print(f"   Max budget: ₱{result[2]:,.2f}")
    print(f"   Min budget: ₱{result[3]:,.2f}")

    conn.close()
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
