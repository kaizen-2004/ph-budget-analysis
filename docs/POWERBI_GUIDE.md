# Power BI Import Guide

## Step 1: Open Power BI Desktop

Download from: https://powerbi.microsoft.com/desktop/
(Free version is enough)

## Step 2: Import Data

1. Click **Home** → **Get Data** → **Excel Workbook**
2. Navigate to: `/home/steve/projects/ph-budget-analysis/data/powerbi/`
3. Select: `philippine_budget_2024_full.xlsx`
4. Click **Open**

## Step 3: Select Sheets

In the Navigator window, check all 3 sheets:
- ☑️ Department_Summary
- ☑️ Region_Summary
- ☑️ Detailed_Data

Click **Transform Data** (not Load) to clean first

## Step 4: Transform Data (Power Query)

For each sheet:
1. Check data types (Amount should be Decimal)
2. Remove any blank rows
3. Click **Close & Apply**

## Step 5: Create Visualizations

### Chart 1: Budget by Department (Donut Chart)
1. Click **Donut Chart** from Visualizations pane
2. Drag `department` to **Legend**
3. Drag `total_budget` to **Values**
4. Click **Format** → turn on Data labels

### Chart 2: Budget by Region (Bar Chart)
1. Click **Stacked Bar Chart**
2. Drag `region` to **Y-axis**
3. Drag `total_budget` to **X-axis**
4. Sort by total_budget descending

### Chart 3: KPI Cards
1. Click **Card** visual
2. Drag `total_budget` to **Fields**
3. Format as currency (₱)
4. Create 3 cards:
   - Total Budget
   - Total Items
   - Average Budget

### Chart 4: Treemap (Department Breakdown)
1. Click **Treemap**
2. Drag `department` to **Group**
3. Drag `total_budget` to **Values**

## Step 6: Create Dashboard Page

1. Add a new page → rename to "Budget Dashboard"
2. Arrange visuals:
   - Top row: 3 KPI cards
   - Middle: Donut chart (left) + Bar chart (right)
   - Bottom: Treemap

## Step 7: Add Filters

1. Click **Slicer** visual
2. Drag `department` to **Field**
3. Now you can filter all charts by department

## Step 8: Export as PDF (for LinkedIn)

1. File → Export → PDF
2. Select: Current page
3. Click Export

## Quick SQL in Power BI (Optional)

If you want to write SQL queries:

1. Get Data → **SQLite Database**
2. Select: `data/clean/budget.db`
3. Write queries like:

```sql
SELECT
    department,
    SUM(amount) as total_budget,
    COUNT(*) as item_count
FROM budget
GROUP BY department
ORDER BY total_budget DESC
```

## Files Location

```
/home/steve/projects/ph-budget-analysis/data/powerbi/
├── philippine_budget_2024_full.xlsx   # Main file to import
├── department_summary_full.csv        # Alternative CSV
└── region_summary_full.csv            # Alternative CSV
```

## Tips

- Use **Format Painter** to match colors across visuals
- Add **Page Title**: "Philippine Budget 2024 Analysis"
- Use **Tooltips** to show additional info on hover
- Publish to Power BI Service for sharing online
