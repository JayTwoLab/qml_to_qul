# `qml_to_qul` : QML to Qul Converter

This Python program processes QML files and converts them to a format compatible with Qt Quick Ultralite (Qul). It identifies unsupported QML elements, replaces them with supported alternatives, and saves the updated files to a specified output directory.

## Features
1. **Unsupported Element Detection**: 
   - The `detect_unsupported_elements` function scans QML files for elements not supported in Qul, such as `ListView`, `Loader`, `GridLayout`, and `Flow`.

2. **Element Replacement**:
   - The `replace_elements` function transforms unsupported elements into alternatives:
     - `ListView` → `Column`
     - `GridLayout` → `Column`
     - `Flow` → `Row`
     - `Loader` → Commented out

3. **Batch File Conversion**:
   - The `convert_qml_files` function processes all `.qml` files in the input directory, applies transformations, and saves the results in the output directory.

4. **Main Function**:
   - The `main` function orchestrates the conversion process. It accepts input and output directory paths as arguments, ensuring the input directory exists before proceeding.

5. **Example Usage**:
   - The program can be run directly, with an example demonstrating how to provide input and output paths:
     ```python
     if __name__ == "__main__":
         example_input_dir = "path/to/your/qml/files"
         example_output_dir = "path/to/converted/qml/files"
         main(example_input_dir, example_output_dir)
     ```

## How to Use
1. Place your QML files in the input directory.
2. Specify the input and output directories in the `main` function or pass them as arguments.
3. Run the script to convert the QML files to a Qul-compatible format.

## Notes
- Only basic unsupported elements are replaced; complex dynamic behaviors must be handled manually.
- Ensure the output directory is writable and sufficient permissions are set.

## License
- MIT License
  
