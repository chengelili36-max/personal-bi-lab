import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

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
df.to_csv("alex_transactions.csv", index=False)

print("✅ successfully generated synthetic transaction data for Alex's bank statement.")
print(f"✅ generated {len(df)} files save as alex_transactions.csv")

gym_sessions = []
for _ in range(150): 
    gym_date = fake.date_time_between(start_date='-1y', end_date='now')
    gym_sessions.append({
        "session_id": fake.uuid4(),
        "date": gym_date.strftime('%Y-%m-%d %H:%M:%S'),
        "workout_type": random.choice(["Strength", "Cardio", "Yoga"]),
        "calories_burned": random.randint(300, 800)
    })

df_gym = pd.DataFrame(gym_sessions)
df_gym.to_sql('raw_gym_activity', engine, if_exists='replace', index=False)