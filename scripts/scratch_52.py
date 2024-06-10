import os
import re

def update_figure_path(file_path):
    # Regular expression to match the figure path
    figure_regex = r'(\.\. figure:: _static/pdf_images/)'
    new_path = r'../_static/pdf_images/'

    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Replace the path using regular expression
    updated_content = re.sub(figure_regex, f'.. figure:: {new_path}', file_content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# Example usage - iterate through files in a directory
directory_path = 'shareholders'
for filename in os.listdir(directory_path):
    if filename.endswith('.rst'):  # or '.rst' if your files have a specific extension
        update_figure_path(os.path.join(directory_path, filename))

print("Figure paths have been updated.")