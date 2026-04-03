#!/usr/bin/env python3

import argparse
import os
import re
import sys
from collections import defaultdict


def extract_test_names(filename):
    test_functions = []
    class_context = None

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            class_match = re.match(r'^\s*class\s+(\w+)', line)
            if class_match:
                class_context = class_match.group(1)
                continue

            func_match = re.match(r'^\s*def\s+(test\w+)\s*\(', line)
            if func_match:
                test_name = func_match.group(1)

                if class_context and ('self' in line or 'cls' in line):
                    full_name = f'{class_context}.{test_name}'
                else:
                    full_name = test_name

                test_functions.append((full_name, i + 1))  # +1 for row number

    except Exception as e:
        print(f'Error while processing file {filename}: {str(e)}')
        return []

    return test_functions


def check_files(filenames):
    all_test_names = defaultdict(list)

    for filename in filenames:
        if not filename.endswith('.py') or not os.path.dirname(filename).startswith('tests'):
            continue

        test_names = extract_test_names(filename)

        for test_name, line in test_names:
            rel_path = os.path.relpath(filename)
            all_test_names[test_name].append((rel_path, line))

    has_duplicates = False

    for test_name, occurrences in all_test_names.items():
        if len(occurrences) > 1:
            has_duplicates = True
            print(f"Error. Test name duplication '{test_name}' found in:")

            for file_path, line in occurrences:
                print(f'  - {file_path}:{line}')

            print('')

    return not has_duplicates


def main():
    parser = argparse.ArgumentParser(description='Check unique pytest function names')
    parser.add_argument('filenames', nargs='*', help='Files for verification')
    args = parser.parse_args()

    if not check_files(args.filenames):
        print('Found test names duplications! Please fix before the commit.')
        return 1

    return 0


if __name__ == '__main__':
    if sys.platform.startswith('win'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    sys.exit(main())
