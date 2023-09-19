import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class WakeOnLan {

    public static final int PORT = 9;    // WOL are of often use UDP port 9

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java WakeOnLan <broadcast-ip> <mac-address>");
            System.out.println("Example: java WakeOnLan 192.168.1.255 00:1A:2B:3C:4D:5E");
            System.exit(1);
        }

        String ipStr = args[0];
        String macStr = args[1];

        try {
            byte[] macBytes = getMacBytes(macStr);
            byte[] bytes = new byte[6 + 16 * macBytes.length];

            // 6 bytes of FF
            for (int i = 0; i < 6; i++) {
                bytes[i] = (byte) 0xff;
            }

            // 16 times the MAC address
            for (int i = 6; i < bytes.length; i += macBytes.length) {
                System.arraycopy(macBytes, 0, bytes, i, macBytes.length);
            }

            InetAddress address = InetAddress.getByName(ipStr);
            DatagramPacket packet = new DatagramPacket(bytes, bytes.length, address, PORT);
            DatagramSocket socket = new DatagramSocket();
            socket.send(packet);
            socket.close();

            System.out.println("WOL Magic Packet sent!");
        } catch (Exception e) {
            System.out.println("Failed to send WOL Magic Packet: " + e.getMessage());
            e.printStackTrace();
        }
    }

    private static byte[] getMacBytes(String macStr) throws IllegalArgumentException {
        byte[] bytes = new byte[6];
        String[] hex = macStr.split("(:|-)");

        if (hex.length != 6) {
            throw new IllegalArgumentException("Invalid MAC address.");
        }

        try {
            for (int i = 0; i < 6; i++) {
                bytes[i] = (byte) Integer.parseInt(hex[i], 16);
            }
        } catch (NumberFormatException e) {
            throw new IllegalArgumentException("Invalid hex digit in MAC address.");
        }

        return bytes;
    }
}