"""
This module reads star data from a file and sorts it based on different criteria.

__author__ = "Jackson"
"""

# Read the data from the file
with open('stars.txt', 'r') as file:
    star_data = eval(file.read())


# Define sorting functions
def sort_by_distance(star_info):
    """Sort stars by distance."""
    return star_info[1]


def sort_by_brightness(star_info):
    """Sort stars by apparent brightness."""
    return star_info[2]


def sort_by_luminosity(star_info):
    """Sort stars by luminosity."""
    return star_info[3]


# Sort the list based on distance, apparent brightness, and luminosity
sorted_by_distance = sorted(star_data, key=sort_by_distance)
sorted_by_brightness = sorted(star_data, key=sort_by_brightness)
sorted_by_luminosity = sorted(star_data, key=sort_by_luminosity)

# Write out the sorted tables
print("Star Name vs. Distance:")
for star in sorted_by_distance:
    print(f"{star[0]}: {star[1]} ly")

print("\nStar Name vs. Apparent Brightness:")
for star in sorted_by_brightness:
    print(f"{star[0]}: {star[2]}")

print("\nStar Name vs. Luminosity:")
for star in sorted_by_luminosity:
    print(f"{star[0]}: {star[3]}")

# Test output
if __name__ == '__main__':
    test_values = [
        ('Alpha Centauri A', 4.3, 0.26, 1.56),
        ('Alpha Centauri B', 4.3, 0.077, 0.45),
        ('Alpha Centauri C', 4.2, 0.00001, 0.00006),
        ("Barnard's Star", 6.0, 0.00004, 0.0005),
        ('Wolf 359', 7.7, 0.000001, 0.00002),
        ('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
        ('Luyten 726-8 A', 8.4, 0.000003, 0.00006),
        ('Luyten 726-8 B', 8.4, 0.000002, 0.00004),
        ('Sirius A', 8.6, 1.00, 23.6),
        ('Sirius B', 8.6, 0.001, 0.003),
        ('Ross 154', 9.4, 0.00002, 0.0005),
    ]

    print("\nTest Output:")
    for star_data in test_values:
        print(f"Star: {star_data[0]}, Distance: {star_data[1]} ly, Apparent Brightness: "
              f"{star_data[2]}, Luminosity: {star_data[3]}")
