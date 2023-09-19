# cli-tool-wake-on-lan
Wake on Lan  (WoL) in different code 

## Testing method for all cli tool.
In Mac, the Ethernet is using `en0`
We can do the following.
```bash
sudo tcpdump -i en0 udp port 9 -vv -X
```
to see the result like the following
```
tcpdump: listening on en0, link-type EN10MB (Ethernet), snapshot length 524288 bytes
23:30:07.711620 IP (tos 0x0, ttl 64, id 58157, offset 0, flags [none], proto UDP (17), length 130)
    172.20.10.4.49444 > broadcasthost.discard: [udp sum ok] UDP, length 102
        0x0000:  4500 0082 e32d 0000 4011 e125 ac14 0a04  E....-..@..%....
        0x0010:  ffff ffff c124 0009 006e 1e36 ffff ffff  .....$...n.6....
        0x0020:  ffff aabb ccdd eeff aabb ccdd eeff aabb  ................
        0x0030:  ccdd eeff aabb ccdd eeff aabb ccdd eeff  ................
        0x0040:  aabb ccdd eeff aabb ccdd eeff aabb ccdd  ................
        0x0050:  eeff aabb ccdd eeff aabb ccdd eeff aabb  ................
        0x0060:  ccdd eeff aabb ccdd eeff aabb ccdd eeff  ................
        0x0070:  aabb ccdd eeff aabb ccdd eeff aabb ccdd  ................
        0x0080:  eeff                                     ..
``````
## Different implmentation
We have the implementation of Java, GCC and Python right now.

## Introduction
### Introduction of Wake-on-LAN
**Wake-on-LAN (WoL) Principle**
Wake-on-LAN (WoL) is a protocol that allows a computer or other networked device to be turned on or woken up from a low-power or off state by a network message. The mechanism operates as follows:

1. **Magic Packet:** At the heart of the WoL technology is the "Magic Packet." This is a broadcast frame containing anywhere within its payload 6 bytes of all 255 (FF FF FF FF FF FF in hexadecimal), followed by sixteen repetitions of the target computer's 48-bit MAC address.
2. **Network Interface Card (NIC):** For WoL to work, the computer's Network Interface Card (NIC) must be WoL-capable. When the computer is powered down, the NIC remains partially active and listens for the Magic Packet.
3. **Broadcasting:** The Magic Packet is typically sent as a broadcast packet, destined for all computers in a subnet. This ensures that the packet reaches the intended machine even if its IP address changes or is not currently assigned.
4. **Activation:** Once the NIC detects its unique Magic Packet, it sends a signal to power on the computer. This is usually achieved by the NIC directly signaling the computer's motherboard.
5. **Configuration:** For WoL to work, it must be supported and enabled in both the computer's BIOS (or UEFI firmware) and its operating system. Additionally, any intermediate network devices, like switches, must allow broadcast traffic to pass.
6. **Use Cases:** WoL is particularly useful for remote system administration. For example, if an IT professional needs to perform maintenance on a machine outside of working hours, they can remotely wake up the machine, perform the necessary tasks, and then shut it down again.
7. **Limitations:** Wake-on-LAN operates on the local network in most typical setups. However, with the right network configuration and tools, it's possible to send a Magic Packet across the internet or through VPNs, known as "Wake-on-WAN."
---- 
In essence, Wake-on-LAN provides a way to remotely power on computers over a network, leveraging the listening capability of a computer's NIC for a specific sequence of data—the Magic Packet.
