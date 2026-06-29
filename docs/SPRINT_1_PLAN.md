# Sprint 1: Data Collection & Setup

**Sprint Goal:** Download and explore Philippine budget data to understand structure and quality issues.

**Duration:** 1-2 hours

---

## Tasks

### Task 1.1: Download Budget Data
- [ ] Find and download Philippine national budget CSV data
- [ ] Store in `data/raw/` directory
- [ ] Document data source and date downloaded

### Task 1.2: Explore Raw Data
- [ ] Preview each CSV file (head, tail, wc)
- [ ] Check file sizes and row counts
- [ ] Identify encoding issues
- [ ] Document column names and data types

### Task 1.3: Document Data Quality Issues
- [ ] List missing values
- [ ] Identify duplicates
- [ ] Note inconsistent formats
- [ ] Create quality report in `docs/DATA_QUALITY.md`

---

## Deliverables
1. Raw CSV files in `data/raw/`
2. Data exploration notes
3. Data quality report

## Screenshots to Capture
1. `ls -la data/raw/` - showing downloaded files
2. `head -20 data/raw/budget_2024.csv` - preview of raw data
3. `csvstat data/raw/budget_2024.csv` - data statistics
