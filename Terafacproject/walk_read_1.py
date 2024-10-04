import os
import subprocess

def walk_and_save_to_file(directory, output_file):
    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        outfile.write(f"Content of {file_path}:\n")
                        outfile.write(content)
                        outfile.write("\n" + "="*50 + "\n")
                except Exception as e:
                    outfile.write(f"Could not read {file_path}: {e}\n")

# # Example usage: Walk through a directory and save content to a file
directory_to_walk = 'C:/Users/mevai/terafacproject/data'
output_file_path = 'C:/Users/mevai/Terafacproject/output.txt'
walk_and_save_to_file(directory_to_walk, output_file_path)
