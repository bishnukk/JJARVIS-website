
import requests
import json

SUPABASE_URL = "https://hlfianhpyryrnnmxwlcy.supabase.co"
SUPABASE_KEY = "your_supabase_key" # I should find this in index.html

def check_supabase():
    # Fetch orders
    url = f"{SUPABASE_URL}/rest/v1/orders?select=*&order=order_date.desc&limit=10"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        orders = response.json()
        print(f"Latest 10 orders:")
        for o in orders:
            print(f"ID: {o.get('id')}, Date: {o.get('order_date')}, Pair: {o.get('jr_pair')}, Status: {o.get('status')}")
    else:
        print(f"Failed to fetch orders: {response.status_code} {response.text}")

    # Fetch signals
    url = f"{SUPABASE_URL}/rest/v1/signals?select=*&order=created_at.desc&limit=10"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        signals = response.json()
        print(f"\nLatest 10 signals:")
        for s in signals:
            print(f"ID: {s.get('id')}, Created At: {s.get('created_at')}, Symbol: {s.get('symbol')}, Action: {s.get('action')}")
    else:
        print(f"Failed to fetch signals: {response.status_code} {response.text}")

if __name__ == "__main__":
    # Get key from index.html first
    with open(r"c:\Users\ASUS\Desktop\JJARVIS-website\index.html", "r", encoding="utf-8") as f:
        content = f.read()
        import re
        match = re.search(r"const SUPABASE_KEY = '(.*?)';", content)
        if match:
            SUPABASE_KEY = match.group(1)
            check_supabase()
        else:
            # Try double quotes just in case
            match = re.search(r'const SUPABASE_KEY = "(.*?)";', content)
            if match:
                SUPABASE_KEY = match.group(1)
                check_supabase()
            else:
                print("Could not find SUPABASE_KEY in index.html")
