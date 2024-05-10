"""
This script prints code snippets along with their explanations.

__author__ = "Jackson"
"""


def print_code_snippets(snippets):
    """
    Print code snippets along with their explanations.

    Parameters:
        snippets (dict): A dictionary where keys are snippet names and values are explanations.

    Returns:
        None
    """
    for snippet, explanation in snippets.items():
        print(f"Code snippet:\n{explanation}\n{snippet}\n\n")


if __name__ == '__main__':
    # Test case
    # Input: code_snippets dictionary containing working, non-working, and fixed code snippets
    # Expected output: Each code snippet printed with its corresponding explanation
    code_snippets = {
        "working_snippet": """
numbers = {}
numbers[0] = -5
numbers[1] = 10.5
""",
        "working_explanation": "This code creates a dictionary called 'numbers' and assigns"
                               "\nvalues to keys 0 and 1.",
        "non_working_snippet": """
other_numbers = []
other_numbers[0] = -5
other_numbers[1] = 10.5
""",
        "non_working_explanation": "This code attempts to assign values to "
                                   "indices in an empty list, causing an IndexError.",
        "fixed_snippet": """
other_numbers = []
other_numbers.append(-5)
other_numbers.append(10.5)
""",
        "fixed_explanation": "Use the append function to add elements to the list instead of "
                             "assigning directly to indices."
    }
    print_code_snippets(code_snippets)
