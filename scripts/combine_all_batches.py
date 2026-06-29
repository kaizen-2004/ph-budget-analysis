#!/usr/bin/env python3
"""Combine all 7 batches of Philippine budget data."""

import json
import pandas as pd
from pathlib import Path

def main():
    data_dir = Path("data/raw")
    output_dir = Path("data/clean")
    output_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("COMBINING ALL 7 BATCHES")
    print("=" * 60)

    all_data = []
    batch_stats = []

    for i in range(1, 8):
        batch_file = data_dir / f"gaa_2024_batch_000{i}.json"
        print(f"\n📦 Loading batch {i}: {batch_file.name}")

        with open(batch_file) as f:
            batch_data = json.load(f)

        batch_amount = sum(item.get('amount', 0) for item in batch_data)
        batch_stats.append({
            'batch': i,
            'records': len(batch_data),
            'amount': batch_amount
        })

        print(f"   Records: {len(batch_data):,}")
        print(f"   Amount: ₱{batch_amount:,.2f}")

        all_data.extend(batch_data)

    # Combine all data
    print(f"\n🔄 Combining all batches...")
    df = pd.DataFrame(all_data)

    # Save combined CSV
    output_file = output_dir / "gaa_2024_full.csv"
    df.to_csv(output_file, index=False)

    print(f"\n✅ Combined data saved to: {output_file}")
    print(f"   Total records: {len(df):,}")
    print(f"   Total budget: ₱{df['amount'].sum():,.2f}")

    # Print batch summary
    print("\n" + "=" * 60)
    print("BATCH SUMMARY")
    print("=" * 60)
    print(f"{'Batch':<8} {'Records':<12} {'Amount (PHP)':<20}")
    print("-" * 40)
    for stat in batch_stats:
        print(f"{stat['batch']:<8} {stat['records']:<12,} ₱{stat['amount']:>15,.2f}")
    print("-" * 40)
    print(f"{'TOTAL':<8} {sum(s['records'] for s in batch_stats):<12,} ₱{sum(s['amount'] for s in batch_stats):>15,.2f}")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
