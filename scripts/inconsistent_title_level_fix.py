# Step 1: Drafting the initial version of the script

import os
import re


def adjust_underlines_in_file(file_path):
    """
    Adjust the underline lengths in a file to match the lengths of their corresponding titles.

    Args:
    file_path (str): The path to the file to be processed.
    """
    # Pattern to identify titles and their underlines: Assumes titles are followed by lines of '~'
    title_underline_pattern = re.compile(r'(.*\n)(~+)')

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # List to hold the adjusted lines
    adjusted_lines = []
    last_index = 0

    for match in title_underline_pattern.finditer(content):
        title, underline = match.groups()
        # Adjust the underline to match the title's length, excluding the newline character
        adjusted_underline = '~' * (len(title) - 1)
        adjusted_lines.append(content[last_index:match.start()])
        adjusted_lines.append(title + adjusted_underline + '\n')
        last_index = match.end()

    # Add the remainder of the file content
    adjusted_lines.append(content[last_index:])

    # Write the adjusted content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(''.join(adjusted_lines))


def adjust_underlines_in_folder(folder_path):
    """
    Adjust the underline lengths for titles in all files within a specified folder.

    Args:
    folder_path (str): The path to the folder containing the files to be processed.
    """
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # Process only files, ignoring directories
        if os.path.isfile(file_path):
            adjust_underlines_in_file(file_path)
            print(f"Processed: {file_path}")

# Note: Function calls are commented out for development. They will be uncommented once the user is ready to use the script.
# adjust_underlines_in_folder("path/to/your/folder")
