import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import JSONB


load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def insights_to_tables(insights):
	tables = {}
	json_columns = {}
	scalar_rows = []

	for insight_name, result in insights.items():
		if isinstance(result, pd.DataFrame):
			tables[insight_name] = result.copy()
		elif isinstance(result, pd.Series):
			table = result.rename_axis(str(result.index.name or "item_key")).reset_index()
			table = table.rename(columns={result.name or 0: result.name or "value"})
			tables[insight_name] = table
		elif isinstance(result, dict):
			tables[insight_name] = pd.DataFrame({"value": [result]})
			json_columns[insight_name] = ["value"]
		elif isinstance(result, (list, tuple)):
			tables[insight_name] = pd.DataFrame({"value": list(result)})
		else:
			if hasattr(result, "item"):
				result = result.item()
			if pd.isna(result):
				result = None
			scalar_rows.append({"insight_name": insight_name, "value": result})

	scalar_dataframe = pd.DataFrame(scalar_rows)
	if not scalar_dataframe.empty:
		scalar_dataframe["value"] = pd.Series(
			[None if pd.isna(value) else value for value in scalar_dataframe["value"]],
			dtype=object,
		)

	return scalar_dataframe, tables, json_columns


def save_insights(insights):
	database_url = os.getenv("DATABASE_URL")
	if not database_url:
		raise RuntimeError(
			"DATABASE_URL is not set. Add the PostgreSQL connection URL to the project .env file."
		)
	if not database_url.startswith("postgresql://"):
		raise ValueError("DATABASE_URL must use the postgresql:// scheme.")

	scalar_dataframe, tables, json_columns = insights_to_tables(insights)
	engine = create_engine(database_url, pool_pre_ping=True)
	try:
		with engine.begin() as connection:
			for table_name, dataframe in tables.items():
				dataframe.to_sql(
					table_name,
					con=connection,
					if_exists="replace",
					index=False,
					dtype={column: JSONB() for column in json_columns.get(table_name, [])},
				)

			if not scalar_dataframe.empty:
				scalar_dataframe.to_sql(
					"sales_insights",
					con=connection,
					if_exists="replace",
					index=False,
					dtype={"value": JSONB()},
				)
	finally:
		engine.dispose()

	return sum(len(dataframe) for dataframe in tables.values()) + len(scalar_dataframe)
