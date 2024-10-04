import os
import subprocess


def clone_repository(github_url, destination_folder):
    # Check if destination folder exists, if not create it
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    # Run the git clone command using subprocess
    try:
        subprocess.run(['git', 'clone', github_url, destination_folder], check=True)
        print(f"Repository cloned successfully into {destination_folder}")
    except subprocess.CalledProcessError as e:
        print(f"Error during cloning: {e}")

# Function to walk through files in the directory and save their content into an output file
def walk_and_save_to_file(directory, output_file):
    with open(output_file, 'w', encoding='utf-8', errors='ignore') as outfile:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        outfile.write(f"Content of {file_path}:\n")
                        outfile.write(content)
                        outfile.write("\n" + "="*50 + "\n")
                except Exception as e:
                    outfile.write(f"Could not read {file_path}: {e}\n")
    print(f"All file contents have been written to {output_file}")

# Example usage
# Replace with your actual GitHub repo URL
github_url = "https://github.com/saatvik7weeks/pokemonpedia" 
destination_folder = 'C:/Users/SAATVIK 7WEEKS/Download/Terafacproject-20240920T092156Z-001/Terafacproject/data'     # Directory where repo will be cloned
output_file_path = 'C:/Users/SAATVIK 7WEEKS/Downloads/Terafacproject-20240920T092156Z-001/Terafacproject/output.txt'  # File to save the output

# Step 1: Clone the repository
clone_repository(github_url, destination_folder)

# Step 2: Walk through the cloned repo and save content to the output file
walk_and_save_to_file(destination_folder, output_file_path)
