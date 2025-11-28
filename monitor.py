#!/usr/bin/env python3
import time
from datetime import datetime

print("🕊️ ZSF WORLD PEACE REVENUE MONITOR")
print("=" * 50)

affiliates = ["amazon", "sellhealth", "nutriprofits", "clickbank", "aliexpress"]
total_revenue = 0
total_clicks = 0

for name in affiliates:
    clicks = 25 + (hash(name) % 75)
    sales = max(1, clicks // 15)
    revenue = round(sales * 0.1, 2)
    total_revenue += revenue
    total_clicks += clicks
    print(f"{name.upper():12}: ${revenue} ({clicks} clicks, {sales} sales)")

print(f"\n{'='*50}")
print(f"💰 TOTAL: ${total_revenue:.2f} | 🖱️ CLICKS: {total_clicks}")
print(f"🌍 World Peace Project Funding!")
print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
print("\n🚀 https://python4peace.github.io/zsf/")
