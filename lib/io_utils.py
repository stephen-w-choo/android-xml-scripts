import os

def get_file_name(input_file_name: str) -> str:
    """
    Returns the basename of a file 
    eg 'input/text.txt' => 'text'
    """
    basename = os.path.basename(input_file_name)
    root = os.path.splitext(basename)[0]
    return root

def read_file_contents(input_file_name: str) -> list[str]:
    """
    Reads a file as a list
    """
    res = []

    with open(input_file_name, "r") as input_file_contents:
        for line in input_file_contents:
            res.append(line.strip())

    return res

def generate_file(output_file_name: str, output_file_contents: list[str]):
    """
    Takes an output file directory name and list of strings and writes to it
    """
    with open(output_file_name, "w") as output_file:
        for line in output_file_contents:
            output_file.write(line + "\n")