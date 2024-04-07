from scapy.all import *
import base64

pkts = sniff(filter="icmp", timeout =15,count=2)

print(pkts)
payload = b""
for packet in pkts:
    if str(packet.getlayer(ICMP).type) == "8": 
        packet_payload = packet[ICMP].load
        
        if packet_payload:
            payload = payload + packet_payload
    
decoded_bytes = base64.b64decode(payload)
decoded_string = decoded_bytes.decode('utf-8')  

print(decoded_string)
            
            
            
            
            