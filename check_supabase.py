import requests
import json

SUPABASE_URL = 'https://hlfianhpyryrnnmxwlcy.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsZmlhbmhweXJ5cm5ubXh3bGN5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYzMTc5MjIsImV4cCI6MjA5MTg5MzkyMn0.SeCgt7JYkYpKmjWSAYBlkLOuE5cL7HkvvjD02WGk4Ik'

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

def check_table(table, order_col):
    print(f"--- Checking {table} ---")
    url = f"{SUPABASE_URL}/rest/v1/{table}?select=*&order={order_col}.desc&limit=5"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            print(json.dumps(item, indent=2))
    else:
        print(f"Error: {response.status_code} - {response.text}")

print("Checking Signals...")
check_table("signals", "created_at")

print("\nChecking Orders...")
check_table("orders", "order_date")
