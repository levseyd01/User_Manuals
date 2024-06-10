import os

import os

def adjust_heading_underlines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    corrected_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Check if the next line is not empty and consists of the underline characters
        if (i + 1 < len(lines) and
            len(lines[i + 1].strip()) > 0 and  # Check that the line is not empty after stripping
            set(lines[i + 1].strip()) <= set("=-~`:'#*^\"!+%<>_")):
            underline = lines[i + 1].strip()
            # Ensure the first character of the non-empty underline is replicated according to the stripped heading's length
            expected_underline = underline[0] * len(line.strip())
            corrected_lines.append(line)
            corrected_lines.append(expected_underline + '\n')
            i += 2  # Skip the next line as it's the underline
        else:
            corrected_lines.append(line)
            i += 1

    # Write the corrected lines to the same file or a new file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(corrected_lines)

def refactor_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.rst'):
            file_path = os.path.join(directory_path, filename)
            adjust_heading_underlines(file_path)
            print(f"Refactored {filename}")

# Update the directory path as needed
directory_path = (r'C:\Users\levse\Desktop2\CodingW\manual\TA_IssuerManual\TA_IssuerManual\source'
                  r'')
refactor_directory(directory_path)
