import base64
import time
from scapy.all import IP, ICMP, send

def send_icmp_echo_request(encoded_data, target_ip):
    chunks = [encoded_data[i:i + 1024] for i in range(0, len(encoded_data), 1024)]
    total_bits = 0
    total_rtt = 0

    for chunk in chunks:
        start_time = time.time()
        send(IP(dst=target_ip) / ICMP(type=8) / chunk)
        
        end_time = time.time()

        rtt = end_time - start_time
        total_rtt += rtt
        total_bits += len(chunk) * 8

    average_bit_rate = total_bits / total_rtt
    print(f"Average Bit Rate: {average_bit_rate:.2f} bits per second")
    

if __name__ == "__main__":
    target_ip = "172.20.10.4"
    payload = b"payload "
    encoded_data = base64.b64encode(payload)
    print(encoded_data)
    send_icmp_echo_request(payload, target_ip)






