import subprocess
import time
import os

# Set the directory where your Python scripts are located
SCRIPT_DIR = 'C:/Users/mevai/Terafacproject'

# Function to run a script and check for success
def run_script(script_name):
    print(f"Running {script_name}...")
    result = subprocess.run(['python', os.path.join(SCRIPT_DIR, script_name)])
    if result.returncode != 0:
        print(f"{script_name} failed.")
        exit(1)

# Execute scripts in order
run_script('clone_dir.py')
run_script('walk_read_1.py')

# Starts server_send_file.py in the background
print("Running server_send_file.py...")
server_process = subprocess.Popen(['python', os.path.join(SCRIPT_DIR, 'server_send_file.py')])

# Runs client_receive.py in a separate terminal window
print("Running client_receive.py in a new terminal...")
client_process = subprocess.Popen(['python', os.path.join(SCRIPT_DIR, 'client_receive.py')])

# Wait for both server and client processes to finish
server_process.wait()
client_process.wait()

# Execute receive_extract_dir.py
run_script('receive_extract_dir.py')

print("All scripts executed successfully.")
