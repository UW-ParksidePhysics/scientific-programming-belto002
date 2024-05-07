# Define the distance in kilometers
distance_km = 0.640

# Convert distance to inches, feet, yards, and miles
distance_inches = distance_km * 100000 / 2.54
distance_feet = distance_inches / 12
distance_yards = distance_feet / 3
distance_miles = distance_yards / 1760

# Output the converted lengths
print("Distance in inches:", distance_inches)
print("Distance in feet:", distance_feet)
print("Distance in yards:", distance_yards)
print("Distance in miles:", distance_miles)
