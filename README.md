# E-Commerce Sales Analytics

SQL + Python analysis of the [Olist Brazilian E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (~99,000 orders). Built a relational database from raw CSVs in MySQL, resolved real data quality issues (inconsistent date formats, missing values, malformed text fields), and used SQL + Python to answer business questions on revenue, customer satisfaction, delivery performance, and customer retention.

**Tools:** MySQL, Python (pandas, SQLAlchemy)

## What's in this repo
- `E-Commerce Sales Analytics — SQL Business Insights.pdf` — 5 SQL business questions with query screenshots and insights
- `rfm_analysis.py` — Python script for RFM (Recency, Frequency, Monetary) customer segmentation
- `rfm_output.csv` — segmentation output per customer
- `load_reviews.py` — script used to load a free-text CSV that MySQL's native loader couldn't parse
- `screenshots/` — proof-of-work screenshots from the MySQL import and analysis process

## Key Findings

**1. Order fulfillment:** 97% of orders were successfully delivered — used as the filter baseline for all revenue analysis.

**2. Revenue trend:** Revenue grew ~9x from Jan 2017 (R$127K) to Nov 2017 (R$1.15M), then plateaued around R$1.0M–1.13M/month through mid-2018 — signaling a shift from growth phase to maturity phase.

**3. Category economics:** `beleza_saude` (health & beauty) leads through volume (8,647 orders), while `relogios_presentes` (watches & gifts) has nearly 2x the average order value (R$212 vs. ~R$110) of high-volume categories — showing two distinct revenue strategies at play.

**4. Customer satisfaction:** Book categories dominate satisfaction ratings (4.37★–4.45★) despite not ranking in the top-10 revenue categories — a satisfaction-revenue mismatch worth exploring for loyalty/cross-sell strategy.

**5. Delivery performance:** 92% of deliveries arrive on time or early (avg. 13.7 days ahead of estimate); the remaining 8% arrive ~9 days late on average.

**6. Customer retention (RFM segmentation):** 97% of customers made only a single purchase — just 3% ever returned. However, repeat buyers spend nearly 2x more on average (R$308 vs. R$160), indicating a retention problem rather than a value problem. Converting even a small share of one-time buyers into repeat customers would be a high-leverage growth lever.
