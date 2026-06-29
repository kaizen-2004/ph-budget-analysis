# Screenshots Guide for LinkedIn Post

## Story: "From JSON Chaos to Clean Analysis"

### Screenshot 1: The Messy Data
**Command:** `ls -lh data/raw/`
**Shows:** Large JSON files (38MB each) - "100,000+ budget records locked in JSON"

### Screenshot 2: Preview Raw Data
**Command:** `head -5 data/raw/gaa_2024_batch_0001.json`
**Shows:** Complex nested JSON structure - "Good luck analyzing this directly"

### Screenshot 3: File Size Comparison
**Command:** `du -h data/raw/* data/clean/*`
**Shows:** Raw vs cleaned data sizes

### Screenshot 4: Quick Analysis with Linux Tools
**Command:** `cut -d',' -f4 data/clean/gaa_2024.csv | sort -rn | head -10`
**Shows:** Top 10 budget amounts

### Screenshot 5: Count Unique Departments
**Command:** `cut -d',' -f7 data/clean/gaa_2024.csv | sort -u | wc -l`
**Shows:** Number of unique departments

### Screenshot 6: Before vs After
**Side by side:** Left = raw JSON, Right = clean CSV

---

## LinkedIn Post Structure

### Hook (First Line)
"I downloaded 100,000+ Philippine government budget records and cleaned them with Linux commands. Here's what I found:"

### Problem
"The data was locked in 38MB JSON files with nested structures. No expensive software needed."

### Solution (Linux Commands)
```bash
# Preview the chaos
head -5 data/raw/gaa_2024_batch_0001.json

# Convert to analysis-ready CSV
python3 scripts/convert_to_csv.py

# Quick insights without opening Excel
cut -d',' -f4 data/clean/gaa_2024.csv | sort -rn | head -5
```

### Key Findings
- Total budget: ₱670.8M (sample batch)
- 1,365 unique budget items
- Largest allocation: General Administration

### Call to Action
"What data project are you working on? Drop it below 👇"

---

## Screenshot Commands (Copy-Paste Ready)

```bash
# 1. Show raw files
ls -lh data/raw/

# 2. Preview JSON
head -3 data/raw/gaa_2024_batch_0001.json

# 3. Show CSV size
wc -l data/clean/gaa_2024.csv

# 4. Top 5 budget items
cut -d',' -f4,5 data/clean/gaa_2024.csv | sort -t',' -k1 -rn | head -5

# 5. Unique departments
cut -d',' -f7 data/clean/gaa_2024.csv | sort -u | head -20

# 6. File comparison
echo "=== Before ===" && du -h data/raw/* && echo "=== After ===" && du -h data/clean/*
```
