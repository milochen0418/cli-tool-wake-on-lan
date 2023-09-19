import socket
import argparse

def send_magic_packet(mac_address, broadcast_address='255.255.255.255', port=9):
    """
    Send a Wake-On-LAN magic packet to the specified MAC address.
    
    Parameters:
    - mac_address (str): The MAC address to send the magic packet to.
    - broadcast_address (str): The broadcast address to send the packet to. Defaults to '255.255.255.255'.
    - port (int): The port to send the packet to. Defaults to 9.
    """
    # Construct the magic packet
    mac_bytes = [int(byte, 16) for byte in mac_address.split(':')]
    data = b'\xff' * 6 + bytes(mac_bytes) * 16

    # Send the magic packet using UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(data, (broadcast_address, port))

if __name__ == "__main__":
    # Parse the arguments.     
    parser.add_argument('-b', '--broadcastaddress', required=True, help='Broadcast IP Address')
    parser.add_argument('-m', '--macaddress', required=True, help='MAC Address')
    args = parser.parse_args()

    # Parsing command line arguments
    parser = argparse.ArgumentParser(description='Send a Wake-On-LAN magic packet.')
    parser.add_argument('-m' '--macaddress', help='Target MAC address to send the magic packet to (format: XX:XX:XX:XX:XX:XX).')
    parser.add_argument('-b', '--broadcastaddress', default='255.255.255.255', help='Broadcast address to send the packet to. Defaults to 255.255.255.255.')
    args = parser.parse_args()

    send_magic_packet(args.mac_address, args.broadcast)
    print(f"Sent WOL packet to {args.mac_address} via {args.broadcast}")
