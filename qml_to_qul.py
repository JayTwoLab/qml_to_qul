import os
import re

# 지원되지 않는 QML 요소 목록
unsupported_elements = ['ListView', 'Loader', 'GridLayout', 'Flow']

def detect_unsupported_elements(file_path):
    """
    QML 파일에서 지원되지 않는 요소를 탐지합니다.
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
    QML 코드에서 지원되지 않는 요소를 대체합니다.
    """
    # GridLayout -> Column으로 대체
    content = re.sub(r'\bGridLayout\b', 'Column', content)
    # ListView -> Column으로 대체
    content = re.sub(r'\bListView\b', 'Column', content)
    # Flow -> Row로 대체
    content = re.sub(r'\bFlow\b', 'Row', content)
    # Loader -> 주석 처리
    content = re.sub(r'\bLoader\b', '// Loader is not supported in Qul', content)
    return content

def convert_qml_files(input_dir, output_dir):
    """
    지정된 디렉토리의 QML 파일을 변환하고, 변환된 파일을 출력 디렉토리에 저장합니다.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.qml'):
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name)

            with open(input_path, 'r') as infile:
                content = infile.read()
                # 지원되지 않는 요소 탐지
                unsupported = detect_unsupported_elements(input_path)
                if unsupported:
                    print(f"Unsupported elements in {file_name}: {unsupported}")

                # 변환 규칙 적용
                new_content = replace_elements(content)

            with open(output_path, 'w') as outfile:
                outfile.write(new_content)
                print(f"Converted {file_name} and saved to {output_path}")

def main(input_directory, output_directory):
    """
    QML 변환기 메인 함수
    """
    if not os.path.exists(input_directory):
        print(f"Error: Input directory '{input_directory}' does not exist.")
        return

    print("Starting QML file conversion...")
    convert_qml_files(input_directory, output_directory)
    print("Conversion completed.")

if __name__ == "__main__":
    # 예제 실행: main 함수에 디렉토리 경로 전달
    example_input_dir = "path/to/your/qml/files"
    example_output_dir = "path/to/converted/qml/files"
    main(example_input_dir, example_output_dir)