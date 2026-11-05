
def electricity_bill(kwh):
    if kwh < 0:
        return None
    tier1 = min(max(kwh, 0), 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)
    total = (tier1 * 480) + (tier2 * 610) + (tier3 * 730)
    total = total + 2000
    total = total * 1.10
    return round(total)
print("Electricity Bill Table")
print("-------------------------------")
for kwh in [0, 35, 50, 120, 200, 350]:
    bill = electricity_bill(kwh)
    usd = bill / 4100
    print(f"{kwh:3} kWh -> {bill:>8,} riel (≈ {usd:.2f} USD)")
kwh = float(input("\nEnter your monthly consumption (kWh): "))
bill = electricity_bill(kwh)
if bill is None:
    print("Invalid consumption!")
else:
    print(f"Your electricity bill: {bill:,} riel")
    print(f"Your electricity bill: ${bill / 4100:.2f} USD")
