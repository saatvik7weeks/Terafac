

import socket

def send_file(file_path, host='localhost', port=12345):
    with open(file_path, 'rb') as f:
        file_data = f.read()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            conn.sendall(file_data)
            print(f"File {file_path} sent successfully.")

# Example usage: Send the output file
send_file('C:/Users/mevai/Terafacproject/output.txt')
