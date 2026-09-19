# Project FORESIGHT — Demand & Inventory Intelligence

## 1. Project Overview

**Client:** NorthBay Living  
**Project:** FORESIGHT — Demand & Inventory Intelligence  
**Role:** Data Scientist / Analytics  
**Domain:** D2C Home & Lifestyle  
**Dataset:** Synthetic training/demo dataset  
**Period:** 2024-01-01 to 2025-12-31

Project FORESIGHT is an analytics solution designed to help an inventory team answer three practical questions:

1. What is likely to sell next?
2. Which products are at risk of stockout?
3. Which products are overstocked and may need clearance?

The project brief requires a reproducible data pipeline, EDA, SKU-level forecasting, transparent inventory risk scoring, a planning dashboard, a scoring service, and an executive readout.

## 2. Business Problem

NorthBay Living currently relies heavily on spreadsheets and judgement for inventory planning. This creates two opposite risks:

- **Stockouts:** popular products run out, causing potential lost sales.
- **Overstock:** slow-moving products accumulate, tying up working capital and potentially requiring markdowns.

FORESIGHT converts sales, demand and inventory information into planning-oriented outputs for operations and finance.

## 3. Dataset

The supplied workbook contains the following main sheets:

- `Raw_Data` — transaction/day-level sales, demand, inventory and planning fields.
- `SKU_Summary` — SKU/category-level summary information.
- `Daily_Summary` — daily aggregate summary.
- `Forecast_Recommendations` — forecast and inventory recommendations.
- `Overview` — dataset and project metadata.

### Dataset profile

| Metric | Value |
|---|---:|
| Rows | 3,000 |
| Unique SKUs | 100 |
| Categories | 5 |
| Regions | 4 |
| Date range | 2024-01-01 to 2025-12-31 |
| Total demand units | 107,885 |
| Total sales units | 106,385 |
| Total revenue | ₹269,682,326.67 |
| Stockout records | 31 |
| Overstock records | 507 |
| Recommended order quantity | 373,375 units |

## 4. Data Quality

The supplied `Raw_Data` sheet was checked for basic completeness and duplication:

- Missing values: **none found**
- Duplicate rows: **none found**
- Date field is available across the stated analysis period.

The project brief asks for coded handling of missing values, duplicates and data types in a reproducible pipeline. The current workbook documents the cleaned/analysis-ready data, while a production implementation should keep those cleaning checks in code.

## 5. Key EDA Findings

### Revenue and demand by category

- **Grocery** is the strongest category by both revenue and demand. It generated approximately **₹8.61 crore** in revenue and **33,396 demand units**.
- **Personal Care** generated approximately **₹6.25 crore** and **25,619 demand units**.
- **Apparel** generated approximately **₹4.89 crore** and **20,100 demand units**.
- **Home & Kitchen** generated approximately **₹4.42 crore** and **17,806 demand units**.
- **Electronics** generated approximately **₹2.80 crore** and **10,964 demand units**.

### Inventory risk

- Grocery has the highest number of recorded stockout events (**19**), indicating that replenishment deserves close attention.
- Electronics has the largest overstock burden (**281 records**), suggesting inventory is tied up in slower-moving products.
- Home & Kitchen also shows a significant overstock burden (**150 records**).

These findings support two different operational priorities: protect availability for high-demand products while reducing excess inventory in slower-moving areas.

## 6. Forecasting Approach

The engagement brief specifies:

1. Define the forecast horizon and WAPE metric.
2. Build a seasonal-naive baseline.
3. Engineer lag, rolling, calendar/seasonality and promotion features.
4. Train a forecasting model.
5. Evaluate using rolling-origin cross-validation.
6. Compare the model against the seasonal-naive baseline.
7. Use the forecast for inventory risk scoring.

The supplied workbook already contains 7-day planning forecast fields (`Forecast_Demand_7D`) and inventory recommendation fields.

**Important:** the current workbook should not be interpreted as evidence of a newly trained, independently validated rolling-origin model. A full D3 implementation should report WAPE for both the seasonal-naive baseline and the final model and should only ship the more accurate approach.

## 7. Risk Scoring Logic

The project brief defines transparent decision rules:

### Stockout risk
Compare expected demand during supplier lead time with available inventory (on-hand plus on-order). If projected stock falls below the required safety level, the SKU is considered at risk.

### Overstock risk
Compare on-hand inventory with forecast demand over a forward window. If inventory is materially higher than expected demand, the SKU is flagged as overstocked.

### Decision quadrants

| Quadrant | Meaning | Recommended action |
|---|---|---|
| Reorder now | High stockout, low overstock | Replenish before stock runs out |
| Markdown / clear | High overstock, low stockout | Promote/discount to free capital |
| Watch / volatile | High on both | Investigate and review manually |
| Healthy | Low on both | No immediate action |

## 8. Dashboard

The completed workbook includes a planning dashboard with:

- Revenue KPI
- Demand KPI
- Sales KPI
- Stockout records
- SKU count
- Category performance
- Risk distribution
- Planning summary
- Revenue and demand charts
- Inventory risk visualization
- Daily demand vs sales

The dashboard is intended to make the outputs understandable to non-technical stakeholders.

## 9. Business Recommendations

1. **Prioritise Grocery replenishment** because it has the strongest demand/revenue profile and the highest number of stockout records.
2. **Review Electronics inventory** for markdown, bundling or reduced replenishment because it has the largest overstock burden.
3. **Review Home & Kitchen stock levels** and identify products suitable for clearance or slower replenishment.
4. **Use SKU-level risk flags** to prioritise operational actions rather than treating every SKU equally.
5. **Validate forecasting performance with rolling-origin WAPE** before using the forecast as an automated planning signal.

## 10. Project Structure

Recommended repository structure:

```text
foresight/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_baseline.ipynb
│   └── 03_model.ipynb
├── src/
│   ├── pipeline.py
│   ├── forecast.py
│   └── risk.py
├── app/
│   └── streamlit_app.py
├── service/
│   └── api.py
├── reports/
│   ├── EDA_Memo.md
│   └── Executive_Report.pdf
├── requirements.txt
├── README.md
└── .gitignore
```

## 11. Limitations

- The workbook is based on a synthetic training/demo dataset.
- The supplied workbook contains planning forecast fields, but it does not by itself document a complete independently trained rolling-origin model comparison.
- Forecast accuracy should therefore be reported only after the required backtest is executed.
- Risk outputs should be treated as decision-support signals and reviewed with business context.
- The project is not intended to automate purchase orders or replace operational judgement.

## 12. Deliverables

The project brief defines seven deliverables:

- **D1:** Reproducible data pipeline
- **D2:** Data-quality & EDA insight memo
- **D3:** Demand forecast model
- **D4:** Stockout/overstock risk scoring
- **D5:** Planning dashboard
- **D6:** Deployed scoring service
- **D7:** Executive readout

---

**Project FORESIGHT — Demand & Inventory Intelligence**  
Prepared for the NorthBay Living client engagement.
