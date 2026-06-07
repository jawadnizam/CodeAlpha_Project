from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("=" * 50)
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)

sniff(prn=packet_callback, count=20)