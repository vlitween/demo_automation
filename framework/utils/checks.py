from datetime import datetime
from re import match


def verify_strings(actual_string, expected_string):
    assert actual_string == expected_string, f'Actual string "{actual_string}" != expected string "{expected_string}"'


def check_text_present(item: str):
    assert bool(item and item.strip()), f'Invalid string "{item}"'


def validate_date_text(date_string: str):
    # Expected format of date_string is like "Tuesday, March 10, 2026"
    date_format = '%A, %B %d, %Y'
    try:
        datetime.strptime(date_string, date_format)
        return
    except ValueError:
        raise AssertionError(f'Invalid date format of string "{date_string}"')


def validate_string_by_pattern(item: str, pattern: str):
    assert match(pattern, item.strip()), f'String "{item}" does not match pattern "{pattern}"'
