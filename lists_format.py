from lib.io_utils import get_file_name, read_file_contents, generate_file
import sys

# Settings
OUTPUT_FILE_PATH = "output/"
OUTPUT_FILE_EXTENSION = ".txt"
LIST_N = 20

def format_output_file(input_file_path: str):
    output: list[str] = []
    file_name = get_file_name(input_file_path)
    output_file_path = OUTPUT_FILE_PATH + file_name + OUTPUT_FILE_EXTENSION

    for line in read_file_contents(input_file_path):
        # append XML list
        xml_elements = generate_xml_elements(line, LIST_N)
        output.extend(xml_elements)
        output.append("\n")

        # append Kotlin list object
        output.append("listOf(")
        list_elements = generate_list(line, LIST_N)
        output.extend(list_elements)
        output.append(")")

    generate_file(
        output_file_name=output_file_path,
        output_file_contents=output
    )
    
def generate_xml_elements(base_string, n):
    xml_elements = []
    for i in range(1, n + 1):
        xml_element = f'<item name="{base_string}{i}" type="id" />'
        xml_elements.append(xml_element)
    return xml_elements

def generate_list(base_string, n):
    list_elements = []
    for i in range(1, n + 1):
        list_elements.append(f'R.id.{base_string}{i}, ')
    
    return list_elements

if len(sys.argv) > 1:
    format_output_file(sys.argv[1])