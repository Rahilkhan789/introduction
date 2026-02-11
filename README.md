# Data Analyst Project: Retail Sales Performance

This project is a beginner-friendly portfolio project for aspiring **Data Analysts**.
It demonstrates how to:

- Clean and inspect CSV data
- Calculate business KPIs
- Segment performance by product category, city, and sales channel
- Answer common business questions using SQL
- Produce a reusable analysis report

## Project Structure

- `data/sales_data.csv` - Sample retail sales dataset
- `analysis/analysis.py` - Python script for KPI analysis and report generation
- `sql/analysis_queries.sql` - SQL queries for interview-style business questions
- `reports/summary_report.md` - Auto-generated summary report (created after running script)

## Skills Demonstrated

- Data cleaning basics (parsing and validation)
- Descriptive analytics and KPI tracking
- Grouped aggregations and ranking
- Business storytelling with metrics
- Basic SQL for analysis

## Dataset Columns

- `order_id`
- `order_date`
- `city`
- `channel`
- `category`
- `product`
- `units_sold`
- `unit_price`
- `discount_pct`

## Key Questions Answered

1. What is total revenue and average order value?
2. Which category drives the highest revenue?
3. Which city has the strongest sales performance?
4. How do online and offline channels compare?
5. What are the top 5 products by revenue?

## How to Run

```bash
python3 analysis/analysis.py
```

The script reads the CSV file, computes KPIs, and writes a report to:

- `reports/summary_report.md`

## Suggested Next Steps (Portfolio Upgrade)

- Add data visualization (Matplotlib / Seaborn / Power BI)
- Expand data volume and include missing values/outliers
- Create a dashboard view (e.g., Streamlit or Tableau)
- Add cohort analysis or month-over-month growth tracking

---

If you're applying for junior analyst roles, this is a great starting project to showcase practical analytics workflow.
