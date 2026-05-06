from dagster import asset, Definitions
import pandas as pd
from sqlalchemy import create_engine


@asset
def raw_transactions():

    pass

@asset
def postgres_table(raw_transactions):
    engine = create_engine('postgresql://admin:admin@localhost:5433/personal_bi')
    raw_transactions.to_sql('raw_transactions', engine, if_exists='replace', index=False)
    return "Success"


defs = Definitions(
    assets=[raw_transactions, postgres_table],
)