import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine

engine = create_engine('postgresql://admin:admin@localhost:5433/personal_bi')

fake = Faker()


def generate_dirty_merchant(merchant):
    prefixes = ["SQ* ", "TST* ", "PAYPAL *", "AMZN MKTP US* ", ""]
    suffixes = [" CA", " SAN FRANCISCO", " NY", " #12345", ""]
    return f"{random.choice(prefixes)}{merchant}{random.choice(suffixes)}"


merchants_config = {
    "Amazon": (10, 200),
    "Whole Foods": (50, 150),
    "DoorDash": (20, 60),
    "Uber": (15, 50),
    "Netflix": (15, 15),
    "Starbucks": (4, 12),
    "Airbnb": (300, 1200),
    "LOEWE": (400, 1500),
    "Alo Yoga": (50, 120)
}

transactions = []


print("⏳ generating synthetic transaction data...")
for _ in range(500):
    merchant_clean = random.choice(list(merchants_config.keys()))
    min_amt, max_amt = merchants_config[merchant_clean]
    
    amount = round(random.uniform(min_amt, max_amt), 2)
    merchant_raw = generate_dirty_merchant(merchant_clean)
    date = fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
    
    transactions.append({
        "transaction_id": fake.uuid4(),
        "date": date,
        "merchant_raw": merchant_raw,
        "amount": -amount
    })

for i in range(12):
    pay_date = (datetime.now() - timedelta(days=30*i)).strftime('%Y-%m-01 08:00:00')
    transactions.append({
        "transaction_id": fake.uuid4(),
        "date": pay_date,
        "merchant_raw": "ACH ELECTRONIC CREDIT DIRECT DEP TECH CORP",
        "amount": 10000.00
    })


df = pd.DataFrame(transactions)
df = df.sort_values(by="date", ascending=False).reset_index(drop=True)


print("⏳ querying...")

df.to_sql('raw_transactions', engine, if_exists='replace', index=False)

print(f"✅ perfect! {len(df)} records have been written to the raw_transactions table in the personal_bi database!")
df.to_csv('raw_transactions_for_tableau.csv', index=False)
print("✅  raw_transactions_for_tableau.csv generated for Tableau Public visualization!")