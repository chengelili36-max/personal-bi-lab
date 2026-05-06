# orchestration/definitions.py

from dagster import asset, Definitions
import pandas as pd
import random

@asset
def raw_transactions():
    """will generate synthetic transaction data using Faker in the future, but for now let's return a simple DataFrame"""
    return pd.DataFrame({"amount": [random.randint(-100, -10) for _ in range(10)]})

@asset
def gym_records():
    """生成健身记录资产"""
    return pd.DataFrame({"workout": ["Cardio", "Strength"], "calories": [300, 500]})

@asset(deps=[raw_transactions, gym_records])
def daily_summary():
    """relays on both transactions and gym records to compute a 'life balance index' or something fun like that"""
   
    print("generating daily summary...")
    return "Balanced"

defs = Definitions(
    assets=[raw_transactions, gym_records, daily_summary]
)