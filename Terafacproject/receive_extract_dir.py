
import os

# Function to recreate files from the received output file
def extract_files_from_output(received_file, new_directory):
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    with open(received_file, 'r', encoding='utf-8', errors='ignore') as infile:
        file_content = ""
        current_file_name = None

        for line in infile:
            # If line starts with "Content of", it's a new file
            if line.startswith("Content of"):
                if current_file_name and file_content:
                    # Save the previous file content
                    save_path = os.path.join(new_directory, current_file_name)
                    with open(save_path, 'w', encoding='utf-8') as f:
                        f.write(file_content)
                    print(f"Created {save_path}")
                
                # Get the next file name from the line
                current_file_name = line.split("Content of ")[1].strip().replace(":", "")
                
                # Ensure the filename is valid and doesn't include invalid characters
                current_file_name = os.path.basename(current_file_name)
                
                file_content = ""
            elif line.startswith("="*50):
                continue  # Skip separator lines
            else:
                file_content += line  # Accumulate file content
        
        # Save the last file if it exists
        if current_file_name and file_content:
            save_path = os.path.join(new_directory, current_file_name)
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(file_content)
            print(f"Created {save_path}")

# Example usage
received_file = 'C:/Users/mevai/Terafacproject/received_output.txt'
new_directory = 'C:/Users/mevai/Terafacproject/extracted_files'

# Step: Extract the received file into a new directory
extract_files_from_output(received_file, new_directory)
