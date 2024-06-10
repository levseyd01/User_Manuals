import os
import re

def update_figure_description(file_path):
    # Regular expression to find "Figure" lines and capture the text following the figure number
    figure_text_regex = r'\n\s*Figure \d+\.\s*(.*?)\n'

    # Function to replace the matched text with the captured description, indented as requested
    def replacement(match):
        return "\n\n   " + match.group(1) + "\n"  # Adding three spaces before the description

    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Use the regular expression to find and replace the figure descriptions
    updated_content = re.sub(figure_text_regex, replacement, file_content)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# Example usage - iterate through files in a directory
directory_path = 'company_information'
for filename in os.listdir(directory_path):
    if filename.endswith('.rst'):  # Adjust the extension as per your files
        update_figure_description(os.path.join(directory_path, filename))

print("Figure descriptions have been updated with proper indentation.")
