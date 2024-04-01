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

    while True:  # Keep the server running indefinitely, accepting new connections as they come in
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        try:
            # Read data from the connection
            request_data = client_socket.recv(1024)  # Up to 1024 bytes of data from the client
            decoded_request_data = request_data.decode()  # Decode the received bytes to a string using UTF-8 decoding
            print(f"Received data:\n{decoded_request_data}")

            # Extract the path from the request
            try:
                path = decoded_request_data.split()[1]  # Split by space and get the second part (the path)
            except IndexError:
                path = "/"

            # Determine response based on the path
            if path == "/":
                # Respond with HTTP/1.1 200 OK
                response = "HTTP/1.1 200 OK\r\n\r\n"  # Response contains Status Line, Empty Response Headers, Empty Response Body
            elif path.startswith("/echo/"):
                # Get the string after "/echo/"
                echo_string = path.split("/echo/")[-1]
                # Response contains Status Line, Non-empty Response Headers, echo_string Response Body
                response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(echo_string)}\r\n\r\n{echo_string}\r\n"
            else:
                # Respond with HTTP/1.1 404 Not Found
                response = "HTTP/1.1 404 Not Found\r\n\r\n"  # Response contains Status Line, Empty Response Headers, Empty Response Body
            
            client_socket.sendall(response.encode())  # Send the UTF-8 encoded response back to the client
        finally:
            # Close the connection
            client_socket.close()
    
    server_socket.close()  # This is good practice to clean up resources when the server is done


if __name__ == "__main__":
    main()
