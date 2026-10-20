# Data_science_ML

## ETL PostgreSQL output

Install dependencies and run the ETL from the project root:

```sh
uv sync
uv run python etl_pipeline/main.py
```

Grouped report results are written to separate tables named after each metric, with entity and measure columns (for example, `top_10_customers_by_purchase_volume` contains `CustomerID` and `Quantity`). Scalar metrics share the `scalar_insights` table with `insight_name` and `value` columns. These tables are replaced on each run so they represent the latest report snapshot.
