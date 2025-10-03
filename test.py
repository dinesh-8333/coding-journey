# Day 0 - Setup Verification

print("="*50)
print("Day 0 Setup Test")
print("="*50)

# Python version
import sys
print(f"\nPython: {sys.version.split()[0]}")

# Math test
print(f"\nMath: 2 + 2 = {2 + 2}")

# Finance calculation
income = 100000
tax = income * 0.30
print(f"\nTax Example:")
print(f"  Income: Rs.{income:,}")
print(f"  Tax (30%): Rs.{tax:,}")

# Compound interest
def compound_interest(p, r, t):
    return p * (1 + r) ** t

result = compound_interest(10000, 0.10, 5)
print(f"\nCompound Interest:")
print(f"  Rs.10,000 at 10% for 5 years = Rs.{result:,.2f}")

print("\n" + "="*50)
print("Setup Complete!")
print("="*50)