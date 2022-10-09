# Exercises 6.9, 6.11, 6.12, 6.18

# 6.9 Covert from feet to meters

def feetToMeters(feet):
    meters = 0.305 * feet
    return meters

def metersToFeet(meters):
    feet = meters / 0.305
    return feet

print(f"{'Feet' :<8}{'Meters' :<7} | {'Meters' :<8}{'Feet' :<7}")
print()
for i in range(1, 11):
    print(f"{format(i, '0.1f') :<8}{format(feetToMeters(i), '0.3f') :<7} | {format(15+i * 5, '0.1f') :<8}{format(metersToFeet(15+i * 5), '0.3f') :<7}")







