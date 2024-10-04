import socket

def receive_file(save_path, host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(save_path, 'wb') as f:
            while True:
                file_data = s.recv(1024)
                if not file_data:
                    break
                f.write(file_data)
            print(f"File received and saved to {save_path}.")

# Example usage: Receive and save the file
receive_file('C:/Users/mevai/Terafacproject/received_output.txt')
