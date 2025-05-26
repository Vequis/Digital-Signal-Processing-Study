import os

def count_files_and_functions(directory):
    file_count = 0
    total_lines = 0
    function_count = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_count += 1
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    total_lines += len(lines)
                    function_count += sum(1 for line in lines if line.strip().startswith('def '))

    return file_count, total_lines, function_count

directory_path = 'predictions_oficial'
file_count, total_lines, function_count = count_files_and_functions(directory_path)
print(f"Number of files: {file_count}")
print(f"Total lines: {total_lines}")
print(f"Number of functions: {function_count}")