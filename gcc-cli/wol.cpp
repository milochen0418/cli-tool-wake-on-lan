#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

#define WOL_PORT 9

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <broadcast-ip> <mac-address>\n", argv[0]);
        return 1;
    }

    unsigned char tosend[102];
    unsigned char mac[6];

    // Parse MAC address
    if (6 != sscanf(argv[2], "%hhx:%hhx:%hhx:%hhx:%hhx:%hhx", &mac[0], &mac[1], &mac[2], &mac[3], &mac[4], &mac[5])) {
        printf("Invalid MAC address format.\n");
        return 1;
    }

    // Build the magic packet
    for (int i = 0; i < 6; i++) {
        tosend[i] = 0xFF;
    }
    for (int i = 1; i <= 16; i++) {
        memcpy(&tosend[i * 6], &mac, 6 * sizeof(unsigned char));
    }

    // Create socket
    int sockfd = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (sockfd == -1) {
        perror("Failed to create socket");
        return 1;
    }

    // Set socket options for broadcasting
    int broadcastEnable = 1;
    if (setsockopt(sockfd, SOL_SOCKET, SO_BROADCAST, &broadcastEnable, sizeof(broadcastEnable))) {
        perror("Error: Failed to set socket to broadcast mode");
        close(sockfd);
        return 1;
    }

    // Set up address
    struct sockaddr_in serveraddr;
    memset(&serveraddr, 0, sizeof(serveraddr));
    serveraddr.sin_family = AF_INET;
    serveraddr.sin_port = htons(WOL_PORT);
    if (!inet_aton(argv[1], &serveraddr.sin_addr)) {
        perror("Invalid IP address format");
        close(sockfd);
        return 1;
    }

    // Send magic packet
    if (sendto(sockfd, &tosend, sizeof(unsigned char) * 102, 0, (struct sockaddr*) &serveraddr, sizeof(serveraddr)) == -1) {
        perror("Failed to send magic packet");
        close(sockfd);
        return 1;
    }

    printf("Magic packet sent to %s\n", argv[2]);
    close(sockfd);
    return 0;
}