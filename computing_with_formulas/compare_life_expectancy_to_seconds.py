"""This script calculates whether a newborn is expected to live for more than one billion seconds and compares it
with the CDC life expectancy.

__author__ = "Jackson"
"""

if __name__ == "__main__":
    # Test case Input: BILLION_SECONDS, CDC_LIFE_EXPECTANCY Expected output: Whether a newborn is expected to live
    # for more than one billion seconds and the CDC life expectancy

    # Constants
    SECONDS_IN_YEAR = 60 * 60 * 24 * 365
    BILLION_SECONDS = 10 ** 9
    CDC_LIFE_EXPECTANCY = 78.7

    # Calculate years in one billion seconds
    one_billion_seconds_years = BILLION_SECONDS / SECONDS_IN_YEAR

    # Output results
    print("one billion seconds is ", one_billion_seconds_years, " years")
    print("CDC life expectancy: ", CDC_LIFE_EXPECTANCY, " years")

    # Comparison
    if one_billion_seconds_years > CDC_LIFE_EXPECTANCY:
        print("Yes, a newborn is expected to live for more than one billion seconds.")
    else:
        print("No, a newborn is not expected to live for more than one billion seconds.")

        # Yes, a newborn baby is expected to live more than one billion seconds.
