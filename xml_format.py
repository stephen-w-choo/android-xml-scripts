from lib.io_utils import get_file_name, read_file_contents, generate_file
import sys

# Settings
OUTPUT_FILE_PATH = "output/"
OUTPUT_FILE_EXTENSION = ".xml"

def format_output_file(input_file_path: str):
    output: list[str] = []
    file_name = get_file_name(input_file_path)
    output_file_path = OUTPUT_FILE_PATH + file_name + OUTPUT_FILE_EXTENSION
    
    # Read and get formatted strings
    xml_elements = format_xml(read_file_contents(input_file_path))
    output.extend(xml_elements)

    generate_file(
        output_file_name=output_file_path,
        output_file_contents=output
    )

def format_xml(input):
    output = []

    for base_string in input:
        formatted_id = f'<item name="{base_string}" type="id" />'     
        output.append(formatted_id)

    return output       

if len(sys.argv) > 1:
    format_output_file(sys.argv[1])