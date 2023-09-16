# java-wake-on-lan
Wake on Lan  (WoL) in java code 

## Usage 
### get info of jre and jdk
- check JRE version

$ java -version
```
java version "1.8.0_381"
Java(TM) SE Runtime Environment (build 1.8.0_381-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.381-b09, mixed mode)```
```

- check JDK version

$ javac -version
```
javac 17.0.8
```

### compile
$ javac WakeOnLan.java 

But we can compile by the following way to make sure the version of JRE is the same as to the JDK. 
$ javac -source 1.8 -target 1.8 WakeOnLan.java

### execute 
$ java WakeOnLan 111.112.255.255 54:EA:F9:70:43:B3


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
