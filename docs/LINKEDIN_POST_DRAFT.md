# LinkedIn Post Draft: Philippine Budget Data Analysis (Full)

## Post Content

---

I downloaded 682,814 Philippine government budget records and analyzed them using Python, SQL, and Linux commands. Here's the full picture:

**The Data:**
- Source: BetterGov.PH (official GAA 2024 data from COA/DBM)
- Records: 682,814 budget line items
- Total Budget: ₱11.5 BILLION (sample from 7 batches)
- Format: JSON → CSV → SQLite

**The Stack:**
🔧 Linux CLI - Download and exploration
🐍 Python + pandas - Data transformation
🗄️ SQL (SQLite) - Aggregation and analysis

**Top 5 Budget Allocations:**

| Department | Budget | % |
|------------|--------|---|
| DPWH (Public Works) | ₱997.9M | 8.7% |
| DILG (Interior) | ₱265.5M | 2.3% |
| DSWD (Social Welfare) | ₱258.8M | 2.2% |
| DOH (Health) | ₱246.7M | 2.1% |
| DND (Defense) | ₱242.4M | 2.1% |

**Key Insights:**
- DPWH gets the largest share - infrastructure is prioritized
- NCR (Region 13) gets ₱2.57 BILLION - 22% of total
- Education (DepEd) data shows ₱8.7B in "Unknown" category - needs deeper investigation
- 152,627 items have zero budget (carry-over or contingency)

**What I learned:**
1. Real government data is messy - 150K+ records missing department codes
2. Data cleaning is 80% of the work
3. Linux + Python + SQL = powerful combo for quick analysis

**Tools used:**
✅ Linux (curl, cut, sort, grep)
✅ Python 3.12 (pandas, json, sqlite3)
✅ SQLite for SQL queries
✅ Git for version control
✅ Power BI for visualization

No Tableau. No expensive licenses. Just code.

What's your go-to data stack? Drop it below 👇

---

**Data Source:** BetterGov.PH Open Budget Data
**Repository:** github.com/bettergovph/open-budget-data

---

## Key Numbers for Screenshots

| Metric | Value |
|--------|-------|
| Total Records | 682,814 |
| Total Budget | ₱11,535,200,000 |
| Unique Departments | 29 |
| Top Department | DPWH (₱997.9M) |
| Top Region | NCR (₱2.57B) |

## Hashtags

#Python #SQL #Linux #DataEngineering #Philippines #OpenData #DataAnalysis #PublicFinance #TechForGood
