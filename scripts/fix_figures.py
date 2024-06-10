

import os



def list_files(directory):
    return os.listdir(directory)

def find_matches(file, pattern):
    """
    Searches for a given pattern in a file and returns all matching lines.
    :param file:
    :param pattern:
    :return:
    """

    matches = []

    with open(file, 'r') as f:
        for line in f:
            if pattern in line:
                matches.append(line)

    return matches


def update_file(file, mapping):
    """
    Reads the content of a given file, replaces specified substrings according
    to a mapping, and writes the updated content back to the file.

    This function opens a file in read mode to capture its current content. It then
    iterates over a dictionary (`mapping`), using each key-value pair to replace
    occurrences of the key in the content with its corresponding value. After all
    replacements are made, the function opens the file again in write mode and
    updates its content with the modified text.

    Parameters:
    - file (str): The path to the file whose content is to be updated.
    - mapping (dict): A dictionary where each key is a substring to be replaced
      in the file's content and each value is the new string that will replace
      the key in the content.

    Returns:
    None. The function directly modifies the file specified by the `file` parameter.

    Example usage:
    >>> update_file('example.txt', {'old_string': 'new_string', 'foo': 'bar'})
    This will replace all occurrences of 'old_string' with 'new_string' and 'foo' with 'bar' in 'example.txt'.
    """
    with open(file, 'r') as f:
        content = f.read()
    for old, new in mapping.items():
        content = content.replace(old, new)
    with open(file, 'w') as f:
        f.write(content)



def main():
    directory = "source"
    pattern = r'^\.\. figure:: _static/pdf_images/page_\d+_image_\d+\.png$'
    for file in list_files(directory):
        matches = find_matches(file, pattern)
        if matches:
            print(f"Found matches in {file}:")
            for match in matches:
                print(match)
                update_file()


















