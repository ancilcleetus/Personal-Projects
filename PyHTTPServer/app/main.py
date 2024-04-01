#!/usr/bin/env python3

# HTTP Server from scratch in Python

# Standard Library imports
import socket

# Third Party imports

# Local Application/Library specific imports


def main():
    # Bind to a Port
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept()  # Wait for client


if __name__ == "__main__":
    main()
