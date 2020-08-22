import struct
import socket
def main():
    Address = "127.0.0.1"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket successfully created")
    UDP_PORT = 69  # port
    server_socket.bind((Address, UDP_PORT))
    print("socket binded to %s" % (UDP_PORT))
    print("[SERVER] Socket info:", server_socket)
    print("[SERVER] Waiting...")
    server_socket.recv(69)

if __name__ == "__main__":
    main()