#!/usr/bin/env python3

# HTTP Server from scratch in Python

# Standard Library imports
import socket

# Third Party imports

# Local Application/Library specific imports


def main():
    # Bind to a Port
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server started. Waiting for incoming connections...")

    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Read data from the connection
    request_data = client_socket.recv(1024)  # Up to 1024 bytes of data from the client
    print("Received data:")
    print(request_data.decode())  # Decode the received bytes to a string using UTF-8 decoding
    
    # Respond with HTTP/1.1 200 OK
    response = "HTTP/1.1 200 OK\r\n\r\n"  # Response contains Status Line, Empty Response Headers, Empty Response Body
    client_socket.sendall(response.encode())  # Send the UTF-8 encoded response back to the client

    # Close the connection
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()
