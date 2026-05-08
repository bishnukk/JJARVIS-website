import requests
import json

SUPABASE_URL = 'https://hlfianhpyryrnnmxwlcy.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsZmlhbmhweXJ5cm5ubXh3bGN5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzYzMTc5MjIsImV4cCI6MjA5MTg5MzkyMn0.SeCgt7JYkYpKmjWSAYBlkLOuE5cL7HkvvjD02WGk4Ik'

headers = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

print("Checking Signals (Latest 20)...")
url = f"{SUPABASE_URL}/rest/v1/signals?select=*&order=created_at.desc&limit=20"
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    for item in data:
        print(f"ID: {item.get('id')}, Created: {item.get('created_at')}, Symbol: {item.get('symbol')}, Action: {item.get('action')}")
else:
    print(f"Error: {response.status_code} - {response.text}")
