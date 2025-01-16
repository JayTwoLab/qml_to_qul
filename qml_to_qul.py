import os
import re

# List of unsupported QML elements 
unsupported_elements = ['ListView', 'Loader', 'GridLayout', 'Flow']

def detect_unsupported_elements(file_path):
    """
    Detects unsupported elements in QML files. 
    """
    with open(file_path, 'r') as file:
        content = file.read()
        found_elements = []
        for element in unsupported_elements:
            if element in content:
                found_elements.append(element)
        return found_elements

def replace_elements(content):
    """
    Replaces elements that are not supported in QML code.
    """
    # GridLayout -> Replace with Column
    content = re.sub(r'\bGridLayout\b', 'Column', content)
    # Replace with ListView -> Column
    content = re.sub(r'\bListView\b', 'Column', content)
    # Replace with Flow -> Row
    content = re.sub(r'\bFlow\b', 'Row', content)
    # Loader -> Annotation Processing
    content = re.sub(r'\bLoader\b', '// Loader is not supported in Qul', content)
    return content

def convert_qml_files(input_dir, output_dir):
    """
    Convert the QML file in the specified directory and store the converted file in the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.qml'):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)

            with open(input_path, 'r') as infile:
                content = infile.read()
                # Unsupported element detection
                unsupported = detect_unsupported_elements(input_path)
                if unsupported:
                    print(f"Unsupported elements in {file_name}: {unsupported}")

                # Applying Conversion Rules
                new_content = replace_elements(content)

            with open(output_path, 'w') as outfile:
                outfile.write(new_content)
                print(f"Converted {file_name} and saved to {output_path}")

def main(input_directory, output_directory):
    """
    QML Transducer Main Function
    """
    if not os.path.exists(input_directory):
        print(f"Error: Input directory '{input_directory}' does not exist.")
        return

    print("Starting QML file conversion...")
    convert_qml_files(input_directory, output_directory)
    print("Conversion completed.")

if __name__ == "__main__":
    # Example Run: Passing a directory path to the main function
    example_input_dir = "path/to/your/qml/files"
    example_output_dir = "path/to/converted/qml/files"
    main(example_input_dir, example_output_dir)
