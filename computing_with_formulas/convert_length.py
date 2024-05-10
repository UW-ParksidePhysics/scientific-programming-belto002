"""
This script converts a given distance from kilometers to inches, feet, yards, and miles.

__author__ = "Jackson"
"""

if __name__ == "__main__":
    # Test case
    # Input: distance_km
    # Expected output: Distance in inches, feet, yards, and miles

    # Define the distance in kilometers
    distance_km = 0.640

    # Constants for conversion
    INCHES_PER_KILOMETER = 100000 / 2.54
    FEET_PER_INCH = 1 / 12
    YARDS_PER_FOOT = 1 / 3
    MILES_PER_YARD = 1 / 1760

    # Convert distance to inches, feet, yards, and miles
    distance_inches = distance_km * INCHES_PER_KILOMETER
    distance_feet = distance_inches * FEET_PER_INCH
    distance_yards = distance_feet * YARDS_PER_FOOT
    distance_miles = distance_yards * MILES_PER_YARD

    # Output the converted lengths
    print("Distance in inches:", distance_inches)
    print("Distance in feet:", distance_feet)
    print("Distance in yards:", distance_yards)
    print("Distance in miles:", distance_miles)
