import socket
import argparse

def send_magic_packet(mac_address, broadcast_address='255.255.255.255', port=9):
    """
    Send a Wake-On-LAN magic packet to the specified MAC address.
    """
    # Construct the magic packet
    mac_bytes = [int(byte, 16) for byte in mac_address.split(':')]
    data = b'\xff' * 6 + bytes(mac_bytes) * 16

    # Send the magic packet using UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(data, (broadcast_address, port))

if __name__ == "__main__":
    # Parsing command line arguments
    parser = argparse.ArgumentParser(description='Send a Wake-On-LAN magic packet.')
    parser.add_argument('-m', '--macaddress', required=True, help='Target MAC address to send the magic packet to (format: XX:XX:XX:XX:XX:XX).')
    parser.add_argument('-b', '--broadcastaddress', default='255.255.255.255', help='Broadcast address to send the packet to. Defaults to 255.255.255.255.')
    args = parser.parse_args()

    send_magic_packet(args.macaddress, args.broadcastaddress)
    print(f"Sent WOL packet to {args.macaddress} via {args.broadcastaddress}")
