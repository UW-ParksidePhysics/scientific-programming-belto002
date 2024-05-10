"""
This module provides functions to parse animation code from a file, format section headers,
and write HTML reports.

__author__ = "Jackson"
"""


def parse_animation_code(code_filename):
    """
    Parse animation code from a file.

    Parameters:
        code_filename (str): The filename of the file containing the animation code.

    Returns:
        str: The animation code read from the file.

    Example:
        If 'animation_code.py' contains the animation code:
        def animate():
            # Animation code here
            pass

        parse_animation_code('animation_code.py') will return:
        "def animate():
            # Animation code here
            pass"
    """
    with open(code_filename, 'r') as file:
        code = file.read()
    return code


def format_section_header(header_string):
    """
    Format a section header string into HTML format.

    Parameters:
        header_string (str): The header string to be formatted.

    Returns:
        str: The HTML-formatted section header.

    Example:
        format_section_header('Animation Code') will return:
        "<h1>Animation Code</h1>"
    """
    return f"<h1>{header_string}</h1>"


def write_html_report(report_str, report_filename):
    """
    Write an HTML report string to a file.

    Parameters:
        report_str (str): The HTML report string to be written to the file.
        report_filename (str): The filename of the HTML report file to be created.

    Returns:
        None.

    Example:
        write_html_report('<h1>Test Report</h1>', 'test_report.html') will create a file
        'test_report.html' containing the HTML string "<h1>Test Report</h1>".
    """
    with open(report_filename, 'w') as file:
        file.write(report_str)


if __name__ == '__main__':
    # Test case
    # Input: 'animation_code.py' containing animation code
    # Output: HTML report file 'test_animation_report.html' containing formatted animation code
    test_code_filename = 'animation_code.py'

    # Call functions
    animation_code = parse_animation_code(test_code_filename)
    animation_code_header = format_section_header('Animation Code')

    # Define HTML tags
    header_one_tag = "<h1>"
    preformatted_tag = "<pre>"
    close_tag = "</pre>"

    # Construct HTML report
    report_string = header_one_tag + "Animation Report" + close_tag
    report_string += animation_code_header + preformatted_tag + animation_code + close_tag

    # Write HTML report
    test_report_filename = 'test_animation_report.html'
    write_html_report(report_string, test_report_filename)

    print(f"Test HTML report created: {test_report_filename}")
