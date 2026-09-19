# Project FORESIGHT — Data Quality & EDA Insight Memo

## Executive Summary

The FORESIGHT dataset contains 3,000 records covering 2024-01-01 through 2025-12-31, with 100 unique SKUs across 5 categories and 4 regions.

The dataset contains **107,885 demand units**, **106,385 sales units**, and approximately **₹26.97 crore in revenue**.

The most important operational finding is that inventory pressure is asymmetric:

- Stockout records are relatively limited at **31**, but Grocery accounts for the largest share with **19**.
- Overstock records total **507**, with Electronics contributing the largest number (**281**) and Home & Kitchen contributing **150**.

This suggests that inventory planning should balance two goals: protect availability for high-demand products while reducing excess inventory in slower-moving categories.

## 1. Data Profile

| Field | Result |
|---|---:|
| Analysis period | 2024-01-01 to 2025-12-31 |
| Rows | 3,000 |
| Unique SKUs | 100 |
| Categories | 5 |
| Regions | 4 |
| Demand units | 107,885 |
| Sales units | 106,385 |
| Revenue | ₹269,682,326.67 |
| Stockout records | 31 |
| Overstock records | 507 |
| Promotion rate | 20.4% |

The source workbook is identified as a synthetic training/demo dataset.

## 2. Data Quality Assessment

### Completeness

The `Raw_Data` sheet contains no missing values in the supplied workbook.

### Duplicates

No duplicate rows were found in the supplied `Raw_Data` sheet.

### Coverage

The dataset covers two calendar years, providing enough historical coverage to investigate changes over time and to support time-based forecasting experiments.

### Data-grain consideration

The workbook contains SKU-level and SKU/category-level summaries. Some SKU IDs appear across more than one category, so analysis involving category should use the appropriate SKU + category grain rather than assuming SKU IDs are globally unique to a category.

## 3. Demand and Sales Overview

Total demand is **107,885 units**, while recorded sales are **106,385 units**. The difference is **1,500 units**, indicating that demand exceeded realised sales in the dataset.

This gap is consistent with the project's inventory-planning objective: demand and sales should not always be treated as identical when stock availability can constrain realised sales.

## 4. Category Analysis

| Category | Revenue | Demand Units | Stockout Records | Overstock Records |
|---|---:|---:|---:|---:|
| Grocery | ₹8.61 Cr | 33,396 | 19 | 0 |
| Personal Care | ₹6.25 Cr | 25,619 | 9 | 12 |
| Apparel | ₹4.89 Cr | 20,100 | 2 | 64 |
| Home & Kitchen | ₹4.42 Cr | 17,806 | 1 | 150 |
| Electronics | ₹2.80 Cr | 10,964 | 0 | 281 |

### Finding 1 — Grocery is the strongest demand category

Grocery leads the dataset in revenue and demand. It also records the highest number of stockout events.

**Business implication:** replenishment attention should be concentrated on high-demand Grocery SKUs so that strong demand is not lost because of insufficient inventory.

### Finding 2 — Electronics has the largest overstock burden

Electronics records **281 overstock events**, the highest among all categories, while generating the lowest category revenue in the dataset.

**Business implication:** planners should investigate slow-moving Electronics SKUs for markdowns, bundles, promotions or reduced future replenishment.

### Finding 3 — Home & Kitchen also needs inventory rationalisation

Home & Kitchen records **150 overstock events**.

**Business implication:** this category should be reviewed for excess stock and opportunities to reduce future replenishment or clear existing inventory.

### Finding 4 — Stockout and overstock problems require different actions

The categories do not show the same type of inventory problem. Grocery is primarily associated with stockout pressure, whereas Electronics and Home & Kitchen show much stronger overstock pressure.

**Business implication:** a single inventory policy is unlikely to be optimal. The dashboard should prioritise different actions by SKU and risk type.

## 5. Promotion and Planning Signals

The supplied data contains a promotion indicator and forecast/inventory-planning fields. Promotions should be considered during forecasting because promotional activity can change short-term demand.

The project brief specifically recommends using calendar/seasonality and promotion signals as forecasting features.

## 6. Forecasting Implications

The EDA supports a time-series forecasting approach rather than a random train/test split.

The project brief requires:

- a seasonal-naive baseline,
- lag and rolling features,
- calendar/seasonality and promotion features,
- rolling-origin cross-validation,
- WAPE comparison against the baseline,
- no future-data leakage.

The current workbook provides `Forecast_Demand_7D`, but the workbook alone does not document an independently trained model and rolling-origin backtest. Therefore, the forecast should be described as a supplied planning output unless the full modelling workflow is subsequently executed.

## 7. Inventory Risk Interpretation

The project brief recommends combining demand forecasts with inventory position.

### Stockout

Forecast demand during lead time should be compared with on-hand and on-order inventory. A SKU is at risk when projected inventory falls below the required safety level.

### Overstock

On-hand inventory should be compared with forecast demand over a forward window. Excess inventory indicates potential capital being tied up in stock that may sell slowly.

### Actions

- **Reorder now:** high stockout risk and low overstock risk.
- **Markdown / clear:** high overstock risk and low stockout risk.
- **Watch / volatile:** high levels of both risks.
- **Healthy:** low levels of both risks.

## 8. Recommended Operational Actions

### Immediate priorities

1. Review high-risk Grocery SKUs and verify replenishment timing.
2. Investigate Electronics SKUs with repeated overstock signals.
3. Review Home & Kitchen excess stock for clearance opportunities.
4. Use SKU-level risk ranking to focus planner attention on the highest-impact items.
5. Monitor demand-versus-sales gaps as an early signal of inventory constraints.

### Forecasting priority

Before production use, run the required rolling-origin backtest and report:

- seasonal-naive WAPE,
- final-model WAPE,
- improvement versus baseline,
- forecast bias,
- performance by relevant SKU/category groups.

## 9. Limitations

1. The dataset is synthetic and should not be treated as a direct representation of real NorthBay Living operations.
2. The workbook contains forecast and risk-planning fields, but does not independently demonstrate a full rolling-origin model evaluation.
3. Rupee impact should be interpreted as planning support unless the exact business valuation methodology is validated with the client.
4. Risk flags should be reviewed alongside supplier and operational context.

## 10. Conclusion

The EDA shows a clear inventory trade-off: **high-demand categories need availability protection, while slower-moving categories require inventory reduction.**

The most actionable priorities are:

- **Protect Grocery availability.**
- **Reduce Electronics overstock.**
- **Rationalise Home & Kitchen inventory.**
- **Use SKU-level forecasting and transparent risk scoring to prioritise actions.**
- **Validate the forecasting model against a seasonal-naive baseline using rolling-origin WAPE before deployment.**

These findings directly support the FORESIGHT objective of turning historical demand and inventory data into practical stocking decisions.
